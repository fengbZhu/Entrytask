import yaml

from conf.setting import PHONE_DATA, ERRORCODE


def get_response(Error_code, error_message=None, reference=None):
    res = {'Error_code': '', 'error_message': '', 'reference': ''}
    res['Error_code'] = int(Error_code)
    if error_message:
        res['error_message'] = error_message
    if reference:
        res['reference'] = reference
    else:
        del res['reference']
    return res


class GetData(object):
    # 获取数据
    def get_phonedata(self):
        with open(PHONE_DATA) as f:
            phone_data = yaml.load(f, Loader=yaml.FullLoader)
        return phone_data

    # 获取错误码信息，系统错误兜底
    def get_errorMsg(self,id):
        with open(ERRORCODE) as f:
            errorCodeMap = yaml.load(f, Loader=yaml.FullLoader)
            errorMsg = errorCodeMap.get(id)
            if errorMsg:
                errorCode = id
            else:
                errorCode = 11
                errorMsg = errorCodeMap.get(errorCode)
            return errorCode,errorMsg


GetData = GetData()
