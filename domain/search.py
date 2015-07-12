__author__ = 'kevin'

import logging
from selenium import webdriver


def search_new(url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    verificationErrors = []
    accept_next_alert = True

    try:
        driver = driver
        driver.get(url)
        logging.info("getting addresses")
        res = [e.text for e in driver.find_elements_by_css_selector("h3.address.truncate-single")]
        driver.quit()
    except:
        driver.quit()
        raise

    logging.info("returning addresses")
    return res

