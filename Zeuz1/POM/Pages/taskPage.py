from selenium.webdriver.common.by import By


class taskPage:
    def __init__(self,driver):
        self.driver = driver
        self.randomText_WE = "//div[@class='container']//h4[@id='randomText']"
        self.input_randomText_WE = "//input[@id='enter_text']"
        self.verify_button_WE = "//button[@id='verify_id']"
        self.statusMassage_WE = "// p[ @ id = 'text_showing']"




    def catch_randomText(self):
        randomText = self.driver.find_element(By.XPATH, "//div[@class='container']//h4[@id='randomText']").text
        print(" \n random Text is: ",randomText, "\n")

        return randomText

    def input_randomText(self, randomText):
        self.driver.find_element(By.XPATH, self.input_randomText_WE).clear()
        self.driver.find_element(By.XPATH, self.input_randomText_WE).send_keys(randomText)

    def click_on_Verify_button(self):
        self.driver.find_element(By.XPATH, self.verify_button_WE).click()

    def status_Massage(self):
        statusMassage = self.driver.find_element(By.XPATH, self.statusMassage_WE).text
        print(" \n status message is: ",statusMassage, "\n")

        return statusMassage
