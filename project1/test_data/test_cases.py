'''
    - -coding= utf-8- -
    @authour=Wangyafei
    @time=2019/3/14 8:00
    @file=test_cases.py
'''
import unittest
from ddt import ddt,data,unpack
from project1.common.do_requests import HttpRequest
from project1.common.do_excel import DoExcel
from project1.common import project_path

test_data = DoExcel(project_path.testcases_path, 'register').read_data('RegisterCASE')

@ddt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.t = DoExcel(project_path.testcases_path, 'register')
    def tearDown(self):
        pass
    @data(*test_data)  #[{}]这种形式要脱掉一层外套用*号
    def test_cases(self,case):

            method = case['method']
            url = case['url']
            param = eval(case['param'])
            module = case['module']
            id = case['id']
            title = case['title']
            print('正在测试{}模块中的第{}条用例，测试标题是{}'.format(module, id, title))
            resp = HttpRequest().http_request(method, url, param)
            try:
                self.assertEqual(eval(case['ExpectedResult']),resp.json()) #加入断言
                TestResult="Pass"
            except AssertionError as e:
                print('请求用例出错了，错误是:{}'.format(e))
                TestResult="Failed"
            finally:
                '''把实际结果写入到excel表中'''
                self.t.write_data(case['id'] + 1, 8, resp.text)
                self.t.write_data(case['id'] + 1, 9, TestResult)
            print('实际结果是:{}'.format(resp.json()))
