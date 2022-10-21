from django.test import LiveServerTestCase

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class HostTest(LiveServerTestCase):

    def test_homepage(self):
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(chrome_options=option)

        driver.get(self.live_server_url)
        assert "Hello, world!" in driver.title


class LoginFormTest(LiveServerTestCase):

    def testform(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)

        driver.get(('%s%s' % (self.live_server_url, '/accounts/login/')))

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        submit = driver.find_element_by_id('submit')

        user_name.send_keys('admin')
        user_password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source
