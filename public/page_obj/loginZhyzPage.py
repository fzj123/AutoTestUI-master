#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os,sys
import time

from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_Element_YAML + '/' + 'login_zhyz.yaml')

class login(Page):
    """
    用户登录页面
    """
    url = '/znyz/admin/login.html'


    # 定位器，通过元素属性定位元素对象
    #用户名输入框
    login_username_loc = (By.XPATH, testData.get_elementinfo(0))
    #密码输入框
    login_password_loc = (By.XPATH, testData.get_elementinfo(1))
    #选择角色
    login_role_loc = (By.XPATH, testData.get_elementinfo(2))
    #登陆
    login_submit_loc = (By.XPATH, testData.get_elementinfo(3))

    def login_username(self,username):
        """
        输入用户名
        :param password:
        :return:
        """
        self.find_element(*self.login_username_loc).send_keys(username)
        

    def login_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_role(self):
        """
        选择角色
        :param password:
        :return:
        """
        s1 = self.find_element(*self.login_role_loc)
        Select(s1).select_by_index(0)

    def login_submit(self):
        """
        登录
        :param password:
        :return:
        """
        self.find_element(*self.login_submit_loc).click()

    def login_open(self):
        self.open()

    def user_login(self,username,password):
        """
        登录
        :param username:用户名
        :param password:密码
        :return:
        """
        self.open()
        self.login_username(username)
        self.login_password(password)
        time.sleep(1)
        self.login_submit()

    user_login_success_loc = (By.XPATH, testData.get_CheckElementinfo(0))

    # 登录成功加载主页
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc).text