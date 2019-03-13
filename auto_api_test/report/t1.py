import os
#用例存放的路径，加r是转义，因为有\  （#第二种方法：这种路径是写死的，复制别人的就会报错，所以选择动态获取）
#strtdir = r'D:\pycharm_project\auto_api_test\case'
#匹配规则
#获取当前脚本的路径(动态)
print(__file__)
curPath = os.path.realpath(__file__)
print(curPath)

filePath = os.path.dirname(curPath)
print(filePath)

reportPath = os.path.join(filePath,"report","report.html")
print(reportPath)

print(os.path.join(reportPath,"report.html"))