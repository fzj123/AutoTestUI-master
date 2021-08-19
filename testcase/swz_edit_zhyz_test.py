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
from public.page_obj.swzEditZhyzPage import facilityEdit

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'swz_edit_zhyz_data.yaml')

log = Log()


class SwzEditUI(myunit.MyTest):
    """
    编辑守望者设备页面
    """

    img_path = 'img'

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @BeautifulReport.add_test_img('修改设备名称前', '修改设备名称后')
    def test_edit_facilityname_save(self):
        """
        编辑守望者设备名称
        """
        test_case = testData.get_case(0)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 修改设备名称
        self.save_img('修改设备名称前')
        po.facilityname_save(query_id,facility_name)
        # 获取消息框信息
        text = po.alert_text()
        po.alert_accept()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('修改设备名称后')


    @BeautifulReport.add_test_img('修改设备id保存前', '修改设备保存id后')
    def test_edit_facilityid_save(self):
        """
        修改设备id,保存
        """
        test_case = testData.get_case(1)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_id = test_case['data']['facility_id']
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('修改设备id保存前')
        po.facilityid_save(query_id,facility_id)
        # 获取消息框信息
        text = po.alert_text()
        po.alert_accept()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('修改设备保存id后')


    @BeautifulReport.add_test_img('修改轨道编号前', '修改轨道编号后')
    def test_edit_trackid_save(self):
        """
        修改轨道编号,保存
        """
        test_case = testData.get_case(2)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        Track_number = test_case['data']['Track_number']
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('修改轨道编号前')
        po.trackid_save(query_id,Track_number)

        # 获取消息框信息
        text = po.alert_text()
        po.alert_accept()
        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        self.save_img('修改轨道编号后')

    @BeautifulReport.add_test_img('修改轨道类型前', '修改轨道类型后')
    def test_edit_tracktype_save(self):
        """
        修改轨道类型，保存
        """
        test_case = testData.get_case(3)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 修改轨道类型
        self.save_img('修改轨道类型前')
        po.tracktype_save(query_id)

        # 获取消息框信息
        text = po.alert_text()
        po.alert_accept()
        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        self.save_img('修改轨道类型后')

    @BeautifulReport.add_test_img('修改栏位类型前', '修改栏位类型后')
    def test_edit_fieldtype_save(self):
        """
        修改栏位类型，保存
        """
        test_case = testData.get_case(4)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 修改栏位类型
        self.save_img('修改栏位类型前')
        po.fieldtype_save(query_id)

        # 获取消息框信息
        text = po.alert_text()
        po.alert_accept()
        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        self.save_img('修改栏位类型后')


    @BeautifulReport.add_test_img('设备id输入中文前', '设备id输入中文后')
    def test_facilityid_input(self):
        """
        设备id输入中文
        """
        test_case = testData.get_case(5)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_id = test_case['data']['facility_id']
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 设备id输入中文
        self.save_img('设备id输入中文前')
        po.facilityid_save(query_id,facility_id)
        #获取消息框信息
        text = po.alter_fail()
        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))

        self.save_img('设备id输入中文后')

    @BeautifulReport.add_test_img('设备名称为空前', '设备名称为空后')
    def test_facilityid_input(self):
        """
        设备名称为空
        """
        test_case = testData.get_case(6)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        facility_name = test_case['data']['facility_name']
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 添加守望者配置
        self.save_img('设备名称为空前')
        po.facilityname_save(query_id,facility_name)
        # 获取消息框信息
        text = po.alter_fail()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        self.save_img('设备名称为空后')

    @BeautifulReport.add_test_img('轨道编号为空前', '轨道编号为空后')
    def test_trackid_input(self):
        """
        轨道编号为空
        """
        test_case = testData.get_case(7)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        Track_number = test_case['data']['Track_number']
        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = facilityEdit(self.driver)
        po.open()
        time.sleep(3)
        # 轨道编号为空
        self.save_img('轨道编号为空前')
        po.trackid_save(query_id,Track_number)
        # 获取消息框信息
        text = po.alter_fail()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        self.save_img('轨道编号为空后')




