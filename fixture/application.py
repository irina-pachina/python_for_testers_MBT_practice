# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


# class Application represents a complex fixture.
# contains a link to the driver, methods that interact with the browser through the driver
# and perform primitive actions. it provides high-level methods, i.e. login
class Application:
    def __init__(self, browser, config):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.stand_url = config["web"]["standURL"]
        self.config = config

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.stand_url)

    def destroy(self):
        self.wd.quit()