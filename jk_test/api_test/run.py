import unittest
from jk_test.api_test.tools.HTMLTestRunner import HTMLTestRunner

case = unittest.defaultTestLoader.discover('case','test_*')
report_path = 'report/test_report.html'
title = '接口测试报告'
describ = '接口测试报告'


with open(report_path,'wb') as f:

    html_main = HTMLTestRunner(stream=f,title=title,description=describ)
    html_main.run(case)