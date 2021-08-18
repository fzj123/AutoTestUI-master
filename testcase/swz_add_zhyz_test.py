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
from public.page_obj.swzAddZhyzPage import facilityAdd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'swz_add_zhyz_data.yaml')

log = Log()


class SwzAddUI(myunit.MyTest):
    """
    添加守望者设备页面
    """

    img_path = 'img'

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @BeautifulReport.add_test_img('添加守望者前', '添加守望者后')
    def test_add_save(self):
        """
        添加守望者设备
        """
        test_case = testData.get_case(0)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('添加守望者前')
        po.facility_save(facility_name,facility_id,Track_number)
        self.save_img('添加守望者后')

        log.info("检查点-> {0}".format(po.alert_text()))
        self.assertEqual(po.alert_text(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.alert_text())
        log.info("返回实际结果是->: {0}".format(po.alert_text()))

    @BeautifulReport.add_test_img('设备id不能输入中文前', '设备id不能输入中文后')
    def test_facilityid_input(self):
        """
        设备id不能输入中文
        """
        test_case = testData.get_case(1)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('设备id不能输入中文前')
        po.facility_save(facility_name,facility_id,Track_number)
        # 获取消息框信息
        text = po.alter_fail()
        self.save_img('设备id不能输入中文后')

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))


    @BeautifulReport.add_test_img('设备名称不能重复前', '设备名称不能重复后')
    def test_facilityname_input(self):
        """
        设备名称不能重复
        """
        test_case = testData.get_case(2)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('设备名称不能重复前')
        po.facility_save(facility_name,facility_id,Track_number)
        self.save_img('设备名称不能重复后')

        log.info("检查点-> {0}".format(po.alert_text()))
        self.assertEqual(po.alert_text(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.alert_text())
        log.info("返回实际结果是->: {0}".format(po.alert_text()))

    @BeautifulReport.add_test_img('设备id不能重复前', '设备id不能重复后')
    def test_id_input(self):
        """
        设备名称不能重复
        """
        test_case = testData.get_case(3)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('设备id不能重复前')
        po.facility_save(facility_name, facility_id, Track_number)
        self.save_img('设备id不能重复后')

        log.info("检查点-> {0}".format(po.alert_text()))
        self.assertEqual(po.alert_text(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.alert_text())
        log.info("返回实际结果是->: {0}".format(po.alert_text()))

    @BeautifulReport.add_test_img('集团名称为空前', '集团名称为空后')
    def test_groupname_input(self):
        """
        集团名称为空，必填项不能为空
        """
        test_case = testData.get_case(4)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('集团名称为空前')
        po.select_input()
        # 获取消息框信息
        text = po.alter_fail()
        self.save_img('集团名称为空后')

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))

    @BeautifulReport.add_test_img('设备名称为空前', '设备名称为空后')
    def test_facilityname_input(self):
        """
        设备名称为空
        """
        test_case = testData.get_case(5)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('设备名称为空前')
        po.facility_save(facility_name, facility_id, Track_number)
        #获取消息框信息
        text = po.alter_fail()
        self.save_img('设备名称为空后')

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))

    @BeautifulReport.add_test_img('设备id为空前', '设备id为空后')
    def test_facilityid_input(self):
        """
        设备名称为空
        """
        test_case = testData.get_case(6)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('设备id为空前')
        po.facility_save(facility_name, facility_id, Track_number)
        # 获取消息框信息
        text = po.alter_fail()
        self.save_img('设备id为空后')

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))

    @BeautifulReport.add_test_img('轨道编号为空前', '轨道编号为空后')
    def test_trackid_input(self):
        """
        轨道编号为空
        """
        test_case = testData.get_case(7)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        facility_id = test_case['data']['facility_id']
        Track_number = test_case['data']['Track_number']

        # 打开配置管理页面
        po = facilityAdd(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('轨道编号为空前')
        po.facility_save(facility_name, facility_id, Track_number)
        # 获取消息框信息
        text = po.alter_fail()
        self.save_img('轨道编号为空后')

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))




