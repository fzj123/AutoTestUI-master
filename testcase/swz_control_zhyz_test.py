#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os, sys

from BeautifulReport import BeautifulReport
from public.models import myunit
import unittest, time
from config import setting
from public.models.log import Log
from public.models.GetYaml import getyaml
from public.page_obj.swzControlZhyzPage import control

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'swz_control_zhyz_data.yaml')

log = Log()


class SwzControlUI(myunit.MyTest):
    """
    守望者控制页面
    """

    img_path = 'img'

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @BeautifulReport.add_test_img('切换手动模式前', '切换手动模式后')
    def test_manual_switch(self):
        """
        切换手动模式
        """
        test_case = testData.get_case(0)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']


        # 打开配置管理页面
        po = control(self.driver)
        po.open()
        time.sleep(3)
        # 点击提交按钮，提示配置成功！
        self.save_img('点击提交按钮前')
        po.manual_switch(query_id)
        # 获取消息框信息
        text = po.alert_text()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        po.alert_accept()
        self.save_img('点击提交按钮后')
