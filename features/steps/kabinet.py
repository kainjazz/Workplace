# -*- coding: utf-8 -*-
import sys

from behave import *
from selene.api import *
from time import sleep
from selene import browser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@given(u'открыта страница "{url}"')
def step_impl(context, url):
    context.url = url
    browser.open_url(context.url)


@given(u'выбран город "{city}"')
def step_impl(context, city):
    if s("[href='/cities/']").should(have.text(city)):
        assert True
    else:
        s("[href='/cities/']").click()
        s("[for='city7800000000000']").click()
        sleep(2)


@when(u'нажать ссылку "Вход"')
def step_impl(context):
    s('#link_enter').click()


@then(u'появится форма входа')
def step_impl(context):
    s('[placeholder="Email адрес"]')


@when(u'ввести емейл "{mail}"')
def step_impl(context, mail):
    s('[placeholder="Email адрес"]').send_keys(mail)
    sleep(2)


@when(u'ввести пароль "{password}"')
def step_impl(context, password):
    s('[placeholder="Пароль"]').send_keys(password)
    sleep(1)


@when(u'нажать кнопку "Войти"')
def step_impl(context):
    s('#link_login').click()
    sleep(4)


@then(u'в шапке сайта появится ссылка "Перейти в личный кабинет"')
def step_impl(context):
    browser.open_url(context.url)
    s("#auth_block_user_fullname").hover()
    sleep(4)
