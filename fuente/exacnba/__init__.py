from flask import Flask, current_app, session as cookieSesion, g, redirect as redireccionar, request as solicitud, render_template as renderizarPlantilla, url_for as rutaRelativa, make_response as crearRespuesta
from flask.wrappers import Request, Response
from werkzeug.datastructures import Headers
from flask_caching import Cache
from flask_minify import Minify

from datetime import timedelta as deltaTiempo, date
from re import sub as sustituir

from exacnba.base_de_datos import BaseDeDatos

from html import escape as escaparCaracteresHTML, unescape as desescaparCaracteresHTML 
from requests import get

import os

servidor = Flask \
(
    __name__.split('.')[0],
    static_url_path='',
    static_folder='estatico',
    template_folder='plantillas'
)


servidor.config.from_pyfile('config.py')
cache = Cache(servidor)

def devolverBDD() -> BaseDeDatos:
    if 'bdd' not in g or g.bdd is None:
        g.bdd = BaseDeDatos()
    return g.bdd


@servidor.before_request
def staging():
    if os.environ.get('EXACNBA_AMBIENTE') == 'STAGING':
        if 'exacnba' not in solicitud.path:
            redireccionar(f'/exacnba/{solicitud.path}')

servidor.jinja_env.globals.update(servidor=servidor)

from exacnba.vistas import *
