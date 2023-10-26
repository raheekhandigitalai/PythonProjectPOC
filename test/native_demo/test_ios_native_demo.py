import os
from test import base_test
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.common import AppiumOptions


class IosDemoTest(base_test.BaseTest):

    proxyUrl = "http://ip:port"

    testName = 'iOS Native Demo'
    driver = None
    options = AppiumOptions()

    def setUp(self):
        super().setUp()
        self.options.set_capability('testName', self.testName)
        self.options.set_capability('app', 'cloud:com.experitest.ExperiBank')
        self.options.set_capability('bundleId', 'com.experitest.ExperiBank')
        self.options.set_capability('platformName', 'ios')
        self.options.set_capability('udid', "00008020-001659561E78003A")


        # os.environ["HTTP_PROXY"] = self.proxyUrl
        # os.environ["HTTPS_PROXY"] = self.proxyUrl

        self.driver = webdriver.Remote(self.getUrl(), options=self.options)

    def testIosNativeDemo(self):
        self.driver.find_element(By.XPATH, "//*[@name='usernameTextField']").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@name='passwordTextField']").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@name='loginButton']").click()

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities['reportUrl'])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
