# coding:utf-8
import unittest
import os
from common import HTML_JPG
from common import send_email


if __name__=='__main__':
    path=os.getcwd()
    # 用例路径
    case_path = os.path.join(path, "case")
    # 报告存放路径
    report_path = os.path.join(path, "report")
    # html报告文件
    report_abspath = os.path.join(report_path, "result.html")
    # excel_abspath=os.path.join(report_path, "result.xlsx")
    # print(report_abspath)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)


    fp = open(report_abspath, "wb")
    runner = HTML_JPG.HTMLTestRunner(stream=fp,
                                               title=u'自动化测试报告：',
                                               description=u'用例执行情况：',
                                               verbosity=2,
                                               retry=1)

    # 调用add_case函数返回值
    runner.run(discover)
    fp.close()
    # send_email.send_email(receiver=['gaoxin','gaoxin@begoit.com'],file_path=report_abspath)
