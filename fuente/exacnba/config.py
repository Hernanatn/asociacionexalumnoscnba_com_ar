import os
import json
SECRET_KEY = '8b40751cdd916048c1e470c1cba23e13b5c01fa02e59051b77ca60056d96ffad229f3460fdc312fe50621f9ec3d5199c4c2dd886fbce6c36f1ccd97507654954cf3b75de76bdca49990cb7f1fc7a1c9c971028e385987a6e4a17a89ee5a7041c'
SESSION_COOKIE_SAMESITE='None'
SESSION_COOKIE_SECURE = True
CACHE_TYPE='FileSystemCache'
CACHE_DIR='/tmp/flaskcache'

GMAIL_CUENTA_DE_SERVICIO = {
    "type": "service_account",
    "project_id": "club-del-disco-newsletter",
    "private_key_id": "12801fad68d468b76bfa09b2eefa90fcf816586d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDUqhKCQGSFQWVL\ncY7rIhx3WCs+0sQvZTowIQmeJeCYfIEkaHkbDpIGGOTRun7aDx6NZNU/YjJB6mUc\nji3Lo2uqtCcnkFHvFoAEHMUbUFO/9K/6ao3tBFesekuD9IRkNP9hXN8YYHxp0evv\nsOgKjbAleRTlO+XvvTHoWR5J7Tdnzwwu7nH2dlKK3erwCV618UVq+DpHgUJmMGLE\nemuk9n7yUkzImvGNAAvQ5Zt5GZS1VEz4ox2o24fdDUJeDC1PNUyUJc7xo0n0jQik\nVvCIvqyT9gvMoUYVMG9DJsdW/VDNwsw0pYFVcZ7rKaFV/IxXweblYlmPq2AIpYxy\ncaUqIVmFAgMBAAECggEABNTsYLs3zXND6ufkmGEJBokhSmcdf/orzUYi4s33gV9q\ny7n37m5xUOQl5sH2+dtYFVxSIAOKIsdBjtmIHtVSr+kx7osv4V/AftdsfwdfL8BO\nc0ESgm0T1N5ectwOWfx+ROcIRpSCnyDe3G5Hh13av681k1O+EKlaxe2oa4ORO7GE\n+TO/bip21qLih9XkSlGz8ZLgFPvDUy+mgK1cEWw80VienGNom09qPoMIDkWq0Pa4\nf+VjMae1yfO+TzCkvI6J2Xa1cumPSHiRMHBqs82UYeBg963jteQV5yyG9bp/FInu\nGJf/rF5mdiBNY5sbaXydn/rJvjk357vvYvGvtg8lIQKBgQDvVp4vbiNV4+rL/Ddg\nD1kdQjj92uU1kDj8N9hiYRQXn4t+DzIySceEQ1DHmD7H8U0SFA25Zzn46lTVidpi\n8NtaM7cjf3/JiIdW3Vvl4CFTgVwld3c0ax2Ix0YFZhR5KM0i3wcisFA2v1cijxNE\nccBr7Z/JnoSoXUM+pRKd0gQNGQKBgQDjeBUCExZ3vCTzgLprRczkt05WwOF0sFGL\nSRbRmRudNU1DHifCZ9ZvfuuNrgMEBJSljceUN4D83itmTp1uAlKn7oU1DY9EPfiv\ntosXr/WDzd8KmXGyHETLclkVdC8Fiv8uJPJldX5y6X+1ozypn4LAJvgUUvwOrEVm\nPJiDAPjRTQKBgHKmSYxq9B5W2cjxfw1TDNtJN8fTLe1kswePMOafnmJamRW/7cnN\nMfgXzwBt29UnsEWyuYhQ/KJSjmTkbmrq+gjRsS8eCnbeIgbobvdFUHGSDDQecEn5\n7eHxo4c+iRwpAWts7xwc3a/8JJ93bkFhRE3vPJX2i5Gja2z84lgbnLkxAoGAFMXl\nnT/jAGJFOZua6qsAMC7xT4jjzgVAHSk6lT+XPv8cJDH/zYgwFBSSLGkky1wjuw68\nmDONawpbCkfJpr89jyqALb0kRUYnjNxtzWb7U+McKFqlAHAGdFHoAsaOeMId1bf4\nDv3w40uhpxPWOWNgzG2CoFCHxktDNzf3cZdIIc0CgYBA+r5z1RDIBkJoWBknO5UF\nTbFLzAQsCPtrLhKw/zGYzvRhOYyRh8sdsxx6T3fGntNivBs9FK3EBroDBWr8nH76\nUOk0RksvUOlXQCG/LlXA/UlCSMaJalCvst7canve14JQaej+Q+RlrY8QZfBvnqN7\nPkURGqhYbUF5RCtwOZy75g==\n-----END PRIVATE KEY-----\n",
    "client_email": "notificaciones-y-correos@club-del-disco-newsletter.iam.gserviceaccount.com",
    "client_id": "104997614823427409757",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/notificaciones-y-correos%40club-del-disco-newsletter.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
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