from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePage


class HomePage(BasePage):
    zor_conn = ( By.LINK_TEXT,'צור קשר')
    odot = (By.LINK_TEXT, 'אודות')

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver.get('https://rt-ed.co.il/')

    def go_to_zor_conn(self):
        self.do_click(self.zor_conn)

    def go_to_odot(self):
        self.do_click(self.odot)
