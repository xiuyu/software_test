from press import press
from test import test

if __name__ == '__main__':
    login_url = "http://47.96.181.17:9090/rest/toController"
    obj = press(login_url,userName="J201903070064",password="362387359")
    obj.run()
    # 接口测试
    #             login_url = "http://47.96.181.17:9090/rest/toController"
    #             register_url = "http://47.96.181.17:9090/rest/ac01CrmController"
    #             obj = test(login_url,userName="J201903070064",password="362387359")
    #             res = obj.login()
    #
    #             if res["code"] == "0000":
    #                 print("获取token成功", res["token"])
    #                 params = {
    #                     "aac003": "张三",
    #                     "aac004": "1",
    #                     "aac011": "21",
    #                     "aac030": "13575726588",
    #                     "aac01u": "88002255",
    #                     "crm003": "1",
    #                     "crm004": "1",
    #                     "crm00a": "2018-11-11",
    #                     "crm00b": "aaaaaa",
    #                     "crm00c": "2019-02-28",
    #                     "crm00d": "bbbbbb"
    #                 }
    #                 obj.register(register_url,params)









