import unittest
import re
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
       driver.get("https://www.cbr.ru/")
       driver.implicitly_wait(10)

       course = driver.find_element_by_xpath("//td[@class='weak']")
       x = course.text
       print(x)
       line = x.replace('руб.', '').split(' ')[1]
       print(line)





