'''
    - -coding= utf-8- -
    @authour=Wangyafei
    @time=2019/3/12 9:46
    @file=homework0219_1.py

'''
import requests
from project1.common.get_data import GetData

class HttpRequest:

    def http_request(self,method,url,param,cookies=None):
        ''''#get,post方法获取响应结果
        method: get post请求方式
        url:接口请求地址
        param:请求参数 字典格式
        rtype: 有响应值，返回响应报文
        cookies:传递cookies参数
        '''
        global COOKIES
        if method.upper()=='GET':
            try:
             resp=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                print("get请求失败，失败原因是{}".format(e))
        elif method.upper()=='POST':
            try:
              resp = requests.post(url, data=param,cookies=cookies)
            except Exception as e:
                print("post请求失败，失败原因是{}".format(e))
        else:
            print('不支持该种方式')
            resp=None
        return resp

#测试代码
if __name__=='__main__':
    method='post'
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    param={"mobilephone":"18813989009","pwd":"123456","regname":"lemonhuahua"}
    resp=HttpRequest().http_request(method,url,param,cookies=None)
    print(resp.text)
    print(resp.status_code)

