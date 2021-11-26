import flask, json
from flask import request

from lib.tools import get_response, GetData

server = flask.Flask(__name__)


@server.route('/searchPhone', methods=['get'])
def searchPhone():
    data = request.get_json()
    try:
        a = data['a']
        b = data['b']
        if not b or (a and type(a) != int):
            errorMsg = GetData.get_errorMsg(21)
            response = get_response(Error_code=errorMsg[0], error_message=errorMsg[1])
        else:
            phone_data = GetData.get_phonedata()
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
                errorMsg = GetData.get_errorMsg(21)
                response = get_response(Error_code=errorMsg[0], error_message=errorMsg[1])
            elif len(phone_bysearch) == 1:
                reference = phone_bysearch[0].get('phone')
                errorMsg = GetData.get_errorMsg(0)
                response = get_response(Error_code=errorMsg[0], error_message=errorMsg[1],reference=reference)
            else:
                errorMsg = GetData.get_errorMsg(22)
                response = get_response(Error_code=errorMsg[0], error_message=errorMsg[1])
        return json.dumps(response, ensure_ascii=False)
    except Exception as e:
        errorMsg = GetData.get_errorMsg(11)
        response = get_response(Error_code=errorMsg[0], error_message=errorMsg[1])
        return json.dumps(response, ensure_ascii=False)
