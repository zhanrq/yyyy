#coidng:utf-8
import unittest
#从工程下面的第一层开始导入
from common.Html_Runner import HTMLTestRunner   #HTMLTestRunner这是个加载器
import os
#用例存放的路径，加r是转义，因为有\  （#第二种方法：这种路径是写死的，复制别人的就会报错，所以选择动态获取）
#strtdir = r'D:\pycharm_project\auto_api_test\case'
#匹配规则
#获取当前脚本的路径
curPath = os.path.dirname(os.path.realpath(__file__))
#用例的路径
strtdir = os.path.join(curPath,"case")
reportPath = os.path.join(curPath,"report","report.html")
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(strtdir,rule)
print(discover)
#这个报告太低级了，所以要被替换
# runner = unittest.TextTestRunner()  #批量执行
# runner.run(discover)
#本节主要讲批量运行所有用例，1.发现所有用例（包括所在地址和匹配规则）2、执行即可
#执行之后发现现实不可观，所以生成一个测试报告，方便观察，步骤先建一个common，新建一个Htmi_Runner,把群文件下载的内容粘贴进去即可
#导入之后下边写生成的报告

#这个可以生成高级的HTML报告
fp = open("report.html","wb")
runner = HTMLTestRunner(fp,
                        title="报告的标题，这是我的借口项目",
                        description="报告如下",
                        verbosity=2, #类注释展示
                        retry=1) #失败重跑

runner.run(discover)   #运行
fp.close()
