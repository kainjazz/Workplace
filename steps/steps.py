#-*- coding: utf-8 -*-
from time import sleep
import sys

from behave import *
from selene.api import *
from selene import config
from selene.browsers import BrowserName
from selene import browser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

@Given('go to 220-volt.ru')
def step_impl(context):
    #config.browser_name = BrowserName.CHROME
    browser.open_url('http://www.220-volt.ru/')

@When('navigate to some category')
def step_impl(context):
    s("a[title='Электроинструменты']").hover()
    s("a[title='Аккумуляторные отвертки']").hover().click()

@then('perform some product')
def step_impl(context):
    s("[href='#add-to-cart']").click()
    sleep(5)

@then('close cart banner')
def step_impl(context):
    s("span.ui-button-icon-primary").click()

@then('go to cart')
def step_impl(context):
    s("span#bQuantityTitle").click()

@then('delete product from cart')
def step_impl(context):
    s(".table-item-del a[href='#']").click()