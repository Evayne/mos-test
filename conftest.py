
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options as ChromeOptions

from pages.locators import MainPageLocators
import pages.page as page


@pytest.fixture
def browser():
    options = ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("disable-infobars")

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.maximize_window()
    driver.implicitly_wait(60)

    yield driver

    driver.quit()

@pytest.fixture
def get_links():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    main_page = page.MainPage(browser)
    urls = main_page.find_elements_href(MainPageLocators.LINK_ELEMENT)
    yield driver

