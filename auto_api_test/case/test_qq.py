# coding:utf-8
import requests
import unittest
class TestQQ(unittest.TestCase):
    '''测试qq功能'''
    def test_qq(self):
        '''测试qq号码，appkey是正确的'''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        #参数
        par = {
              "key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
              "qq":  "283340479"
               }
        #post请求
        r2 = requests.post(url, params=par)
        print(r2.text)  #获取的返回结果
        result = r2.json()["reason"]
        print(result)
        #断言
        self.assertTrue("success" == result)
        self.assertTrue("success" in r2.text)
        self.assertIn("success",r2.text)
        self.assertEqual("success",result,msg="失败的时候打印")
    def test_qq_appkey_error(self):
        '''测试qq号码，appkey是正确的'''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        #参数
        par = {
              "key": "1111111111111",  # appkey需要注册申请
              "qq":  "283340479"
               }
        #post请求
        r2 = requests.post(url, params=par)
        print(r2.text)  #获取的返回结果
        result = r2.json()["reason"]
        print(result)
        self.assertTrue("KEY ERROR!",result1)  #result故意写错的，为了测试报告中显示有错误的展示
if __name__ == "__main__":
    unittest.main()
