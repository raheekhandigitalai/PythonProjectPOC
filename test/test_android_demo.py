import unittest
from test import base_test
from appium import webdriver


class AndroidDemoTest(base_test.BaseTest):

    testName = 'Android Native Demo'
    driver = None

    def setUp(self):
        super().setUp()
        self.dc['testName'] = self.testName
        self.dc['appPackage'] = 'com.experitest.ExperiBank'
        self.dc['appActivity'] = '.LoginActivity'
        self.dc['platformName'] = 'android'
        self.dc['deviceQuery'] = "@os='android' and @category='PHONE'"
        self.dc['appiumVersion'] = "1.22.3"
        self.driver = webdriver.Remote(self.getUrl(), self.dc)

    def testQuickStartAndroidNativeDemo(self):
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/usernameTextField").send_keys('company')
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/passwordTextField").send_keys('company')
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/loginButton").click()
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/makePaymentButton").click()
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/phoneTextField").send_keys('1234567')
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/nameTextField").send_keys('Jon Snow')
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/amountTextField").send_keys('50')
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/countryTextField").send_keys('Switzerland')
        self.driver.find_element_by_id("com.experitest.ExperiBank:id/sendPaymentButton").click()
        self.driver.find_element_by_id("android:id/button1").click()

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
