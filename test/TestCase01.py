import unittest
import time
from appium import webdriver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['deviceName'] = '127.0.0.1:62001'
        # desired_caps['appPackage'] = 'com.android.dialer'
        # desired_caps['appActivity'] = 'DialtactsActivity'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '58284d0a'
        desired_caps['appPackage'] = 'com.example.kun.testapplication'
        desired_caps['appActivity'] = 'MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testDial(self):
        self.driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
        search_box = self.driver.find_element_by_id('com.android.dialer:id/search_view')
        search_box.click()
        search_box.send_keys('hello toby')
        print("测试完成！")

    def teseDemo(self):
        #  com.UCMobile/com.uc.browser.InnerUCMobile
        self.driver.find_element_by_id('com.example.kun.testapplication:id/button1').click()


    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

myTC = MyTestCase()
myTC.testDemo()