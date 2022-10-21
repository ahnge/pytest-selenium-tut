from django.test import LiveServerTestCase

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class HostTest(LiveServerTestCase):

    def test_homepage(self):
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(chrome_options=option)

        driver.get(self.live_server_url)
        assert "Hello, world!" in driver.title
