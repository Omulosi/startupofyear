from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_binary
import os


def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("prefs", {
    #   "safebrowsing.enabled": True,
    # })
    options.add_argument("--disable-extensions")
    options.add_argument("--enable-javascript")
    # options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=options)

    # prevent bugs due to elements not loading properly in headless mode
    driver.set_window_size(1440, 900)
    return driver

def get_proxy_driver():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("prefs", {
    #   "safebrowsing.enabled": True,
    # })
    options.add_argument("--disable-extensions")
    options.add_argument("--enable-javascript")
    # options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=options)

    # prevent bugs due to elements not loading properly in headless mode
    driver.set_window_size(1440, 900)
    return driver
