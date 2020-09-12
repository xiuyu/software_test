import requests ,time,json,threading,random

class test (object):
    headers = {
        "Content-type":"application/json"
    }

    def __init__(self,login_url,userName="",password=""):
        self.login_url = login_url
        self.userName = userName
        self.password = password
        self.session = requests.Session()
        self.session.headers = self.headers

    def login(self):
        data = {"userName":self.userName,"password":self.password}
        res = self.session.post(self.login_url,json.dumps(data))
        if res.json()["code"] == "0000":
            self.session.headers['X-AUTH-TOKEN'] = res.json()['token']
        return res.json()

    def register(self,register_url,params):
        res = self.session.post(register_url,json.dumps(params))
        print(res.json())
