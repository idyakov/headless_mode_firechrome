from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)


class HomePage(Page):
    def verify_home_page_url(self):
        print('Verification')

    def verify_user_name(self, name):
        print('name:', name)
#

class HelpPage(Page):
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    SING_IN_POPUP = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    TARGET_EMAIL = (By.CSS_SELECTOR, "[id*='username']")  # input email
    TARGET_PASSWORD = (By.CSS_SELECTOR, "[id*='password']")  # input password
    CLICK_SIGN_IN_USER = (By.CSS_SELECTOR,
                          "button[class='styles__StyledBaseButtonInternal-sc-ysboml-0 "
                          "styles__ButtonPrimary-sc-5fh6rr-0 styles__SignInButton-sc-q9vn5-4 hBqTSs bEdlr gCsDNn']")
    TARGET_VERIFY_ACCOUNT = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    # click button SIgn in with password
    TARGET_NAME_VERIFICATION = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    MENU = (By.CSS_SELECTOR, "select[id='j_id0:contentTemplate:j_id79:j_id80:viewHelpTopics:ViewHelpTopics']")

    def dropdown_menu(self):
        dropdown_menu_1 = self.find_element(*self.MENU)
        select = Select(dropdown_menu_1)
        select.select_by_value('Orders & Purchases')

    def open_help_page(self):
        self.driver.get(
            'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_page(self, expected_url):
        print(expected_url)
        self.wait.until(EC.url_contains(expected_url), message=f'URL verified')
