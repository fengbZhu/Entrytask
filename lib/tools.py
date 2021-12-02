import yaml

from conf.setting import PHONE_DATA, ERRORCODE_DATA


def get_response(error_code, error_message=None, reference=None):
    res = {'error_code': int(error_code), 'error_message': '', 'reference': ''}
    if error_message:
        res['error_message'] = error_message
    if reference:
        res['reference'] = reference
    else:
        del res['reference']
    return res


class GetData(object):
    # 获取数据
    @staticmethod
    def get_phonedata():
        with open(PHONE_DATA) as f:
            phone_data = yaml.load(f, Loader=yaml.FullLoader)
        return phone_data

    # 获取错误码信息，系统错误兜底
    @staticmethod
    def get_errorMsg(id):
        with open(ERRORCODE_DATA) as f:
            errorless = yaml.load(f, Loader=yaml.FullLoader)
            erroneous = errorless.get(id)
            if erroneous:
                errcode = id
            else:
                errcode = 11
                erroneous = errorless.get(errcode)
            return errcode, erroneous


get_data = GetData()
