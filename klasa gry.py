from modul import get_driver
from selenium.webdriver.remote.webdriver import WebDriver

class EyeGamePage:

    url = "https://www/igame.com/eye-test/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load_game(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iFrame"))

    def click(self):
        self.driver.find_element_by_css_selector('.thechosenone').click()

