from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Page):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    REELLY_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")  # input email
    REELLY_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")  # input password
    CLICK_SETTINGS = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Settings']")
    CLICK_EDIT_PROFILE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
    INPUT_FIELD_VERIFICATION = (
        By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    CLICK_SAVE = (By.XPATH, "//div[contains(text(), 'Save changes')]")
    CLICK_CLOSE = (By.XPATH, "//div[contains(@class, 'profile-button-block') and contains(., 'Close')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.default_pw = 'Password'

    def click_sign_in(self):
        self.click(*self.CONTINUE_BUTTON)

    def input_credentials(self):
        self.input_text('dyak.ilya@gmail.com', *self.REELLY_EMAIL)  #input your own registered email
        self.input_text('XrvzakG!E4i@Zzh', *self.REELLY_PASSWORD)  #input your own registered password

    def click_on_settings(self):
        self.click(*self.CLICK_SETTINGS)

    def edit_profile(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CLICK_EDIT_PROFILE)
        ).click()

    def input_fields(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_FIELD)
        )
        self.input_text('Hebrew, Russian', *self.INPUT_FIELD)

    def verify_input_fields(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_FIELD_VERIFICATION)
        )
        text_message = element.get_attribute('value')
        print(f'The language chosen is - "{text_message}"')

    def click_on_save(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CLICK_SAVE)
        ).click()

    def click_on_close(self):
        self.click(*self.CLICK_CLOSE)
