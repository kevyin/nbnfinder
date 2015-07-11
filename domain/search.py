__author__ = 'kevin'

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import re

def search_new(url):
	driver = webdriver.Chrome()
	driver.implicitly_wait(310)
	verificationErrors = []
	accept_next_alert = True

	try:
		driver = driver
		driver.get(url)
		logging.info("getting addresses")
		res = [ e.text for e in driver.find_elements_by_css_selector("h3.address.truncate-single")]
		driver.quit()
	except:
		driver.quit()
		raise

	logging.info("returning addresses")
	return res

