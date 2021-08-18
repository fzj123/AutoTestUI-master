#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time

from public.models.newReport import new_report
from public.models.sendmail import send_mail
from BeautifulReport import BeautifulReport

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
#if not os.path.exists(setting.TEST_REPORT):os.makedirs(setting.TEST_REPORT + '/' + "screenshot")


def add_case(test_path=setting.TEST_DIR):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*_test.py')

    return discover


def run_case(all_case, result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + 'result.html'

    result = BeautifulReport(all_case)
    result.report(filename=filename, description='测试deafult报告',
                  log_path=result_path)


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
