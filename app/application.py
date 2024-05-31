# from pages.HomePage import HomePage
from pages.base_page import Page
from pages.MainPage import MainPage
# from pages.header import Header
from pages.LoginPage import LoginPage

#
class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        # self.header = Header(driver)
        self.login_page = LoginPage(driver)
        # self.home_page = HomePage(driver)

