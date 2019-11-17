import unittest
import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        user = "rashmik"
        pwd = "guhaamin"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        try:
            elem = driver.find_element_by_xpath("/ html / body / div / div / div / div / div / div / div / div / div[1] / div / div / h2")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)


    def test_customer_city(self):
        user = "rashmik"
        pwd = "guhaamin"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/customer_list")
        time.sleep(3)
        try:
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[9]")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)


    def test_customer_edit(self):
        user = "rashmik"
        pwd = "guhaamin"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/customer_list")
        time.sleep(3)
        try:
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a")
            time.sleep(3)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_element_by_xpath("/html/body/form/button")
            time.sleep(3)
            elem.send_keys(Keys.RETURN)
            elem = driver.find_element_by_xpath("/ html / body / div / div / div / div[2] / h2")
            time.sleep(3)
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False


    def test_product_list(self):
        user = "rashmik"
        pwd = "guhaamin"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/product_list")
        time.sleep(3)
        try:
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/h2")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

