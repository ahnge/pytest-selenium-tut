from django.test import LiveServerTestCase

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class HostTest(LiveServerTestCase):

    def test_homepage(self):
        service = Service(
            executable_path="/home/nayzaw/Documents/learning-pjs/working/pytest-tut/chromedriver_linux64/chromedriver")
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(service=service, chrome_options=option)

        driver.get(self.live_server_url)
        assert "Hello, world!" in driver.title
