import os
import time

import pytest


def take_screenshot(driver, name):
    print('first', os.path.dirname(name))
    print('second', os.path.join("screenshots", os.path.dirname(name)))
    os.makedirs(os.path.join("screenshots",
                os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshots", name))


@pytest.mark.usefixtures("init_chrome_webdriver")
class TestSomething:
    def test_takescreenshot(self, live_server):
        self.driver.get(f"{live_server.url}/admin/")
        take_screenshot(self.driver, "again.png")
