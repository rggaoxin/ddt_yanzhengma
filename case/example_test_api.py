# coding:utf-8
import unittest
import ddt
import os
import requests
from common import base_api
from common import readexcel
from common import writeexcel

# 获取demo_api.xlsx路径
# path=os.getcwd()
# abspath=os.path.dirname(path)
#excelPath=path+"\\data\\testdata.xlsx"
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path=os.path.join(curpath,'data')
testxlsx = os.path.join(data_path, "demo_api.xlsx")

# 复制demo_api.xlsx文件到report下
report_path = os.path.join(curpath, "report")
reportxlsx = os.path.join(report_path, "demo_api_result.xlsx")

testdata = readexcel.ExcelUtil(testxlsx).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("ceshi")
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了
        writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = base_api.send_requests(self.s, data)

        base_api.wirte_result(res, filename=reportxlsx)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s" % check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s" % res_text)
        # 断言
        self.assertTrue(check in res_text)


if __name__ == "__main__":
    unittest.main()