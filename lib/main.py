import time

import flask, json
from flask import request

from lib.tools import get_response, getdata

server = flask.Flask(__name__)


@server.route('/searchPhone', methods=['get'])
def searchPhone():
    data = request.get_json()
    try:
        a = data['a']
        b = data['b']
        # a = int(request.args.get('a'))
        # b = request.args.get('b')
        if not b or (a and type(a) != int):
            msg = getdata.get_errorMsg(21)
            response = get_response(error_code=msg[0], error_message=msg[1])
        else:
            phone_data = getdata.get_phonedata()
            time.sleep(0.5)
            phone_bysearch = []
            for i in phone_data:
                name = i.get('name')
                id = i.get('id')
                if a:
                    if a == id and b == name:
                        phone_bysearch.append(i)
                else:
                    if b == name:
                        phone_bysearch.append(i)
            if not phone_bysearch:
                msg = getdata.get_errorMsg(21)
                response = get_response(error_code=msg[0], error_message=msg[1])
            elif len(phone_bysearch) == 1:
                reference = phone_bysearch[0].get('phone')
                msg = getdata.get_errorMsg(0)
                response = get_response(error_code=msg[0], error_message=msg[1],reference=reference)
            else:
                msg = getdata.get_errorMsg(22)
                response = get_response(error_code=msg[0], error_message=msg[1])
        return json.dumps(response, ensure_ascii=False)
    except Exception as e:
        print(e)
        msg = getdata.get_errorMsg(11)
        response = get_response(error_code=msg[0], error_message=msg[1])
        return json.dumps(response, ensure_ascii=False)

