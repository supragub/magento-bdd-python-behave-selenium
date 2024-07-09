from behave import fixture
from selenium import webdriver

@fixture
def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()

@fixture
def after_scenario(context, scenario):
    context.browser.quit()