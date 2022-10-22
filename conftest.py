import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def init_chrome_webdriver(request):
    service = Service(
        executable_path='/home/nayzaw/Documents/learning-pjs/working/pytest-selenium-tut/chromedriver_linux64/chromedriver')
    option = Options()
    option.headless = True

    driver = webdriver.Chrome(service=service, options=option)
    request.cls.driver = driver
    yield
    driver.close()
