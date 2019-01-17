#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/1/2

from appium import webdriver
from time import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = '58284d0a'
desired_caps['appPackage'] = 'com.example.kun.testapplication'
desired_caps['appActivity'] = 'MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
# search_box = driver.find_element_by_id('com.android.dialer:id/search_view')
# search_box.click()
# search_box.send_keys('hello toby')


#  com.UCMobile/com.uc.browser.InnerUCMobile
driver.find_element_by_id('com.example.kun.testapplication:id/button1').click()

driver.quit()
