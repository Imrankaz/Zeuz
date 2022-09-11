import time

from POM.Pages.taskPage import taskPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
#from selenium import *

from Zeuz1.POM.Locators import locators
from Zeuz1.POM.Pages import taskPage

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


class TestTask:
    @pytest.fixture()
    def test_setup(self):
        self.locator_obj = locators
        global driver
        self.driver = webdriver.Firefox(executable_path= self.locator_obj.locators.geckoDriver)

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        yield
        self.driver.close()
        self.driver.quit()
        print("test completed")

    def test_task_for_Successful_statusMassage(self, test_setup):
        self.driver.get(self.locator_obj.locators.task_page_URL)

        self.taskPage_obj = taskPage(self.driver)

        randomText= self.taskPage_obj.taskpage.catch_randomText()
        print(randomText)
        self.taskPage_obj.taskpage.input_randomText_WE(randomText)
        self.taskPage_obj.taskpage.click_on_Verify_button()
        statusMassage = self.taskPage_obj.taskpage.status_Massage()

        if statusMassage == "You have successfully verified the text":
            assert True
        else:
            assert False

