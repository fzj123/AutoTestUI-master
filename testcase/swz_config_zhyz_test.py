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
from public.page_obj.swzConfigZhyzPage import facilityConfig

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'swz_config_zhyz_data.yaml')

log = Log()


class SwzConfigUI(myunit.MyTest):
    """
    配置守望者设备页面
    """

    img_path = 'img'

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @BeautifulReport.add_test_img('修改配置保存成功前', '修改配置保存成功后')
    def test_config_save(self):
        """
        修改配置保存成功
        """
        test_case = testData.get_case(0)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']
        review_number= test_case['data']['review_number']
        into_Battery= test_case['data']['into_Battery']
        out_Battery= test_case['data']['out_Battery']
        collect= test_case['data']['collect']
        interval= test_case['data']['interval']

        # 打开配置管理页面
        po = facilityConfig(self.driver)
        po.open()
        time.sleep(3)
        # 修改配置保存成功
        self.save_img('修改配置保存成功前')
        po.config_save(query_id,review_number,into_Battery,out_Battery,collect,interval)
        self.save_img('修改配置保存成功后')

        log.info("检查点-> {0}".format(po.alert_text()))
        self.assertEqual(po.alert_text(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.alert_text())
        log.info("返回实际结果是->: {0}".format(po.alert_text()))



