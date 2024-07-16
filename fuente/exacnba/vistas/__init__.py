from flask import Flask, session as cookieSesion, g, redirect as redireccionar, make_response as crearRespuesta, request as solicitud, render_template as renderizarPlantilla, url_for as rutaRelativa, send_from_directory as enviarDesdeDirectorio
from flask.wrappers import Request, Response
from werkzeug.datastructures import Headers


#from http import HTTPStatus, HTTPMethod
from mimetypes import guess_type

from markupsafe import escape

from secrets import token_urlsafe
from base64 import b64encode, b64decode

from requests import get, post, put, patch, delete
from json import loads, dumps

from re import compile as compilarRegex, search as buscarRegex, Pattern as PatronRegex

from collections import namedtuple

from exacnba import servidor


#PAGINAS
@servidor.route("/")
def inicio():
    return renderizarPlantilla("/inicio.html.j2")
@servidor.route("/la-asociacion")
def laAsociacion():
    return renderizarPlantilla("/la-asociacion.html.j2")
@servidor.route("/promociones")
def promociones():
    return renderizarPlantilla("/promociones.html.j2")
@servidor.route("/beneficios")
def beneficios():
    return renderizarPlantilla("/beneficios.html.j2")
@servidor.route("/actividades")
def actividades():
    return renderizarPlantilla("/actividades.html.j2")
@servidor.route("/novedades")
def novedades():
    return renderizarPlantilla("/novedades.html.j2")


#CONTACTO
@servidor.route("/contacto", methods=["GET"])
def contactoGET():
    return renderizarPlantilla("/parciales/contactoBase.html.j2")
@servidor.route("/contacto", methods=["POST"])
def contactoPOST():
    return renderizarPlantilla("/parciales/contactoCorrecto.html.j2")