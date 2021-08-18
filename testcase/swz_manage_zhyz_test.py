#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'


import os,sys

from BeautifulReport import BeautifulReport
from public.models import myunit
import unittest,time
from config import setting
from public.models.log import Log
from public.page_obj.swzManageZhyzPage import manage
from public.models.GetYaml import getyaml

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'swz_manage_zhyz_data.yaml')




log = Log()

class SwzManageUI(myunit.MyTest):
    """
    守望者设备管理页面
    """

    img_path = 'img'
      
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(setting.IMG_DIR, img_name))

    @BeautifulReport.add_test_img('集团名称查询前','集团名称查询后')
    def test_group_query(self):
        """
        集团名称查询
        """
        test_case = testData.get_case(0)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        #打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #集团名称查询
        self.save_img('集团名称查询前')
        po.group_query()
        time.sleep(3)
        po.query()
        time.sleep(3)
        self.save_img('集团名称查询后')
        time.sleep(3)

        log.info("检查点-> {0}".format(po.group_query_success_hint()))
        self.assertEqual(po.group_query_success_hint(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.group_query_success_hint())
        log.info("返回实际结果是->: {0}".format(po.group_query_success_hint()))

    @BeautifulReport.add_test_img('猪场名称查询前', '猪场名称查询后')
    def test_pig_query(self):
        """
        猪场名称查询
        """
        test_case = testData.get_case(1)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #猪场名称查询
        self.save_img('猪场名称查询前')
        po.pig_query()
        time.sleep(3)
        po.query()
        time.sleep(3)
        self.save_img('猪场名称查询后')
        time.sleep(3)

        log.info("检查点-> {0}".format(po.pig_query_success_hint()))
        self.assertEqual(po.pig_query_success_hint(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.pig_query_success_hint())
        log.info("返回实际结果是->: {0}".format(po.pig_query_success_hint()))

    @BeautifulReport.add_test_img('栋舍名称查询前', '栋舍名称查询后')
    def test_dong_query(self):
        """
        栋舍名称查询
        """
        test_case = testData.get_case(2)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #栋舍名称查询
        self.save_img('栋舍名称查询前')
        po.dong_query()
        time.sleep(3)
        po.query()
        time.sleep(3)
        self.save_img('栋舍名称查询后')
        time.sleep(3)

        log.info("检查点-> {0}".format(po.dong_query_success_hint()))
        self.assertEqual(po.dong_query_success_hint(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.dong_query_success_hint())
        log.info("返回实际结果是->: {0}".format(po.dong_query_success_hint()))

    @BeautifulReport.add_test_img('设备id查询前', '设备id查询后')
    def test_facilityid_query(self):
        """
        输入设备id查询
        """
        test_case = testData.get_case(3)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #设备id查询
        self.save_img('设备id查询前')
        mac_id = test_case['data']['mac_id']
        po.facilityid_query(mac_id)
        time.sleep(3)
        po.query()
        time.sleep(3)
        self.save_img('设备id查询后')
        time.sleep(3)

        log.info("检查点-> {0}".format(po.facilityid_query_success_hint()))
        self.assertEqual(po.facilityid_query_success_hint(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.facilityid_query_success_hint())
        log.info("返回实际结果是->: {0}".format(po.facilityid_query_success_hint()))

    @BeautifulReport.add_test_img('重置查询条件前', '重置查询条件后')
    def test_reset_query(self):
        """
        重置查询条件
        """
        test_case = testData.get_case(4)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #重置查询条件
        po.group_query()
        self.save_img('重置查询条件前')
        po.reset_query()
        time.sleep(3)
        self.save_img('重置查询条件后')
        time.sleep(3)

        log.info("检查点-> {0}".format(po.reset_query_success_hint()))
        self.assertEqual(po.reset_query_success_hint(), test_case['check'][0]), "返回实际结果是->: {0}".format(
            po.reset_query_success_hint())
        log.info("返回实际结果是->: {0}".format(po.reset_query_success_hint()))

    @BeautifulReport.add_test_img('添加守望者前', '添加守望者后')
    def test_add_swz(self):
        """
        添加守望者，断言-查看截图
        """
        test_case = testData.get_case(5)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #添加守望者
        self.save_img('添加守望者前')
        po.add_swz()
        time.sleep(3)
        self.save_img('添加守望者后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('下载导入模板前', '下载导入模板后')
    def test_download_swz(self):
        """
        下载导入模板，断言-查看截图
        """
        test_case = testData.get_case(6)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #下载导入模板
        self.save_img('下载导入模板前')
        po.download_swz()
        time.sleep(3)
        self.save_img('下载导入模板后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('导入模板前', '导入模板后')
    def test_import_swz(self):
        """
        导入模板，断言-查看截图
        """
        test_case = testData.get_case(7)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #导入模板
        self.save_img('导入模板前')
        po.import_swz()
        time.sleep(3)
        self.save_img('导入模板后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击控制按钮前', '点击控制按钮后')
    def test_control_swz(self):
        """
        点击控制按钮，断言-查看截图
        """
        test_case = testData.get_case(8)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        #点击控制按钮
        self.save_img('点击控制按钮前')
        po.control_swz()
        time.sleep(3)
        self.save_img('点击控制按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击编辑按钮前', '点击编辑按钮后')
    def test_edit_swz(self):
        """
        点击编辑按钮，断言-查看截图
        """
        test_case = testData.get_case(9)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击编辑按钮
        self.save_img('点击编辑按钮前')
        po.edit_swz()
        time.sleep(3)
        self.save_img('点击编辑按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击配置管理按钮前', '点击配置管理按钮后')
    def test_conf_swz(self):
        """
        点击配置管理按钮，断言-查看截图
        """
        test_case = testData.get_case(10)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击配置管理按钮
        self.save_img('点击配置管理按钮前')
        po.conf_swz()
        time.sleep(3)
        self.save_img('点击配置管理按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击栏位管理按钮前', '点击栏位管理按钮后')
    def test_fieldList_swz(self):
        """
        点击栏位管理按钮，断言-查看截图
        """
        test_case = testData.get_case(11)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击栏位管理按钮
        self.save_img('点击栏位管理按钮前')
        po.fieldList_swz()
        time.sleep(3)
        self.save_img('点击栏位管理按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击OTA升级按钮前', '点击OTA升级按钮后')
    def test_linuxota_swz(self):
        """
        点击OTA升级按钮，断言-查看截图
        """
        test_case = testData.get_case(12)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击OTA升级按钮
        self.save_img('点击OTA升级按钮前')
        po.linuxota_swz()
        time.sleep(3)
        self.save_img('点击OTA升级按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击故障历史按钮前', '点击故障历史按钮后')
    def test_faultList_swz(self):
        """
        点击故障历史按钮，断言-查看截图
        """
        test_case = testData.get_case(13)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击故障历史按钮
        self.save_img('点击故障历史按钮前')
        po.faultList_swz()
        time.sleep(3)
        self.save_img('点击故障历史按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击故障报警按钮前', '点击故障报警按钮后')
    def test_fault_swz(self):
        """
        点击故障报警按钮，断言-查看截图
        """
        test_case = testData.get_case(14)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击故障报警按钮
        self.save_img('点击故障报警按钮前')
        po.fault_swz()
        time.sleep(3)
        self.save_img('点击故障报警按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

    @BeautifulReport.add_test_img('点击分布式测重按钮前', '点击分布式测重按钮后')
    def test_outFactory_swz(self):
        """
        点击分布式测重按钮，断言-查看截图
        """
        test_case = testData.get_case(15)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(test_case['id'], test_case['detail']))

        # 打开配置管理页面
        po = manage(self.driver)
        po.open()
        time.sleep(3)
        # 点击分布式测重按钮
        self.save_img('点击分布式测重按钮前')
        po.outFactory_swz()
        time.sleep(3)
        self.save_img('点击分布式测重按钮后')

        log.info("检查点-> {0}".format('查看截图'))
        log.info("显示截图结果".format(test_case['check'][0]))

if __name__ =="__main__":
    unittest.main()   