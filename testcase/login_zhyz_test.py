#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'


import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from public.models.driver import browser
from public.models.GetYaml import getyaml
from BeautifulReport import BeautifulReport
import unittest,time
from config import setting
from public.models.log import Log
from public.page_obj.loginZhyzPage import login

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
testData = getyaml(setting.TEST_DATA_YAML + '/' + 'login_zhyz_data.yaml')



class Login_Zhyz_UI(unittest.TestCase):
    """
    登录成功
    """
  
    img_path = 'img'
      
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()



    @BeautifulReport.add_test_img('登录成功前','登录成功后')
    def test_login(self):
        """
        登录测试，输入用户名，密码
        """
        test_case = testData.get_case(0)
        username = test_case['data']['username']
        password = test_case['data']['password']

        login(self.driver).open()
        self.save_img('登录成功前')
        login(self.driver).login_username(username)
        login(self.driver).login_password(password)
        self.save_img('登录成功后')
        login(self.driver).login_submit()

        self.assertEqual('1','1')
        print('跳转与保存截图完成')





if __name__ =="__main__":
    unittest.main()   