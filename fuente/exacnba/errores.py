from flask import Flask, session as cookieSesion, g, redirect as redireccionar, make_response as crearRespuesta, request as solicitud, render_template as renderizarPlantilla, url_for as rutaRelativa, send_from_directory as enviarDesdeDirectorio
from flask.wrappers import Request, Response
from jinja2.exceptions import UndefinedError
from werkzeug.datastructures import Headers

from http import HTTPStatus, HTTPMethod
from mimetypes import guess_type

from markupsafe import escape

from secrets import token_urlsafe
from base64 import b64encode, b64decode

from requests import get, post, put, patch, delete
from json import loads, dumps

from re import compile as compilarRegex, search as buscarRegex, Pattern as PatronRegex

from exacnba import servidor
from exacnba.base_de_datos.tipos import *
from exacnba.base_de_datos.errores import *
from mysql.connector.errors import OperationalError

from flask.templating import TemplateNotFound
from werkzeug.exceptions import HTTPException, BadRequest, NotFound
import traceback




@servidor.errorhandler(TemplateNotFound)
def manejarPlantillaNoExiste(e):
    servidor.logger.error(f'--- {solicitud.full_path} => {solicitud.endpoint}() --- \n {type(e)} {e} \n {traceback.format_exc()}')
    

@servidor.errorhandler(FileNotFoundError)
def manejarArchivoNoEncontrado(e):
    servidor.logger.debug(f'--- {solicitud.full_path} => {solicitud.endpoint}() --- \n {type(e)} {e} \n {traceback.format_exc()}')
    
@servidor.errorhandler(404)
def manejar404(e): 
    servidor.logger.debug(f'--- {solicitud.full_path} => {solicitud.endpoint}() --- \n {type(e)} {e}')
    try:
        return renderizarPlantilla(
            f"/errores/404.html.j2",
            USUARIO = g.esteUsuario
        )
    except (TemplateNotFound, UndefinedError, AttributeError):
        return renderizarPlantilla(
            f"/errores/publico/404.html.j2",
        )
    return crearRespuesta(msj,404)



@servidor.errorhandler(OperationalError)
@servidor.errorhandler(ErrorBDD)
def manejarErrorBDD(e):
    import traceback
    servidor.logger.error(f"{e} \n {traceback.format_exc()}")
    respuesta = crearRespuesta("",429)
    respuesta.headers['Retry-After'] = 1
    return respuesta


@servidor.errorhandler(500)
@servidor.errorhandler(AssertionError)
@servidor.errorhandler(Exception)
@servidor.errorhandler(ErrorMalaSolicitud)
def manejar500(e):
    servidor.logger.error(f'--- {solicitud.full_path} => {solicitud.endpoint}() --- \n {type(e)} {e} \n {traceback.format_exc()}')
    msj = f'No pudimos procesar tu solicitud. {e}'

    plantilla = f"/errores/indicador-hx-error.html.j2" if solicitud.referrer is not None and servidor.config.get('URL_BASE') in solicitud.referrer else f"/{idioma}/errores/publico/baseError.html.j2" 
    respuesta = crearRespuesta(
        renderizarPlantilla(
            plantilla,
            ERROR = msj
        )
    )
    respuesta.headers['HX-Retarget'] = '#indicador-cargando-mensaje'
    respuesta.headers['HX-Reselect'] = '#indicador-cargando-mensaje'
    respuesta.headers['HX-Reswap'] = 'outerHTML'
    respuesta.headers['HX-Push-Url'] = 'false'
    return respuesta
    
