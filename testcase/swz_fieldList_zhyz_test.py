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
from public.page_obj.swzFieldListZhyzPage import fieldList

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'swz_fieldList_zhyz_data.yaml')

log = Log()


class SwzFieldListUI(myunit.MyTest):
    """
    守望者栏位管理页面
    """

    img_path = 'img'

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @BeautifulReport.add_test_img('点击提交按钮前', '点击提交按钮后')
    def test_filld_save(self):
        """
        保存栏位信息，提示配置成功！
        """
        test_case = testData.get_case(0)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = fieldList(self.driver)
        po.open()
        time.sleep(3)
        # 点击提交按钮，提示配置成功！
        self.save_img('点击提交按钮前')
        po.submit_field(query_id)
        # 获取消息框信息
        text = po.alert_text()

        log.info("检查点-> {0}".format(text))
        self.assertEqual(text, test_case['check'][0]), "返回实际结果是->: {0}".format(
            text)
        log.info("返回实际结果是->: {0}".format(text))
        po.alert_accept()

        self.save_img('点击提交按钮后')

    @BeautifulReport.add_test_img('关键词搜索前', '关键词搜索后')
    def test_filld_query(self):
        """
        关键词搜索
        """
        test_case = testData.get_case(1)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']
        keyword = test_case['data']['key_query']

        # 打开配置管理页面
        po = fieldList(self.driver)
        po.open()
        time.sleep(3)
        #关键词搜索
        self.save_img('关键词搜索前')
        po.query_field(query_id,keyword)

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

        self.save_img('关键词搜索后')

    @BeautifulReport.add_test_img('待选择栏位移动到已选择栏位前', '待选择栏位移动到已选择栏位后')
    def test_filld_right_move(self):
        """
        待选择栏位移动到已选择栏位
        """
        test_case = testData.get_case(2)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']


        # 打开配置管理页面
        po = fieldList(self.driver)
        po.open()
        time.sleep(3)
        # 待选择栏位移动到已选择栏位
        self.save_img('待选择栏位移动到已选择栏位前')
        po.move_right_field(query_id)

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

        self.save_img('待选择栏位移动到已选择栏位后')

    @BeautifulReport.add_test_img('已选择栏位移动到待选择栏位前', '已选择栏位移动到待选择栏位后')
    def test_filld_left_move(self):
        """
        已选择栏位移动到待选择栏位
        """
        test_case = testData.get_case(3)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']


        # 打开配置管理页面
        po = fieldList(self.driver)
        po.open()
        time.sleep(3)
        # 已选择栏位移动到待选择栏位
        self.save_img('已选择栏位移动到待选择栏位前')
        po.move_left_field(query_id)

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

        self.save_img('已选择栏位移动到待选择栏位后')

    @BeautifulReport.add_test_img('栏位向上移动前', '栏位向上移动后')
    def test_filld_goon(self):
        """
        栏位向上移动
        """
        test_case = testData.get_case(4)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = fieldList(self.driver)
        po.open()
        time.sleep(3)
        # 栏位向上移动
        self.save_img('栏位向上移动前')
        po.go_on_field(query_id)

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

        self.save_img('栏位向上移动后')

    @BeautifulReport.add_test_img('栏位向下移动前', '栏位向下移动后')
    def test_filld_godown(self):
        """
        栏位向下移动
        """
        test_case = testData.get_case(5)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        query_id = test_case['data']['publlic_facilityid']

        # 打开配置管理页面
        po = fieldList(self.driver)
        po.open()
        time.sleep(3)
        # 栏位向下移动
        self.save_img('栏位向下移动前')
        po.go_down_field(query_id)

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

        self.save_img('栏位向下移动后')