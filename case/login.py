import requests
import unittest
import re

class Login(unittest.TestCase):
    def test_login(self,account='admin',pwd='Admin123'):
        self.url="http://120.78.168.211/m4m/action/userAction/adminLogin"
        self.headers={'Content-Type':'application/x-www-form-urlencoded',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        self.data={'account':account,
            'pwd':pwd,
            'captcha':'1111'
        }
        r=requests.session().post(self.url,data=self.data,headers=self.headers)
        # result=r.content.decode('utf-8')
        print(r.content.decode('utf-8'))
        result = re.findall(r"<title> .+?</title>", r.content.decode('utf-8'))   # 实际结果
        # self.assertIn("主页示例",result)
        print(result)

if __name__=="__main__":
    unittest.main()