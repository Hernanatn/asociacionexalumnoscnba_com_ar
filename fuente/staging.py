import os 

import sys

path = '/var/www/asociacionexalumnoscnba_com_ar/fuente/'
if path not in sys.path:
    sys.path.append(path)

os.environ['EXACNBA_AMBIENTE'] = 'STAGING'
from exacnba import servidor as application