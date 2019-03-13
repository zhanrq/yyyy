# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
# s = requests.session()  # 全局的s
class LoginLgw():

    def __init__(self, s):
        self.s = s

    def get_token(self):
        '''
        fuction: 获取token
        args: s 参数 -》s = requests.session()
        :return  anti_token  ->{'X-Anit-Forge-Token': 'xx', 'X-Anit-Forge-Code': '38515842'}
       '''
        # 局部的s没定义，从外部传入s
        url = 'https://passport.lagou.com/login/login.html'
        h1 = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
            }
        r1 = self.s.get(url, headers=h1, verify=False)
        # print(r1.text)

        soup = BeautifulSoup(r1.content, "html.parser", from_encoding='utf-8')

        a = soup.findAll('script')[1].getText().splitlines()
        anti_token = {}
        anti = [str(x) for x in a]
        anti_token['X-Anit-Forge-Token'] = re.findall(r'= \'(.+?)\'', anti[1])[0]
        anti_token['X-Anit-Forge-Code'] = re.findall(r'= \'(.+?)\'', anti[2])[0]
        # 获取token和code
        # print(anti_token)  # dict  # print只是打印出来看下，心理作用，心理踏实一点
        return anti_token


    def login_lgw(self, anti_token, user, psw):

        url2 = 'https://passport.lagou.com/login/login.json'
        h2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "X-Anit-Forge-Token": anti_token['X-Anit-Forge-Token'] ,
            "X-Anit-Forge-Code": anti_token['X-Anit-Forge-Code'],
            "Referer": "https://passport.lagou.com/login/login.html"
            }
        body = {
                "isValidate": "true",
                "username": user,
                "password": psw,
                "request_form_verifyCode": "",
                "submit": ""
            }
        print(self.s.headers)  # s的头部

        # 更新s的头部
        self.s.headers.update(h2)
        print(self.s.headers)
        r2 = self.s.post(url2, data=body, verify=False)
        print(r2.text)
        return r2.json()

if __name__ == "__main__":
    # 自测的内容
    ss = requests.session()
    lgw = LoginLgw(ss)
    token = lgw.get_token()
    lgw.login_lgw(token, "1212", "2222")