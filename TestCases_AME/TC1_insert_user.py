import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from appium import webdriver
import sys

sys.path.append("C://Users/elsys/Documents/pycharm_robot/appium_POM")
from Pages_objects.user_functions import UserPage
from devices_setup.device_setup import DevicesSetup


class UserTest(unittest.TestCase):

    def setUp(self):
        dv = DevicesSetup
        self.user_name = dv.name_user1
        self.dc = {'appPackage': dv.app_package_used, 'appActivity': dv.appActivity_used,
                   'platformName': dv.os_mobile, 'deviceName': dv.id_mobile}
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        # appPackage and appActivity  desired capability specify app details to Appium
        # platformName desired capability specify platform detail to Appium
        # This is not clear the app when insert user
        # self.dc['noReset'] = 'true'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(5)

    def test_user_cadastro(self):
        up = UserPage(self.driver)
        up.click_banner_allow()
        up.click_button_mais()
        up.click_novo_cadastro()
        up.inserir_campo_nome(self.user_name)
        time.sleep(1)
        up.click_salvar_cadastro()
        time.sleep(2)
        up.click_OK_salvar()
        time.sleep(1)
        up.back_button()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users/elsys/Documents/pycharm_robot/appium_POM/Reports'))
