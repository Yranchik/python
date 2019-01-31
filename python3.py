import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://vtbcmo-qa-2.bpm.lanit:21828/prweb/PRServlet/")
        driver.implicitly_wait(10)
        self.assertIn("Pega", driver.title)

        loginField = driver.find_element_by_id("txtUserID")
        loginField.send_keys("ddukov@test")

        passwordField = driver.find_element_by_id("txtPassword")
        passwordField.send_keys("rules")

        loginBtn = driver.find_element_by_id("sub")
        loginBtn.click()


        actionsList = driver.find_element_by_xpath("//a[text() = 'Создать']")
        actionsList.click()

        createNewObject = driver.find_element_by_xpath("//li[text()]//span[text() = 'Новый лимит (сделка вне лимита)']")
        #driver.save_screenshot("screen.png")
        createNewObject.click()

        driver.switch_to.frame("PegaGadget1Ifr")

        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div//input[@id='PartySearchTin']"))
            )
        finally:
            #driver.save_screenshot("screen1.png")
            companyField = driver.find_element_by_xpath("//div//input[@id='PartySearchTin']")
            companyField.send_keys('123')
            findButton = driver.find_element_by_xpath("//button[@name = 'PreLoanPartySearch_pyWorkPage.MvcPages.PartyComList(1)_4']")
            findButton.click()

            idCompany = driver.find_element_by_xpath("//span[text()='Поле']")
            idCompany.click()

            selectBtn = driver.find_element_by_xpath("//button[text() ='  Выбрать ']")
            selectBtn.click()
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.invisibility_of_element_located((By.XPATH, "//button[text() ='  Выбрать ']"))
                )
            finally:
                summaryInfo = driver.find_element_by_xpath("//h3[text() = 'Общая информация']")
                driver.save_screenshot("screen4.png")
                summaryInfo.click()



    #def tearDown(self):
       # self.driver.close()

#if __name__ == "__main__":
   # unittest.main()