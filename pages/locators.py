from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (By.ID, "mos-header")
    FOOTER = (By.ID, "mos_footer")
    LINK_ELEMENT = (By.XPATH, "//a[contains(@href,'')]")
