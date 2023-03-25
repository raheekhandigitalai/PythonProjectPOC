import unittest
from appium import webdriver

from test import base_test


class IosDemoTest(base_test.BaseTest):

    testName = 'iOS NATIVE Demo'
    driver = None

    def setUp(self):
        super().setUp()
        self.dc['testName'] = self.testName
        self.dc['app'] = 'cloud:com.experitest.ExperiBank'
        self.dc['bundleId'] = 'com.experitest.ExperiBank'
        self.dc['platformName'] = 'ios'
        self.dc['deviceQuery'] = "@os='ios' and @category='PHONE'"
        self.dc['appiumVersion'] = "1.22.3"
        self.driver = webdriver.Remote(self.getUrl(), self.dc)

    def testQuickStartIosNativeDemo(self):
        self.driver.find_element_by_xpath("//*[@name='usernameTextField']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@name='passwordTextField']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@name='loginButton']").click()
        self.driver.find_element_by_xpath("//*[@name='makePaymentButton']").click()
        self.driver.find_element_by_xpath("//*[@name='phoneTextField']").send_keys('1234567')
        self.driver.find_element_by_xpath("//*[@name='nameTextField']").send_keys('Jon Snow')
        self.driver.find_element_by_xpath("//*[@name='amountTextField']").send_keys('50')
        self.driver.find_element_by_xpath("//*[@name='countryButton']").click()
        self.driver.find_element_by_xpath("//*[@name='Switzerland']").click()
        self.driver.find_element_by_xpath("//*[@name='sendPaymentButton']").click()
        self.driver.find_element_by_xpath("//*[@name='Yes']").click()

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
