#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os
import sys
import time

from config import setting
from .GetYaml import getyaml
from  .driver import browser
import unittest
from public.page_obj.loginZhyzPage import login

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
testData = getyaml(setting.TEST_DATA_YAML + '/' + 'login_zhyz_data.yaml')

class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        #登录
        test_case = testData.get_case(0)
        login(cls.driver).user_login(test_case['data']['username'],test_case['data']['password'])
        cls.driver.implicitly_wait(5)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


