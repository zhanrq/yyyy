#coding:utf-8
import requests
host = "http://127.0.0.1"
class  SendFile():
    def __init__(self,s):
        self.s = s
    def sendImg(self):
        url2 = host +"http://127.0.0.1/zentao/file-ajaxUpload-5c862855cf421.html?dir=image"
        #ff = open("C:\fakepath\1.png","rb")
        body = {"localUrl":(None,"1.png"),
                 "imgFile":("1.png",open("1.png","rb"),"image/png")
                }
        #上传图片的时候不能用data和json，要用files
        r2 = self.s.post(url2,files=body)
        print(r2.text)
        try:
            jpg_url = r2.json()["url"]
            print(jpg_url)
        except Exception as msg:
            print("图片上传失败,原因：%s"%msg)
if __name__ == "__mian__":
    s = requests.session()
    send = SendFile(s)
    send.sendImg()
