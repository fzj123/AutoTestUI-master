#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zhyz-test'


import os


def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new


if __name__ =="__main__":
    a= new_report(u'c:/Users/x1t/Desktop/ZhyzUI-master/report')
    print(a)