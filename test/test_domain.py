# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Domain(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.domain.com.au/search/buy/state/nsw/area/eastern-suburbs/sydney-city/region/sydney-region/suburb/darlinghurst/east-sydney/strawberry-hills/surry-hills/?ssubs=1&bedrooms=1&to=750000&searchterm=2010&features=broadband+internet+access|2&sort=date-asc"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_domain(self):
        driver = self.driver
        driver.get(
            self.base_url + "/search/buy/state/nsw/area/eastern-suburbs/sydney-city/region/sydney-region/suburb/darlinghurst/east-sydney/strawberry-hills/surry-hills/?ssubs=1&bedrooms=1&to=750000&searchterm=2010&features=broadband+internet+access%7c2&sort=date-asc")
        for e in driver.find_elements_by_css_selector("h3.address.truncate-single"):
            print e.text


def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e:
        return False
    return True


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException, e:
        return False
    return True


def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()