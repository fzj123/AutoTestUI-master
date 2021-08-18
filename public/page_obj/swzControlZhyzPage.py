#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os,sys
from config import setting
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_Element_YAML + '/' + 'swz_control_zhyz.yaml')

class control(Page):
    """
    守望者控制页面
    """
    url = '/znyz/admin/page/basedata/mqttDevice.html'

    # 定位器，通过元素属性定位元素对象
    # 栏位列表按钮按钮
    control_run_loc = (By.XPATH, testData.get_elementinfo(0))
    # 切换iframe表单
    switch_iframe_addpage_loc = (By.XPATH, testData.get_elementinfo(1))
    # 设备管理列表，设备id输入框
    manage_facilityid_loc = (By.XPATH, testData.get_elementinfo(2))
    # 设备管理列表，查询按钮输入框
    manage_search_loc = (By.XPATH, testData.get_elementinfo(3))
    #测重控制按钮
    control_weight_loc = (By.XPATH, testData.get_elementinfo(4))
    #盘点控制按钮
    control_inventory_loc = (By.XPATH, testData.get_elementinfo(5))
    #自动/手动模式按钮
    control_auto_loc = (By.XPATH, testData.get_elementinfo(6))
    # 切换休眠/唤醒状态
    control_sleep_loc = (By.XPATH, testData.get_elementinfo(7))
    #点击前栏
    control_foreward_loc = (By.XPATH, testData.get_elementinfo(8))
    #点击后栏
    control_backward_loc = (By.XPATH, testData.get_elementinfo(9))
    #点击暂停
    control_pause_loc = (By.XPATH, testData.get_elementinfo(10))
    #开启/关闭直播
    control_live_loc = (By.XPATH, testData.get_elementinfo(11))
    #前进
    control_go_loc = (By.XPATH, testData.get_elementinfo(12))
    #后退
    control_back_loc = (By.XPATH, testData.get_elementinfo(13))
    #停止
    control_stop_loc = (By.XPATH, testData.get_elementinfo(14))
    # 自动/手动模式,切换休眠/唤醒,开启/关闭直播,按钮文本获取
    control_text_loc = (By.XPATH, testData.get_elementinfo(15))


    def control_click(self):
        """
        点击栏位列表编辑按钮
        """
        self.find_elements(*self.control_run_loc)[0].click()

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

    def weight_click(self):
        """
        测重控制点击
        """
        self.find_element(*self.control_weight_loc).click()
        

    def inventory_click(self):
        """
        盘点控制点击
        """
        self.find_element(*self.control_inventory_loc).click()

    def auto_click(self):
        """
        点击自动/手动模式按钮
        """
        self.find_elements(*self.control_auto_loc)[0].click()

    def auto_text(self):
        """
        点击自动/手动模式按钮,获取文本
        """
        self.find_elements(*self.control_text_loc)[0].text()

    def sleep_click(self):
        """
        点击休眠状/唤醒态按钮
        """
        self.find_elements(*self.control_sleep_loc)[1].click()

    def sleep_text(self):
        """
        点击休眠状/唤醒态按钮,获取文本
        """
        self.find_elements(*self.control_text_loc)[1].text()

    def foreward_click(self):
        """
        点击前栏
        """
        self.find_element(*self.control_foreward_loc).click()

    def backward_click(self):
        """
        点击后栏
        """
        self.find_element(*self.control_backward_loc).click()

    def pause_click(self):
        """
        点击暂停
        """
        self.find_element(*self.control_pause_loc).click()

    def live_click(self):
        """
        点击开启/关闭直播按钮
        """
        self.find_elements(*self.control_live_loc)[2].click()

    def live_text(self):
        """
        点击开启/关闭直播按钮,获取文本
        """
        self.find_elements(*self.control_text_loc)[2].text()

    def go_click(self):
        """
        前进
        """
        self.find_element(*self.control_go_loc).click()

    def back_click(self):
        """
        后退
        """
        self.find_element(*self.control_back_loc).click()

    def stop_click(self):
        """
        后退
        """
        self.find_element(*self.control_stop_loc).click()


    def manual_switch(self,query_id):
        """
        切换手动模式
        """
        self.manage_facilityid_query(query_id)
        self.control_click()
        self.switch_editpage()

        self.auto_click()



    def alert_text(self):
        str = self.switch_alert().text
        return str

    def alert_accept(self):
        self.switch_alert().accept()

    # 断言条件定位
    alter_success_loc = (By.XPATH, testData.get_CheckElementinfo(0))
    auto_success_loc = (By.XPATH, testData.get_CheckElementinfo(1))

    #必填选项不能为空
    def alter_fail(self):
        s = self.find_element(*self.alter_success_loc).text
        return s

    #切换手动模式成功
    def auto_success(self):
        s = self.find_elements(*self.auto_success_loc)[0]
        return s.text





