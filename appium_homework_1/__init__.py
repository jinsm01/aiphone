from appium import webdriver


class BasePage:
    def __init__(self):
        des_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'devicesName': 'emulator-7555',
                    'appPackage': 'com.xueqiu.android', 'appActivity': '.common.MainActivity', 'noReset': True,
                    'unicodeKeyBoard': True, 'resetKeyBoard': True, 'dontStopAppOnReset': True,
                    'skipDeviceInitialization': True}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def back(self):
        return self.driver.back()


from appium.webdriver.common.mobileby import MobileBy
from appium_homework_1.page.base_page import BasePage


class Index(BasePage):
    content = None

    def test_search(self, search_content):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.find(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(search_content)
        self.find(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        self.content = self.find(MobileBy.ID, 'com.xueqiu.android:id/stockName').text
        self.back()


import pytest
from appium_homework_1.page.index import Index


class TestSearch:
    def setup(self):
        self.index = Index()

    @pytest.mark.parametrize('search_content', ['阿里巴巴', '阅文集团'])
    def test_search(self, search_content):
        self.index.test_search(search_content)
        assert search_content == self.index.content
