from werkzeug.datastructures.file_storage import FileStorage
from PIL import Image
import os 
def guardarImagen(imagen : FileStorage, dirDestino : str, nombreArchivo : str) -> str:

    imagenBase : str = Image.open(imagen)
    nombreArchivoImagen : str = f"{nombreArchivo}.webp".encode('ascii','ignore').decode('ascii')
    archivoDestino = os.path.join(dirDestino,nombreArchivoImagen) 
    
    imagenMaxi = imagenBase
    imagenMaxi.save(os.path.join(dirDestino,'maxi',nombreArchivoImagen), lossless = True, quality=30)
    
    imagen = imagenBase.copy()
    imagen.thumbnail((300,300))
    imagen.save(os.path.join(dirDestino,nombreArchivoImagen), quality= 70)

    imagenMedia = imagenBase.copy()
    imagenMedia.thumbnail((200,200))
    imagenMedia.save(os.path.join(dirDestino,'media',nombreArchivoImagen), quality= 50)
    
    imagenMini = imagenBase.copy()
    imagenMini.thumbnail((75,75))
    imagenMini.save(os.path.join(dirDestino,'mini',nombreArchivoImagen), quality=40 )

    return nombreArchivoImagen
