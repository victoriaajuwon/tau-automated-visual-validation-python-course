from unittest import TestCase

from applitools.selenium import Eyes
from selenium import webdriver

from config.base import APPLITOOLS_API_KEYS


class BaseTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.initialize_eyes()
        self.driver.get('https://applitools.com/helloworld')

    def tearDown(self):
        self.driver.quit()

    def initialize_eyes(self):
        self.eyes = Eyes()
        self.eyes.api_key = APPLITOOLS_API_KEYS