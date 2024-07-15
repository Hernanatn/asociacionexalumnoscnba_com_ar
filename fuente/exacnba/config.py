import os
import json
SECRET_KEY = '8b40751cdd916048c1e470c1cba23e13b5c01fa02e59051b77ca60056d96ffad229f3460fdc312fe50621f9ec3d5199c4c2dd886fbce6c36f1ccd97507654954cf3b75de76bdca49990cb7f1fc7a1c9c971028e385987a6e4a17a89ee5a7041c'
SESSION_COOKIE_SAMESITE='None'
SESSION_COOKIE_SECURE = True
CACHE_TYPE='FileSystemCache'
CACHE_DIR='/tmp/flaskcache'

GMAIL_CUENTA_DE_SERVICIO = {
}

if not os.environ.get('EXACNBA_AMBIENTE') or os.environ.get('EXACNBA_AMBIENTE') == 'DESARROLLO':
    URL_BASE='http://127.0.0.1:5000'
    CSS = 'css'
elif os.environ.get('EXACNBA_AMBIENTE') == 'STAGING':
    URL_BASE='https://pruebas.asociacionexalumnos.com.ar'
    CSS = 'min-css'
elif os.environ.get('EXACNBA_AMBIENTE') == 'PRODUCCION':
    URL_BASE='https://asociacionexalumnos.com.ar'
    CSS = 'min-css'