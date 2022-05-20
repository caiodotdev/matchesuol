from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from django.conf import settings

LOCAL = settings.LOCAL


class EngineModel(object):

    def __init__(self):
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        desired_cap = {
        'os_version': '11',
        'resolution': '1920x1080',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        }
        self.browser = webdriver.Remote(
            command_executor='https://caiodotdev_irwadE:Ke15XkyiQ6qp9XryA26w@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)

    def get_info(self, args, **kwargs):
        pass

    def dispose(self):
        self.browser.close()
        self.browser.quit()