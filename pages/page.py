import time

from selenium.common.exceptions import TimeoutException
from pages.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def switch_to_tab(self, tab_index: int):
        """Переключение по вкладкам. В tab_index передаем цифру-индекс вкладки (текущая вкладка имеет индекс 0)"""

        time.sleep(1)
        all_tabs = self.driver.window_handles

        if len(all_tabs) == 1:
            print("Доступна одна вкладка")
            self.driver.switch_to.window(all_tabs[tab_index])
        else:
            self.driver.switch_to.window(all_tabs[tab_index])
            time.sleep(1)
        return self

    def do_click(self, by_locator, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator)).click()
        return self

    def is_visible_bool(self, by_locator, wait_time=4):
        try:
            if WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator)):
                return True
        except TimeoutException:
            return False

    def find_elements(self, by_locator):
        """Возвращает список текста элементов в виде объекта вебдрайвера"""
        elements = self.driver.find_elements(*by_locator)
        return elements



class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def find_elements_href(self, by_locator):
        """Возвращает список текста элементов в виде объекта вебдрайвера"""
        elements = self.driver.find_elements(*by_locator)
        element_list = []
        for element in elements:
            element_list.append(element.get_attribute("href"))
        return element_list



