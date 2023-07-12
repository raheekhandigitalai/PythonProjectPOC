import unittest
import configparser
import urllib.parse


class BaseTest(unittest.TestCase):

    config = configparser.ConfigParser()
    config.read('cloud.properties')

    def setUp(self):
        self.options.set_capability('accessKey', self.config.get('cloud', 'accessKey'))

    def getUrl(self):
        url = self.config.get('cloud', 'url')
        return urllib.parse.urljoin(url, '/wd/hub')


if __name__ == '__main__':
    unittest.main()