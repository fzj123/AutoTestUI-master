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
        # 获取消息框信息
        text = po.alert_text()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(text)
        log.info("返回实际结果是->: {0}".format(text))
        po.alert_accept()

        self.save_img('修改配置保存成功后')

    @BeautifulReport.add_test_img('入仓电量不能小于3000前', '入仓电量不能小于3000后')
    def test_into_Battery(self):
        """
        入仓电量不能小于3000
        """
        test_case = testData.get_case(1)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']
        into_Battery= test_case['data']['into_Battery']

        # 打开配置管理页面
        po = facilityConfig(self.driver)
        po.open()
        time.sleep(3)
        # 入仓电量不能小于3000
        self.save_img('入仓电量不能小于3000前')
        po.into_Battery(query_id,into_Battery)
        # 获取消息框信息
        text = po.alter_fail()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('入仓电量不能小于3000后')


    @BeautifulReport.add_test_img('出仓电量不能小于入仓电量阈值前', '出仓电量不能小于入仓电量阈值后')
    def test_out_Battery(self):
        """
        出仓电量不能小于入仓电量阈值
        """
        test_case = testData.get_case(2)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']
        out_Battery= test_case['data']['out_Battery']

        # 打开配置管理页面
        po = facilityConfig(self.driver)
        po.open()
        time.sleep(3)
        # 出仓电量不能小于入仓电量阈值
        self.save_img('出仓电量不能小于入仓电量阈值前')
        po.out_Battery(query_id,out_Battery)
        # 获取消息框信息
        text = po.alter_fail()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('出仓电量不能小于入仓电量阈值后')

    @BeautifulReport.add_test_img('采集图片不能小于5张前', '采集图片不能小于5张后')
    def test_depth_photo(self):
        """
        采集图片不能小于5张
        """
        test_case = testData.get_case(3)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']
        collect= test_case['data']['collect']

        # 打开配置管理页面
        po = facilityConfig(self.driver)
        po.open()
        time.sleep(3)
        # 采集图片不能小于5张
        self.save_img('采集图片不能小于5张前')
        po.depth_photo(query_id,collect)
        # 获取消息框信息
        text = po.alter_fail()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('采集图片不能小于5张后')


    @BeautifulReport.add_test_img('超出采集时间范围前', '超出采集时间范围后')
    def test_depth_time(self):
        """
        超出采集时间范围（10~3600秒）
        """
        test_case = testData.get_case(4)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']
        interval= test_case['data']['interval']

        # 打开配置管理页面
        po = facilityConfig(self.driver)
        po.open()
        time.sleep(3)
        # 超出采集时间范围（10~3600秒）
        self.save_img('超出采集时间范围前')
        po.depth_time(query_id,interval)
        # 获取消息框信息
        text = po.alter_fail()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('超出采集时间范围后')

    @BeautifulReport.add_test_img('启动时间不能为空前', '启动时间不能为空后')
    def test_clear_time(self):
        """
        启动时间不能为空
        """
        test_case = testData.get_case(4)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityConfig(self.driver)
        po.open()
        time.sleep(3)
        # 启动时间不能为空
        self.save_img('启动时间不能为空前')
        po.clear_time(query_id)
        # 获取消息框信息
        text = po.alert_text()
        po.alert_accept()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('启动时间不能为空后')