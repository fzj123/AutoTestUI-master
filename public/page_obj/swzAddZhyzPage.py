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

testData = getyaml(setting.TEST_Element_YAML + '/' + 'swz_add_zhyz.yaml')


class facilityAdd(Page):
    """
    添加设备页面
    """
    url = '/znyz/admin/page/basedata/mqttDevice.html'

    # 定位器，通过元素属性定位元素对象
    # 添加按钮
    facilityadd_add_loc = (By.XPATH, testData.get_elementinfo(0))
    # 切换iframe表单
    switch_iframe_addpage_loc = (By.XPATH, testData.get_elementinfo(1))
    # 集团名称下拉框
    facilityadd_group_loc = (By.XPATH, testData.get_elementinfo(2))
    # 猪场名称下拉框
    facilityadd_pig_loc = (By.XPATH, testData.get_elementinfo(3))
    # 栋舍列表下拉框
    facilityadd_dong_loc = (By.XPATH, testData.get_elementinfo(4))
    # 集团名称下拉框-选择选项
    facilityadd_groupname_loc = (By.XPATH, testData.get_elementinfo(5))
    # 猪场名称下拉框-选择选项
    facilityadd_pigname_loc = (By.XPATH, testData.get_elementinfo(6))
    # 栋舍名称下拉框-选择选项
    facilityadd_dongname_loc = (By.XPATH, testData.get_elementinfo(7))
    # 设备名称输入框
    facilityadd_facilityaname_loc = (By.XPATH, testData.get_elementinfo(8))
    # 设备id输入框
    facilityadd_facilityid_loc = (By.XPATH, testData.get_elementinfo(9))
    # 轨道编号输入框
    facilityadd_trackNo_loc = (By.XPATH, testData.get_elementinfo(10))
    # 轨道类型下拉框
    facilityadd_tracktype_loc = (By.XPATH, testData.get_elementinfo(11))
    # 栏位类型下拉框
    facilityadd_fieldtype_loc = (By.XPATH, testData.get_elementinfo(12))
    # 轨道类型下拉框-选择选项
    facilityadd_trackname_loc = (By.XPATH, testData.get_elementinfo(13))
    # 栏位类型下拉框-选择选项
    facilityadd_fieldname_loc = (By.XPATH, testData.get_elementinfo(14))
    # 保存按钮
    facilityadd_save_loc = (By.XPATH, testData.get_elementinfo(15))

    def add_click(self):
        """
        点击添加按钮
        """
        self.find_element(*self.facilityadd_add_loc).click()

    def switch_addpage(self):
        """
        切换iframe-添加页面
        """
        a = self.find_element(*self.switch_iframe_addpage_loc)
        self.driver.switch_to.frame(a)


    def group_select(self):
        """
        添加页面-选择集团名称
        """
        self.find_elements(*self.facilityadd_group_loc)[0].click()
        self.find_element(*self.facilityadd_groupname_loc).click()

    def pig_select(self):
        """
        添加页面-选择猪场名称
        """
        self.find_elements(*self.facilityadd_pig_loc)[1].click()
        self.find_element(*self.facilityadd_pigname_loc).click()

    def dong_select(self):
        """
        添加页面-选择栋舍名称
        """
        self.find_elements(*self.facilityadd_dong_loc)[2].click()
        self.find_element(*self.facilityadd_dongname_loc).click()

    def facilityaname_input(self, facilityaname):
        """
        添加页面-输入设备名称
        """
        self.find_element(*self.facilityadd_facilityaname_loc).send_keys(facilityaname)

    def facilityid_input(self, facilityid):
        """
        添加页面-输入设备id
        """
        self.find_element(*self.facilityadd_facilityid_loc).send_keys(facilityid)

    def trackNo_input(self, trackNo):
        """
        添加页面-输入轨道编号
        """
        self.find_element(*self.facilityadd_trackNo_loc).send_keys(trackNo)

    def tracktype_select(self):
        """
        添加页面-选择轨道类型
        """
        self.find_element(*self.facilityadd_tracktype_loc).click()
        self.find_element(*self.facilityadd_trackname_loc).click()

    def fieldtype_select(self):
        """
        添加页面-选择栏位类型
        """
        self.find_element(*self.facilityadd_fieldtype_loc).click()
        self.find_element(*self.facilityadd_fieldname_loc).click()

    def save_click(self):
        """
        添加页面-点击保存按钮
        """
        self.find_element(*self.facilityadd_save_loc).click()





    def facility_save(self,facilityaname,facilityid,trackNo):
        """
        添加页面-添加设备
        """
        self.add_click()
        time.sleep(1)
        self.switch_addpage()
        self.group_select()
        time.sleep(1)
        self.pig_select()
        time.sleep(1)
        self.dong_select()
        time.sleep(1)
        self.facilityaname_input(facilityaname)
        self.facilityid_input(facilityid)
        self.trackNo_input(trackNo)
        self.tracktype_select()
        self.fieldtype_select()
        self.script("document.body.style.transform='scale(0.7)'")
        self.save_click()

    def select_input(self):
        """
        添加页面-添加设备
        """
        self.add_click()
        time.sleep(1)
        self.switch_addpage()
        time.sleep(1)
        self.script("document.body.style.transform='scale(0.7)'")
        self.save_click()


    def alert_text(self):
        str = self.switch_alert().text
        return str

    def alert_accept(self):
        self.switch_alert().accept()

    # 断言条件定位
    alter_success_loc = (By.XPATH, testData.get_CheckElementinfo(0))

    #必填选项不能为空
    def alter_fail(self):
        s = self.find_element(*self.alter_success_loc).text
        return s


