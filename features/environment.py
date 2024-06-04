from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.application import Application
from selenium.webdriver.chrome.options import Options
#
def browser_init(context, browser_type="chrome", headless=False):
    # """
    # :param context: Behave context
    # :param browser_type: Type of browser to initialize ("chrome" or "firefox")
    # :param headless: Whether to run the browser in headless mode
    # """
    # if browser_type == "chrome":
    #     options = ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #         options.add_argument('--window-size=1920,1080')
    #     driver_path = ChromeDriverManager().install()
    #     service = Service(driver_path)
    #     context.driver = webdriver.Chrome(service=service, options=options)
    #
    # elif browser_type == "firefox":
    #     options = FirefoxOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #         options.add_argument('--window-size=1920,1080')
    #     driver_path = GeckoDriverManager().install()
    #     service = Service(driver_path)
    #     context.driver = webdriver.Firefox(service=service, options=options)
    #
    # else:
    #     raise ValueError(f"Unsupported browser type: {browser_type}")
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)


    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'idyakov_etLzbT'
    bs_key = 'djMq7KBSFzzFZwu4B3eu'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Chrome',
        'sessionName': 'User is able to open Privacy Policy'
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_type = "chrome"  # Change to "firefox" for Firefox
    headless = True  # Set to True for headless mode
    browser_init(context, browser_type, headless)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
