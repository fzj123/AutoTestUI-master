#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os, sys
import time

from config import setting
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from public.models.GetYaml import getyaml

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_Element_YAML + '/' + 'swz_manage_zhyz.yaml')


class manage(Page):
    """
    设备管理页面
    """
    url = '/znyz/admin/page/basedata/mqttDevice.html'

    # 定位器，通过元素属性定位元素对象
    # 集团名称下拉框
    manageer_group_loc = (By.XPATH, testData.get_elementinfo(0))
    #猪场名称下拉框
    manageer_pig_loc = (By.XPATH, testData.get_elementinfo(1))
    #栋舍列表下拉框
    manageer_dong_loc = (By.XPATH, testData.get_elementinfo(2))
    #设备id
    manageer_facilityid_loc = (By.XPATH, testData.get_elementinfo(3))
    #查询按钮
    manageer_query_loc = (By.XPATH, testData.get_elementinfo(4))
    #重置按钮
    manageer_reset_loc = (By.XPATH, testData.get_elementinfo(5))
    #添加按钮
    manageer_add_loc = (By.XPATH, testData.get_elementinfo(6))
    #下载导入模板按钮
    manageer_download_loc = (By.XPATH, testData.get_elementinfo(7))
    #选择文件按钮
    manageer_import_loc = (By.XPATH, testData.get_elementinfo(8))
    #控制按钮
    manageer_control_loc = (By.XPATH, testData.get_elementinfo(9))
    #编辑按钮
    manageer_edit_loc = (By.XPATH, testData.get_elementinfo(10))
    #配置管理按钮
    manageer_conf_loc = (By.XPATH, testData.get_elementinfo(11))
    #栏位列表按钮
    manageer_fieldList_loc = (By.XPATH, testData.get_elementinfo(12))
    #OTA升级按钮
    manageer_linuxota_loc = (By.XPATH, testData.get_elementinfo(13))
    #故障历史按钮
    manageer_faultList_loc = (By.XPATH, testData.get_elementinfo(14))
    #故障报警按钮
    manageer_fault_loc = (By.XPATH, testData.get_elementinfo(15))
    #出厂按钮
    manageer_outFactory_loc = (By.XPATH, testData.get_elementinfo(16))
    #分布式测重按钮
    manageer_workstation_loc = (By.XPATH, testData.get_elementinfo(17))
    #集团名称下拉框-选择选项
    manageer_groupname_loc = (By.XPATH, testData.get_elementinfo(18))
    #猪场名称下拉框-选择选项
    manageer_pigname_loc = (By.XPATH, testData.get_elementinfo(19))
    # 栋舍名称下拉框-选择选项
    manageer_dongname_loc = (By.XPATH, testData.get_elementinfo(20))


    def group_query(self):
        """
        集团名称查询
        """
        self.find_elements(*self.manageer_group_loc)[0].click()
        self.find_element(*self.manageer_groupname_loc).click()

    def pig_query(self):
        """
        猪场名称查询
        """
        self.find_elements(*self.manageer_pig_loc)[1].click()
        self.find_element(*self.manageer_pigname_loc).click()

    def dong_query(self):
        """
        栋舍列表查询
        """
        self.find_elements(*self.manageer_pig_loc)[1].click()
        self.find_element(*self.manageer_pigname_loc).click()
        time.sleep(2)
        self.find_elements(*self.manageer_dong_loc)[2].click()
        self.find_element(*self.manageer_dongname_loc).click()

    def facilityid_query(self, mac_id):
        """
        输入设备id
        """
        self.find_element(*self.manageer_facilityid_loc).send_keys(mac_id)

    def query(self):
        """
        查询
        """
        self.find_element(*self.manageer_query_loc).click()

    def reset_query(self):
        """
        重置查询条件
        """
        self.find_element(*self.manageer_reset_loc).click()

    def add_swz(self):
        """
        重置查询条件
        """
        self.find_element(*self.manageer_add_loc).click()

    def download_swz(self):
        """
        下载导入模板
        """
        self.find_element(*self.manageer_download_loc).click()

    def import_swz(self):
        """
        导入模板
        """
        self.find_element(*self.manageer_import_loc).click()

    def control_swz(self):
        """
        控制
        """
        self.find_elements(*self.manageer_control_loc)[0].click()

    def edit_swz(self):
        """
        编辑
        """
        self.find_elements(*self.manageer_edit_loc)[0].click()

    def conf_swz(self):
        """
        配置管理
        """
        self.find_elements(*self.manageer_conf_loc)[0].click()

    def fieldList_swz(self):
        """
        栏位列表
        """
        self.find_elements(*self.manageer_fieldList_loc)[0].click()

    def linuxota_swz(self):
        """
        栏位列表
        """
        self.find_elements(*self.manageer_linuxota_loc)[0].click()

    def faultList_swz(self):
        """
        故障历史
        """
        self.find_elements(*self.manageer_faultList_loc)[0].click()

    def fault_swz(self):
        """
        故障报警
        """
        self.find_elements(*self.manageer_fault_loc)[0].click()

    def outFactory_swz(self):
        """
        分布式测重
        """
        self.find_elements(*self.manageer_workstation_loc)[0].click()


    #断言条件定位
    group_query_success_loc = (By.XPATH, testData.get_CheckElementinfo(0))
    pig_query_success_loc = (By.XPATH, testData.get_CheckElementinfo(1))
    dong_query_success_loc = (By.XPATH, testData.get_CheckElementinfo(2))
    facilityid_query_success_loc = (By.XPATH, testData.get_CheckElementinfo(3))
    reset_query_success_loc = (By.XPATH, testData.get_CheckElementinfo(4))

    #集团名称查询成功
    def group_query_success_hint(self):
        return self.find_elements(*self.group_query_success_loc)[1].text

    # 猪场名称查询成功
    def pig_query_success_hint(self):
        return self.find_elements(*self.pig_query_success_loc)[1].text

    # 栋舍名称查询成功
    def dong_query_success_hint(self):
        return self.find_elements(*self.dong_query_success_loc)[1].text

    # 设备id查询成功
    def facilityid_query_success_hint(self):
        return self.find_elements(*self.facilityid_query_success_loc)[1].text

    # 集团检索条件清空成功
    def reset_query_success_hint(self):
        return self.find_element(*self.reset_query_success_loc).get_attribute('placeholder')




