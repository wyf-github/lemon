'''
    - -coding= utf-8- -
    @authour=Wangyafei
    @time=2019/3/12 19:07
    @file=run.py

'''

import sys
sys.path.append("./")

#执行用例，生成测试报告
import unittest
from project1.common import HTMLTestRunnerNew
from project1.test_cases.test_cases import TestCases
from project1.common import project_path
from project1.test_data import test_register
from project1.test_data import test_recharge
from project1.test_data import test_cases
from project1.test_data import test_invest
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestCases))
suite.addTest(loader.loadTestsFromModule(test_register))

#执行用例，生成测试报告
with open(project_path.testReport_path, 'wb+') as file:

 runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                         verbosity=2,
                                         title='python14 测试报告',
                                         description='python14 测试报告',
                                         tester='Yafei')
 runner.run(suite)
