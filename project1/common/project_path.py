'''
    - -coding= utf-8- -
    @authour=Wangyafei
    @time=2019/3/13 18:21
    @file=project_path.py
    所有文件的路径

'''
import os
project_path=os.path.split(os.path.dirname(__file__))[0]
print(project_path)

#测试用例的路径
testcases_path=os.path.join(project_path,'test_cases','test_api.xlsx')
print(testcases_path)



#测试报告的路径
testReport_path=os.path.join(project_path,'test_result','test_report','Test_report.html')
print(testReport_path)

#测试log的路径
log_path=os.path.join(project_path,'test_result','test_log','log.txt')
print(log_path)

#配置文件的路径
conf_path=os.path.join(project_path,'conf','case.conf')
print(conf_path)
