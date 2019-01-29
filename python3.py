import unittest
from selenium import webdriver
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
        self.assertIn("Pega", driver.title)

        loginField = driver.find_element_by_id("txtUserID")
        loginField.send_keys("akondratyev@test")

        passwordField = driver.find_element_by_id("txtPassword")
        passwordField.send_keys("rules")

        loginBtn = driver.find_element_by_id("sub")
        loginBtn.click()


        actionsList = driver.find_element_by_css_selector(".pzbtn-img")
        actionsList.click()

        time.sleep()



        assert "Кондратьев" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()