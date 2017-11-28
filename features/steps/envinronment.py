#-*- coding: utf-8 -*-
import sys

from behave import *
from selene.api import *
from time import sleep
from selene import browser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    driver = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome',
                              'version': '62.0',
                              'javascriptEnabled': True})
except WebDriverException, e:
    print("Ошибка при подключении к Selenoid:", e)
    sys.exit(1)

browser.set_driver(driver)

print("Подключен Selenoid\n")
