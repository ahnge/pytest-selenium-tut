import pytest

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# from django.test import LiveServerTestCase


# class TestBrowser1(LiveServerTestCase):
#     def test_admin(self):
#         service = Service(
#             executable_path='/home/nayzaw/Documents/learning-pjs/working/pytest-selenium-tut/chromedriver_linux64/chromedriver')
#         driver = webdriver.Chrome(service=service)
#         print(f"{self.live_server_url}/admin/login/?next=/admin/")
#         driver.get(f"{self.live_server_url}/admin/")
#         assert "Log in | Django site admin" in driver.title


# class TestBrowser2(LiveServerTestCase):
#     def test_admin(self):
#         service = Service(
#             executable_path='/home/nayzaw/Documents/learning-pjs/working/pytest-selenium-tut/chromedriver_linux64/chromedriver')
#         option = Options()
#         option.headless = True

#         driver = webdriver.Chrome(service=service, options=option)

#         driver.get(f"{self.live_server_url}/admin/")
#         assert "Log in | Django site admin" in driver.title


# utilizing django.test.LiveServerTestCase
# @pytest.mark.usefixtures("init_chrome_webdriver")
# class TestWhatever(LiveServerTestCase):
#     def test_whatever(self):
#         self.driver.get(f"{self.live_server_url}/admin/")
#         assert "Log in | Django site admin" in self.driver.title


# utilizing pytest live_server
@pytest.mark.usefixtures("init_chrome_webdriver")
class TestWhatever:
    def test_whatever(self, live_server):
        self.driver.get(f"{live_server.url}/admin/")
        assert "Log in | Django site admin" in self.driver.title
