__author__ = 'kevin'

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def search_addr(addr):
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	# driver.set_page_load_timeout(30)
	base_url = "http://www.nbnco.com.au/connect-home-or-business/check-your-address.html"
	verificationErrors = []
	accept_next_alert = True

	logging.info("searching: " + addr)

	tf = False
	type = "no"
	try:
		driver
		driver.get(base_url + "/connect-home-or-business/check-your-address.html")
		driver.find_element_by_id("map-lookup-input").clear()
		driver.find_element_by_id("map-lookup-input").send_keys(addr)
		driver.find_element_by_id("map-lookup-button-home").click()
		try:
			element = WebDriverWait(driver, 10).until(
				EC.presence_of_all_elements_located(EC.visibility_of_element_located(driver.find_element_by_id('main')))
			)
		finally:
			driver.quit()

		logging.info("main" + driver.find_element_by_id('main').text)
		# Warning: assertTextPresent may require manual changes
		body = driver.find_element_by_css_selector("BODY").text
		if re.match(r"^[\s\S]*Great news, the nbn[\s\S]*$", body):
			logging.info("YES")
			tf = True
			type = "available"
		elif re.match(r"^[\s\S]*Work started in your area[\s\S]*$", body):
			logging.info("Started")
			tf = True
			type = "started"
		elif re.match(r"^[\s\S]*is coming to your[\s\S]*$", body):
			logging.info("Coming")
			tf = True
			type = "coming"
		else:
			logging.info("NO")
		driver.quit()
	except:
		driver.quit()
		raise

	return type

