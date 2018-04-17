# -*- coding: utf-8 -*-
# @Author  : leizi
from  case.example_test_api import Test_api
import  unittest,time,os
from common import  BSTestRunner
from common import send_email
if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_api))
    now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'report')
    file = os.path.join(file_dir, (now + '.html'))
    re_open = open(file, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试结果')
    m=runner.run(suite)
    send_email.send_email(receiver=['gaoxin', 'gaoxin@begoit.com'], file_path=file)