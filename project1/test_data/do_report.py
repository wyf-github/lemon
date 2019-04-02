'''
    - -coding= utf-8- -
    @authour=Wangyafei
    @time=2019/3/14 15:47
    @file=do_report.py
'''
#执行用例，生成测试报告
import unittest
from project1.test_data.test_cases import TestCases
from project1.common import HTMLTestRunnerNew

#测试集
suit=unittest.TestSuite

#添加用例
loader=unittest.TestLoader

suit.addTest(loader.loadTestsFromTestCase(testCaseClass=TestCases))

#执行用例，生成测试报告
with open('Test_report.html','wb+') as file:

 runner=HTMLTestRunnerNew.HTMLTestRunner(stream='Test_report.html',
                                        verbosity=2,
                                        title='python14 测试报告',
                                        description='python14 测试报告',
                                        tester='Yafei')
 runner.run(suit)
