from os.path import join, normpath
import os
SECRET_FILE_PATH = join(os.getcwd(),'etc', 'configs', 'secrets.ini')

SUCCESS_RESPONSE = {
    "status_code": 200,
    "data": {},
}

COMPLETED_STATUS = 'COMPLETED'
NOT_COMPLETED_STATUS = 'NOT_COMPLETED'