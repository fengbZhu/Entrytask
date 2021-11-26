import os

BASE_PATH = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

PHONE_DATA = os.path.join(BASE_PATH, 'data', 'phone.yml')
ERRORCODE = os.path.join(BASE_PATH, 'data', 'errorCOde.yml')