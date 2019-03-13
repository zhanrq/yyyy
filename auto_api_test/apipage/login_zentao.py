#coding:utf-8
import requests
host = "http://127.0.0.1"
class LoginZentao():
    def __init__(self,s):
        self.s = s
    def login(self,user="admin",psw="e10adc3949ba59abbe56e057f20f883e"):
        #s = requests.session()  #代码里面的微型浏览器
        url = host+"/zentao/user-login-L3plbnRhby8=.html"

        body ={
                "account":user,
                "password":psw,
                "referer":"/zentao/"
        }
        r = self.s.post(url,data=body)

        print(r.content.decode("utf-8"))
if __name__ == "__main__":
    s = requests.session()# 一：定义s参数
    zentao = LoginZentao(s)  #实例化
    zentao.login()


