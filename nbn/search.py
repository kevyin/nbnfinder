__author__ = 'kevin'

import logging
import re
import time

from selenium import webdriver


def search_addr(addr):
    driver = webdriver.Firefox()
    driver.implicitly_wait(130)
    # driver.set_page_load_timeout(30)
    base_url = "http://www.nbnco.com.au/connect-home-or-business/check-your-address.html"
    verificationErrors = []
    accept_next_alert = True

    logging.info("searching: " + addr)

    tf = False
    type = "no"
    try:
        driver.get(base_url + "/connect-home-or-business/check-your-address.html")
        driver.find_element_by_id("map-lookup-input").clear()
        driver.find_element_by_id("map-lookup-input").send_keys(addr)
        logging.info("CLICKING")
        driver.find_element_by_id("map-lookup-button-home").click()
        logging.info("waiting")
        # WebDriverWait(driver, 10).until(
        # 	EC.visibility_of_element_located((By.CLASS_NAME, "richtext"))
        # )
        # WebDriverWait(driver, 10).until(
        # 	EC.visibility_of_element_located((By.ID, "main"))
        # )
        time.sleep(4)

        logging.info("waited")

        # logging.info("main" + driver.find_element_by_id('main').text)
        # Warning: assertTextPresent may require manual changes
        # body = driver.find_element_by_css_selector("BODY").text
        body = driver.find_element_by_id('main').text
        if re.search("Great news", body) is not None:
            logging.info("YES")
            tf = True
            type = "available"
        elif re.search("Work started", body) is not None:
            logging.info("Started")
            tf = True
            type = "started"
        elif re.search("is coming to your", body) is not None:
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

