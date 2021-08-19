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

testData = getyaml(setting.TEST_Element_YAML + '/' + 'swz_edit_zhyz.yaml')


class facilityEdit(Page):
    """
    编辑设备页面
    """
    url = '/znyz/admin/page/basedata/mqttDevice.html'

    # 定位器，通过元素属性定位元素对象
    # 编辑按钮
    facilityadd_add_loc = (By.XPATH, testData.get_elementinfo(0))
    # 切换iframe表单
    switch_iframe_addpage_loc = (By.XPATH, testData.get_elementinfo(1))
    # 设备名称输入框
    facilityadd_facilityaname_loc = (By.XPATH, testData.get_elementinfo(2))
    # 设备id输入框
    facilityadd_facilityid_loc = (By.XPATH, testData.get_elementinfo(3))
    # 轨道编号输入框
    facilityadd_trackNo_loc = (By.XPATH, testData.get_elementinfo(4))
    # 轨道类型下拉框
    facilityadd_tracktype_loc = (By.XPATH, testData.get_elementinfo(5))
    # 栏位类型下拉框
    facilityadd_fieldtype_loc = (By.XPATH, testData.get_elementinfo(6))
    # 轨道类型下拉框-选择选项
    facilityadd_trackname_loc = (By.XPATH, testData.get_elementinfo(7))
    # 栏位类型下拉框-选择选项
    facilityadd_fieldname_loc = (By.XPATH, testData.get_elementinfo(8))
    # 保存按钮
    facilityadd_save_loc = (By.XPATH, testData.get_elementinfo(9))
    # 设备管理列表，设备id输入框
    manage_facilityid_loc = (By.XPATH, testData.get_elementinfo(10))
    # 设备管理列表，查询按钮输入框
    manage_search_loc = (By.XPATH, testData.get_elementinfo(11))

    def edit_click(self):
        """
        点击编辑按钮
        """
        self.find_elements(*self.facilityadd_add_loc)[0].click()

    def switch_editpage(self):
        """
        切换iframe-编辑页面
        """
        a = self.find_element(*self.switch_iframe_addpage_loc)
        self.driver.switch_to.frame(a)

    def facilityaname_clear(self):
        """
        编辑页面-清空设备名称
        """
        self.find_element(*self.facilityadd_facilityaname_loc).clear()

    def facilityaname_input(self, facilityaname):
        """
        编辑页面-输入设备名称
        """
        self.find_element(*self.facilityadd_facilityaname_loc).send_keys(facilityaname)

    def facilityid_clear(self):
        """
        编辑页面-清空设备id
        """
        self.find_element(*self.facilityadd_facilityid_loc).clear()

    def facilityid_input(self, facilityid):
        """
        编辑页面-输入设备id
        """
        self.find_element(*self.facilityadd_facilityid_loc).send_keys(facilityid)

    def trackNo_clear(self):
        """
        编辑页面-清空轨道编号
        """
        self.find_element(*self.facilityadd_trackNo_loc).clear()

    def trackNo_input(self, trackNo):
        """
        编辑页面-输入轨道编号
        """
        self.find_element(*self.facilityadd_trackNo_loc).send_keys(trackNo)

    def tracktype_select(self):
        """
        编辑页面-选择轨道类型
        """
        self.find_element(*self.facilityadd_tracktype_loc).click()
        self.find_element(*self.facilityadd_trackname_loc).click()

    def fieldtype_select(self):
        """
        编辑页面-选择栏位类型
        """
        self.find_element(*self.facilityadd_fieldtype_loc).click()
        self.find_element(*self.facilityadd_fieldname_loc).click()

    def save_click(self):
        """
        编辑页面-点击保存按钮
        """
        self.find_element(*self.facilityadd_save_loc).click()

    def manage_facilityid_query(self,query_id):
        """
        设备列表-查询设备id
        """
        self.find_element(*self.manage_facilityid_loc).send_keys(query_id)
        self.find_element(*self.manage_search_loc).click()

    def facilityname_save(self,query_id,facilityname):
        """
        编辑页面-编辑设备名称
        """
        self.manage_facilityid_query(query_id)
        self.edit_click()
        self.switch_editpage()
        time.sleep(1)
        self.facilityaname_clear()
        self.facilityaname_input(facilityname)
        self.save_click()

    def facilityid_save(self,query_id,facilityid):
        """
        编辑页面-编辑设备id名称
        """
        self.manage_facilityid_query(query_id)
        self.edit_click()
        self.switch_editpage()
        self.facilityid_clear()
        time.sleep(1)
        self.facilityid_input(facilityid)
        self.save_click()

    def trackid_save(self,query_id,trackid):
        """
        编辑页面-编辑轨道编号id名称
        """
        self.manage_facilityid_query(query_id)
        self.edit_click()
        self.switch_editpage()
        time.sleep(1)
        self.trackNo_clear()
        self.trackNo_input(trackid)
        self.save_click()

    def tracktype_save(self,query_id):
        """
        编辑页面-编辑轨道类型
        """
        self.manage_facilityid_query(query_id)
        self.edit_click()
        self.switch_editpage()
        time.sleep(1)
        self.tracktype_select()
        self.save_click()

    def fieldtype_save(self,query_id):
        """
        编辑页面-编辑栏位类型
        """
        self.manage_facilityid_query(query_id)
        self.edit_click()
        self.switch_editpage()
        time.sleep(1)
        self.fieldtype_select()
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


