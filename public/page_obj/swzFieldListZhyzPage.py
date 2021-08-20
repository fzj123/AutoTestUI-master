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

testData = getyaml(setting.TEST_Element_YAML + '/' + 'swz_fieldList_zhyz.yaml')


class fieldList(Page):
    """
    编辑设备页面
    """
    url = '/znyz/admin/page/basedata/mqttDevice.html'

    # 定位器，通过元素属性定位元素对象
    # 栏位列表按钮按钮
    fieldList_edit_loc = (By.XPATH, testData.get_elementinfo(0))
    # 切换iframe表单
    switch_iframe_addpage_loc = (By.XPATH, testData.get_elementinfo(1))
    # 设备管理列表，设备id输入框
    manage_facilityid_loc = (By.XPATH, testData.get_elementinfo(2))
    # 设备管理列表，查询按钮输入框
    manage_search_loc = (By.XPATH, testData.get_elementinfo(3))
    # 关键字检索输入框查询
    fieldList_keyword_loc = (By.XPATH, testData.get_elementinfo(4))
    # 待选择栏位复选框选择
    fieldList_field_wait_loc = (By.XPATH, testData.get_elementinfo(5))
    # 已选择栏位复选框选择
    fieldList_field_select_loc = (By.XPATH, testData.get_elementinfo(6))
    # 向右侧移动按钮
    fieldList_go_right_loc = (By.XPATH, testData.get_elementinfo(7))
    # 向左侧移动按钮
    fieldList_go_left_loc = (By.XPATH, testData.get_elementinfo(8))
    # 向上移动按钮
    fieldList_go_on_loc = (By.XPATH, testData.get_elementinfo(9))
    # 向下移动按钮
    fieldList_go_down_loc = (By.XPATH, testData.get_elementinfo(10))
    # 保存按钮
    fieldList_submit_loc = (By.XPATH, testData.get_elementinfo(11))
    # 选择栏位
    fieldList_select_loc = (By.XPATH, testData.get_elementinfo(12))

    def fieldList_click(self):
        """
        点击栏位列表编辑按钮
        """
        self.find_elements(*self.fieldList_edit_loc)[0].click()

    def switch_editpage(self):
        """
        切换iframe-编辑页面
        """
        a = self.find_element(*self.switch_iframe_addpage_loc)
        self.driver.switch_to.frame(a)

    def manage_facilityid_query(self,query_id):
        """
        设备列表-查询设备id
        """
        self.find_element(*self.manage_facilityid_loc).send_keys(query_id)
        self.find_element(*self.manage_search_loc).click()

    def keyword_input(self,keyword):
        """
        关键字检索输入框-输入
        """
        self.find_element(*self.fieldList_keyword_loc).send_keys(keyword)

    def field_wait_select(self):
        """
        待选择栏位复选框-点击
        """
        self.find_element(*self.fieldList_field_wait_loc).click()

    def field_select_select(self):
        """
        已选择栏位复选框-点击
        """
        self.find_element(*self.fieldList_field_select_loc).click()

    def go_right_click(self):
        """
        向右侧移动按钮-点击
        """
        self.find_element(*self.fieldList_go_right_loc).click()

    def go_left_click(self):
        """
        向左侧移动按钮-点击
        """
        self.find_element(*self.fieldList_go_left_loc).click()

    def go_on_click(self):
        """
        向上移动按钮-点击
        """
        self.find_element(*self.fieldList_go_on_loc).click()

    def go_down_click(self):
        """
        向下移动按钮-点击
        """
        self.find_element(*self.fieldList_go_down_loc).click()

    def submit_click(self):
        """
        提交按钮-点击
        """
        self.find_element(*self.fieldList_submit_loc).click()

    def select_field(self):
        """
        选择栏位
        """
        self.find_elements(*self.fieldList_select_loc)[3].click()


    def submit_field(self,query_id):
        """
        提交栏位信息
        """
        self.manage_facilityid_query(query_id)
        self.fieldList_click()
        self.switch_editpage()
        self.submit_click()

    def query_field(self,query_id,keyword):
        """
        待选择栏位检索
        """
        self.manage_facilityid_query(query_id)
        self.fieldList_click()
        self.switch_editpage()
        self.keyword_input(keyword)


    def move_right_field(self,query_id):
        """
        向右侧移动栏位信息
        """
        self.manage_facilityid_query(query_id)
        self.fieldList_click()
        self.switch_editpage()
        time.sleep(1)
        self.field_wait_select()
        self.go_right_click()

    def move_left_field(self,query_id):
        """
        向左侧移动栏位信息
        """
        self.manage_facilityid_query(query_id)
        self.fieldList_click()
        self.switch_editpage()
        time.sleep(1)
        self.field_wait_select()
        self.go_right_click()
        time.sleep(1)
        self.field_select_select()
        self.go_left_click()


    def go_on_field(self,query_id):
        """
        栏位向上移动
        """
        self.manage_facilityid_query(query_id)
        self.fieldList_click()
        self.switch_editpage()
        time.sleep(1)
        self.field_wait_select()
        self.go_right_click()
        time.sleep(1)
        self.select_field()
        self.go_on_click()

    def go_down_field(self,query_id):
        """
        栏位向下移动
        """
        self.manage_facilityid_query(query_id)
        self.fieldList_click()
        self.switch_editpage()
        time.sleep(1)
        self.field_wait_select()
        self.go_right_click()
        time.sleep(1)
        self.select_field()
        self.go_down_click()


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


