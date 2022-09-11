import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium import *

import pytest



@pytest.fixture()
def test_firefoxDriver():
    global driver
    driver = webdriver.Firefox(executable_path="D:\study\python\Zeuz1\Webdriver\geckodriver.exe")
    driver.maximize_window()
    driver.delete_all_cookies()
    # driver.get(login_page_url)

    yield
    driver.close()
    driver.quit()



def test_task_for_Successful_statusMassage(test_firefoxDriver):
    driver.get("https://demo.zeuz.ai/web/level/one/actions/save_text")

    randomText = driver.find_element(By.XPATH, "//div[@class='container']//h4[@id='randomText']").text
    print(randomText)
    driver.find_element(By.XPATH, "//input[@id='enter_text']").send_keys(randomText)
    driver.find_element(By.XPATH, "//button[@id='verify_id']").click()
    statusMassage = driver.find_element(By.XPATH, "// p[ @ id = 'text_showing']").text
    if statusMassage == "You have successfully verified the text":
        assert True
    else:
        assert False





