import unittest
import configparser
import urllib.parse


class BaseTest(unittest.TestCase):

    dc = {}

    config = configparser.ConfigParser()
    config.read('cloud.properties')

    def setUp(self):
        self.dc['accessKey'] = self.config.get('cloud', 'accessKey')

    def getUrl(self):
        url = self.config.get('cloud', 'url')
        return urllib.parse.urljoin(url, '/wd/hub')


if __name__ == '__main__':
    unittest.main()