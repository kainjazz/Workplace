#-*- coding: utf-8 -*-
import sys

from behave import *
from selene.api import *
from time import sleep
from selene import browser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

@Given('открыта страница "{url}"')
def step_impl(context, url):
    browser.open_url(url)

@when('нажать ссылку "Вход"')
def step_impl(context):
    s('#link_enter').click()

@then('появится форма входа')
def step_impl(context):
    s('[placeholder="Email адрес"]')

@when('ввести емейл')
def step_impl(context):
    s('[placeholder="Email адрес"]').send_keys('kainjazz@gmail.com')

@when('ввести пароль')
def step_impl(context):
    s('[placeholder="Пароль"]').send_keys('VAksImUjtaptut1')

@when('нажать кнопку "Войти"')
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