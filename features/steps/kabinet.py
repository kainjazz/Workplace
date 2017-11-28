# -*- coding: utf-8 -*-
import sys

from behave import *
from selene.api import *
from time import sleep
from selene import browser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@Given(u'открыта страница "{url}"')
def step_impl(context, url):
    context.url = url
    browser.open_url(context.url)


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


@Then(u'нажать кнопку "Войти"')
def step_impl(context):
    s('#link_login').click()
    sleep(4)


@Then(u'откроется страница со ссылкой "Перейти в личный кабинет"')
def step_impl(context):
    browser.open_url(context.url)
    sleep(4)
