#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'

import os, sys
import time

from selenium.webdriver.common.keys import Keys

from config import setting
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from public.models.GetYaml import getyaml
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_Element_YAML + '/' + 'swz_config_zhyz.yaml')


class facilityConfig(Page):
    """
    编辑设备页面
    """
    url = '/znyz/admin/page/basedata/mqttDevice.html'

    # 定位器，通过元素属性定位元素对象
    # 编辑按钮
    facilityadd_add_loc = (By.XPATH, testData.get_elementinfo(0))
    # 切换iframe表单
    switch_iframe_addpage_loc = (By.XPATH, testData.get_elementinfo(1))
    # 设备管理列表，设备id输入框
    manage_facilityid_loc = (By.XPATH, testData.get_elementinfo(2))
    # 设备管理列表，查询按钮输入框
    manage_search_loc = (By.XPATH, testData.get_elementinfo(3))
    # 复查按钮
    facilityconfig_review_loc = (By.XPATH, testData.get_elementinfo(4))
    # 入仓电量输入框
    facilityconfig_into_Battery_loc = (By.XPATH, testData.get_elementinfo(5))
    # 出仓电量输入框
    facilityconfig_out_Battery_loc = (By.XPATH, testData.get_elementinfo(6))
    # 测重按钮
    facilityconfig_depth_loc = (By.XPATH, testData.get_elementinfo(7))
    # 采集图片张数输入框
    facilityconfig_depthphoto_loc = (By.XPATH, testData.get_elementinfo(8))
    # 采集时间输入框
    facilityconfig_depthtime_loc = (By.XPATH, testData.get_elementinfo(9))
    # 大猪盘点按钮
    facilityconfig_bigpig_loc = (By.XPATH, testData.get_elementinfo(10))
    # 小猪盘点按钮
    facilityconfig_smallpig_loc = (By.XPATH, testData.get_elementinfo(11))
    # 盘点图片张数输入框
    facilityconfig_inventoryphoto_loc = (By.XPATH, testData.get_elementinfo(12))
    # 盘点间隔输入框
    facilityconfig_inventorytime_loc = (By.XPATH, testData.get_elementinfo(13))
    # 添加时间按钮
    facilityconfig_addtime_loc = (By.XPATH, testData.get_elementinfo(14))
    # 时间画布
    facilityconfig_canvas_loc = (By.XPATH, testData.get_elementinfo(15))
    # 清空按钮
    facilityconfig_clearbtn_loc = (By.XPATH, testData.get_elementinfo(16))
    # 清空按钮
    facilityconfig_savebtn_loc = (By.XPATH, testData.get_elementinfo(17))

    def config_click(self):
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

    def manage_facilityid_query(self,query_id):
        """
        设备列表-查询设备id
        """
        self.find_element(*self.manage_facilityid_loc).send_keys(query_id)
        self.find_element(*self.manage_search_loc).click()

    def review_input(self,review):
        """
        复位按钮输入框-输入
        """
        self.find_element(*self.facilityconfig_review_loc).send_keys(review)

    def review_clear(self):
        """
        复位按钮输入框-清空
        """
        self.find_element(*self.facilityconfig_review_loc).clear()

    def into_Battery_input(self,into):
        """
        入仓电量输入框-输入
        """
        self.find_element(*self.facilityconfig_into_Battery_loc).send_keys(into)

    def into_Battery_clear(self):
        """
        入仓电量输入框-清空
        """
        element = self.find_element(*self.facilityconfig_into_Battery_loc)
        element.send_keys(Keys.CONTROL, 'a')


    def out_Battery_input(self,out):
        """
        出仓电量输入框-输入
        """
        self.find_element(*self.facilityconfig_out_Battery_loc).send_keys(out)

    def out_Battery_clear(self):
        """
        出仓电量输入框-清空
        """
        element = self.find_element(*self.facilityconfig_out_Battery_loc)
        element.send_keys(Keys.CONTROL, 'a')

    def depth_click(self):
        """
        测重按钮-点击
        """
        self.find_element(*self.facilityconfig_depth_loc).click()

    def depth_select(self):
        """
        测重按钮-按钮是否被选择
        """
        return self.find_element(*self.facilityconfig_depth_loc).is_selected()

    def depthphoto_input(self,depthphoto):
        """
        采集图片张数输入框-输入
        """
        self.find_element(*self.facilityconfig_depthphoto_loc).send_keys(depthphoto)

    def depthphoto_clear(self):
        """
        采集图片张数输入框-清空
        """
        element = self.find_element(*self.facilityconfig_depthphoto_loc)
        element.send_keys(Keys.CONTROL, 'a')

    def depthtime_input(self,depthtime):
        """
        采集时间输入框-输入
        """
        self.find_element(*self.facilityconfig_depthtime_loc).send_keys(depthtime)

    def depthtime_clear(self):
        """
        采集时间输入框-清空
        """
        element = self.find_element(*self.facilityconfig_depthtime_loc)
        element.send_keys(Keys.CONTROL, 'a')


    def bigpig_click(self):
        """
        大猪盘点按钮-点击
        """
        self.find_element(*self.facilityconfig_bigpig_loc).click()

    def smallpig_click(self):
        """
        小猪盘点按钮-点击
        """
        self.find_element(*self.facilityconfig_smallpig_loc).click()

    def inventoryphoto_input(self,inventoryphoto):
        """
        盘点图片张数输入框-输入
        """
        self.find_element(*self.facilityconfig_inventoryphoto_loc).send_keys(inventoryphoto)

    def inventoryphoto_clear(self):
        """
        盘点图片张数输入框-清空
        """
        element = self.find_element(*self.facilityconfig_inventoryphoto_loc)
        element.send_keys(Keys.CONTROL, 'a')

    def inventorytime_click(self,inventorytime):
        """
        盘点间隔输入框-输入
        """
        self.find_element(*self.facilityconfig_inventorytime_loc).send_keys(inventorytime)

    def inventorytime_clear(self):
        """
        盘点间隔输入框-清空
        """
        element = self.find_element(*self.facilityconfig_inventorytime_loc)
        element.send_keys(Keys.CONTROL, 'a')

    def addtime_click(self):
        """
        添加时间按钮-点击
        """
        self.find_element(*self.facilityconfig_addtime_loc).click()

    def canvas_click(self):
        canvas = self.find_element(*self.facilityconfig_canvas_loc)
        ActionChains(self.driver).move_to_element_with_offset(canvas, 90, 1).click().perform()
        ActionChains(self.driver).move_to_element_with_offset(canvas, 90, 1).click().perform()

    def clearbtn_click(self):
        """
        清空按钮-点击
        """
        self.find_element(*self.facilityconfig_clearbtn_loc).click()

    def savebtn_click(self):
        """
        保存按钮-点击
        """
        self.find_element(*self.facilityconfig_savebtn_loc).click()



    def config_save(self,query_id,review_number,into_Battery,out_Battery,collect,interval):
        """
        修改配置信息，点击保存
        """
        self.manage_facilityid_query(query_id)
        self.config_click()
        self.switch_editpage()
        self.review_clear()
        self.review_input(review_number)
        time.sleep(2)
        self.into_Battery_clear()
        self.into_Battery_input(into_Battery)
        time.sleep(2)
        self.out_Battery_clear()
        self.out_Battery_input(out_Battery)
        #判断单选框是否选中
        depth = self.depth_select()
        if depth:
            self.depth_click()
            self.depthphoto_clear()
            self.depthphoto_input(collect)
            self.depthtime_clear()
            self.depthtime_input(interval)

        #滚动条，拉到最下面
        self.driver.execute_script('var q=document.body.scrollTop=10000')
        self.addtime_click()
        self.canvas_click()
        self.savebtn_click()







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


