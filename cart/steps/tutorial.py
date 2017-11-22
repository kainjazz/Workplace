#-*- coding: utf-8 -*-
from behave import *
from selene.api import *
from time import sleep
from selene import browser
from selenium import webdriver

driver = webdriver.Remote(
        command_executor='http://selenoid:4444',
        desired_capabilities={'browserName': 'chrome',
                              'version': '62.0',
                              'javascriptEnabled': True})
browser.set_driver(driver)

@Given('open http//:220-volt.ru')
def step_impl(context):
    # config.browser_name = BrowserName.CHROME
    browser.open_url('http://www.220-volt.ru/')

@when('press "login"')
def step_impl(context):
    s('#link_enter').click()

@then('open login form')
def step_impl(context):
    s('[placeholder="Email адрес"]')

@then('input login')
def step_impl(context):
    s('[placeholder="Email адрес"]').send_keys('kainjazz@gmail.com')

@then('input pass')
def step_impl(context):
    s('[placeholder="Пароль"]').send_keys('VAksImUjtaptut1').press_enter()

@then('press Enter')
def step_impl(context):
    s('#link_login').click()
    sleep(4)

@then('go to LK')
def step_impl(context):
    s(by.xpath('//*[@id="auth_block_user_fullname"]')).click()
    sleep(2)

@then('Are u in LK')
def step_impl(context):
    s('[href="/profile/userinfo/"]').hover()

@when('in lk')
def step_impl(context):
    s("[href='/profile/userinfo/']").click()


@then('press contacts')
def step_impl(context):
    s("[href='/profile/userinfo/']").click()


@then('press favorite')
def step_impl(context):
    s("[href='/profile/favorites/']").click()

@then('press gift')
def step_impl(context):
    s("[href='/profile/giftcard/']").click()

@then('press hammer')
def step_impl(context):
    s("[href='/guarantee/']").click()