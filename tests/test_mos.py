import pytest
import requests
import pages.page as page
from pages.locators import MainPageLocators
import pytest_check as check
import allure


class TestMos:

    @allure.testcase('Проверка наличия шапки и подвала')
    def test_footer_header(self, browser):
        browser.get("https://www.mos.ru")
        main_page = page.MainPage(browser)

        assert main_page.is_visible_bool(MainPageLocators.HEADER), "Header is not visible"
        assert main_page.is_visible_bool(MainPageLocators.FOOTER), "Footer is not visible"

    @allure.testcase('Проверка ссылок на странице на response 200')
    def test_links_api(self, browser):
        browser.get("https://www.mos.ru")
        main_page = page.MainPage(browser)

        urls = main_page.find_elements_href(MainPageLocators.LINK_ELEMENT)
        for url in urls:
            r = requests.get(url, timeout=5)
            check.equal(r.status_code, 200, f'{url}')

    @allure.testcase('Проверка ссылок на правильный редирект')
    def test_links(self, browser):
        browser.get("https://www.mos.ru")
        main_page = page.MainPage(browser)
        urls = main_page.find_elements_href(MainPageLocators.LINK_ELEMENT)
        for url in urls:
            browser.get(url)
            check.equal(url, browser.current_url)
