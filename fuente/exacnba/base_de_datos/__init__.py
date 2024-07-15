from collections import namedtuple

from mysql.connector import connect
from mysql.connector.pooling import MySQLConnectionPool as ConexionesMultiplesMySQL, PooledMySQLConnection as ConexionMySQL, CNX_POOL_MAXSIZE, PoolError 
from mysql.connector.cursor import MySQLCursorBufferedDict, MySQLCursorBufferedNamedTuple
from mysql.connector.errors import DatabaseError as ErrorMySQL
from solteron import Solteron
#from exacnba.base_de_datos.tipos import * 
from exacnba.base_de_datos.errores import *
import os
from typing import Optional,Self,Dict,Any,List

CursorMySQL = MySQLCursorBufferedDict | MySQLCursorBufferedNamedTuple

class ConfigBDD(metaclass=Solteron):

    __HOST : str = "localhost"
    __USUARIO : str = "servidor_local"
    __CONTRASENA : str = "Servidor!1234"
    __NOMBRE_BDD : Optional[str] = "BaseDePrueba"

    __root : str = "root"
    __root_p : str = "Root!1234"

    @property
    def PARAMETROS_CONEXION(self) -> dict: 
        return \
        {
            "host" : self.__HOST,
            "user" : self.__USUARIO,
            "password" : self.__CONTRASENA,
            "database" : self.__NOMBRE_BDD
        }

    @property
    def PARAMETROS_ROOT(self) -> dict: 
        return \
        {
            "host" : self.__HOST,
            "user" : self.__root,
            "password" : self.__root_p,
            "database" : self.__NOMBRE_BDD
        }

    @property
    def PARAMETROS_MULTIPLES(self) -> dict:
        return \
        {
            "pool_name" : f"{self.__NOMBRE_BDD}_POOL",
            "pool_size" : int(CNX_POOL_MAXSIZE / 8)     
        }

    @property
    def OPCION_CURSOR(self) -> dict:
        return \
        {
           "dictionary" : True,
           "named_tuple" : False,   
        }

class BaseDeDatos():
    """
    Clase que representa la 'pool' de conexiones con la base de datos.
    Se puede iniciarlizar pasando una configuración, por defecto utiliza los valores del Singleton `ConfigBDD`
    
    Interfaz pública:  
    `conectar()` establece una ConexionMySQL.  
    `desconectar()` cierra el cursor y la conexión vivas.  
    `ejecutar(consultaSQL, multiconsulta)` ejecuta la consulta SQL provista, y devuelve la propia BDD.

    `devolverUnResultado()` si se llama luego de una consulta, devuelve el primer resultado.  
    `devolverResultados(cantidad)` devuelve la cantidad de resultados solicitada, o todos, si se omite.  
    `devolverIdUltimaInsercion()` devuelve el id auto incrementado de la última insercion en una tabla.  

    `conexion` establece una ConexionMySQL (si no la hay) y la devuelve.  
    `cursor` establece una ConexionMySQL (si no la hay) y devuelve el cursor asociado a la misma.
    
    **Se puede utilizar dentro de un `contexto`, ejemplo:**
    >>> esteDisco = None
    >>> with BaseDeDatos() as bdd:
    >>>     esteDisco(bdd, **parámetros)
    >>>     id = esteDisco.guardar()
    >>>
    >>> # Esto garantiza que `desconectar()` será llamado al cerrar el contexto,   
    >>> # y la conexión será devuelta a la 'pool' o terminada.  
    >>> #   
      

    **Se pueden encadenar ejecución y resultados, ejemplo:**
    >>> with bdd:
    >>>     datos = bdd.ejecutar(f"SELECT * FROM Usuarios WHERE idSesion = '{idSesion}'") \\
    >>>            .devolverUnResultado()
    >>>


    """
    __slots__ = \
    (
        "__config",
        "__pool",
        "__conexion",
        "__cursor"
    )

    __config : Optional[dict]
    #Interfaz Pública

    @property
    def conexion(self) -> ConexionMySQL:
        """Una conexión con la Pool de Conexiones MySQL. Si la Base no está conectada, conecta.
        """
        if self.__conexion is None:
            self.conectar()
        return self.__conexion
  
    @property
    def cursor(self) -> CursorMySQL:
        """El cursor asociado a la conexión MySQL. Si la Base no está conectada, conecta.
        """
        if self.__cursor == None:
            self.__cursor = self.conexion.cursor(buffered=True,**self.__config.OPCION_CURSOR)
            #[HACER] RESOLVER QUE LA CONEXION SE CAE

        return self.__cursor

    def conectar(self) -> Self:
        """
        Establece una conexión en pool con el servidor MySQL y recupera una conexión individual.
        ### Devuelve:
        :arg BaseDeDatos Self: Esta instancia de BaseDeDatos.
        ### Levanta:
        :arg PoolError: Si la Pool de Conexiones está llena.
        :arg Exception: Propaga errores de conexión con la BDD.     

        """
        if self.__config is None : 
            match os.environ.get('CDD_AMBIENTE'):
                case 'PRODUCCION':
                    self .__config = ConfigBDDDigitalOceanProduccion()
                case 'STAGING':
                    self .__config = ConfigBDDDigitalOceanStaging()
                case 'DESAROLLO' | _:
                    self.__config = ConfigBDD()

            #f"[DEBUG]{self.__config.__class__.__name__}")
    
        if self.__conexion is not None : return self
        if self.__pool is not None: 
            self.__conexion = self.__pool.get_connection()
        else:
            try: 
                self.__pool = ConexionesMultiplesMySQL \
                        (
                            **self.__config.PARAMETROS_MULTIPLES,
                            **self.__config.PARAMETROS_CONEXION,
                        )
                self.__conexion = self.__pool.get_connection()
            except PoolError as e: 
                raise ErrorPoolLlena(f"No se pudo crear la Conexión {e}. Pool llena.")
            except ErrorMySQL as f: 
                self.reconectar()
                #return self.conectar()
                raise ErrorDemasiadasConexiones(f"No se pudo crear la Conexión {f}. Demasiadas conexiones.")
            except Exception as g:
                raise g
                #[HACER] RESOLVER QUE LA CONEXION SE CAE

        return self

    def ejecutar(self, consultaSQL : str, multiconsulta : bool = True) -> Self:
        """
        Ejecuta y *commitea* la consulta provista y devuelve el ``cursor`` para manejar los resultados.
        ### Parámetros:
        :param str consultaSQL: la consulta a ejecutar.
        :param bool multiconsulta: si se realiza más de un procedimiento en simultaneo, por defecto es ``True``
        ### Devuelve:
        :param CursorMySQL: el cursor con los resultados en búfer.
        ### Levanta:
        :arg Exception: propaga excepciones de conexión con la BDD.
        """
        try:
            self.cursor.execute(consultaSQL, multi = multiconsulta)
            self.conexion.commit()
        except ErrorBDD as e:
            ###print(f"[ERROR] {e}")
            self.reconectar()
            self.cursor.execute(consultaSQL, multi = multiconsulta)
            self.conexion.commit()
        except AttributeError as e:
            ###print(f"[ERROR] {e}")
            self = BaseDeDatos()
            self.conectar()
            self.cursor.execute(consultaSQL, multi = multiconsulta)
            self.conexion.commit()

        return self

    def devolverIdUltimaInsercion(self) -> Optional[int]:
        return self.__cursor.lastrowid

    def devolverUnResultado(self) -> Optional[Dict[str, Any]]:
        """
        Devuelve el primer resultado de la última consulta.
        """
        return self.__cursor.fetchone()
        
    def devolverResultados(self, cantidad : Optional[int] = None) -> Optional[List[Dict[str, Any]]]:
        resultados = self.__cursor.fetchall()
        
        if not resultados: return None
        elif cantidad is None: return resultados
        elif cantidad == 0: return []
        elif cantidad > 0: return resultados[0:cantidad-1]
        else: raise IndexError("Se solicitó una cantidad negativa de resultados, lo cual es un sinsentido.")

    def desconectar(self):
        if self.__cursor is not None:
            self.__cursor.close()
            del self.__cursor
            self.__cursor = None
        if self.__conexion is not None:
            self.__conexion.close()
            del self.__conexion
            self.__conexion = None
    
    def reconectar(self) -> Self:
        self.__matar()
        if self.__config is None : 
            match os.environ.get('CDD_AMBIENTE'):
                case 'PRODUCCION':
                    self .__config = ConfigBDDDigitalOceanProduccion()
                case 'STAGING':
                    self .__config = ConfigBDDDigitalOceanStaging()
                case 'DESAROLLO' | _:
                    self.__config = ConfigBDD()
        if self.__conexion is not None : return self
        if self.__pool is not None: 
            self.__conexion = self.__pool.get_connection()
        else:
            try:
                self.__pool = ConexionesMultiplesMySQL \
                        (
                            **self.__config.PARAMETROS_MULTIPLES,
                            **self.__config.PARAMETROS_CONEXION,
                        )
                self.__conexion = self.__pool.get_connection()
            except ErrorMySQL as e:
                raise ErrorBDD(f" {e}. {self.__config.__class__.__name__=}|{os.environ.get('CDD_AMBIENTE')=}")
        return self

    def __matar(self):
        if self.__cursor is not None:
            c = self.__cursor.reset()
            if c is not None:
                c.execute("SELECT id FROM INFORMATION_SCHEMA.PROCESSLIST;")
                resultados = self.__cursor.fetchall()
                hilosDeEstaConexión = (resultado.get('id') for resultado in resultados)
                for h in hilosDeEstaConexión:
                    self.__cursor.execute\
                    (
                        f"KILL {h};"
                    )
                del self.__cursor
                del self.__conexion
                del self.__pool
                
                self.__cursor = None
                self.__conexion = None
                self.__pool = None
                return   
        
        self.desconectar()
        if self.__cursor is not None:
            self.__cursor.close()
            self.__conexion.cmd_process_kill
        if self.__conexion is not None:
            self.__conexion.close()
        if self.__pool is not None:
            self.__pool._remove_connections()
            del self.__pool
            self.__pool = None


    def __init__(self, configuracion : Optional[ConfigBDD] = None) -> None:
        self.__config = configuracion
        self.__conexion = None
        self.__pool = None
        self.__cursor = None

    def __del__(self):
        self.__matar()

    # with BaseDeDatos() as bdd
    def __enter__(self) -> 'BaseDeDatos':
        if self.__conexion is None:
            return self.conectar()
        # ###print(f"[DEBUG] Entrando {self.__cursor=}{self.__conexion=}{self.__pool=}")
        return self

    def __exit__(self, exc_type,excl_val,exc_tb) -> None:
        # ###print(f"[DEBUG] Saliendo {self.__cursor=}{self.__conexion=}{self.__pool=}")
        self.desconectar()