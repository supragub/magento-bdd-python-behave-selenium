import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('I am on the Luma homepage and I am not logged in')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://magento.softwaretestingboard.com")

@given('I navigate to the Customer Login page')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Sign In").click()

@when('I fill in the login form with valid data')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("teszt@supraweb.hu")
    context.browser.find_element(By.ID, "pass").send_keys("Q1w2e3r4")

@when('I dont enter anything into email and password fields')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("")
    context.browser.find_element(By.ID, "pass").send_keys("")

@when('I enter invalid credentials into email and password fields')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("teszt2@supraweb.hu")
    context.browser.find_element(By.ID, "pass").send_keys("password")

@when('I click on login button')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "button.action.login.primary").click()

@then('I should get logged in')
def step_impl(context):
    time.sleep(2)
    welcome_message = context.browser.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span").text
    print(welcome_message)
    assert "Welcome," in welcome_message
    context.browser.quit()

@then('I should see required fields warning message and the login fails')
def step_impl(context):
    email_error = context.browser.find_element(By.XPATH, "//*[@id='email-error']").text
    password_error = context.browser.find_element(By.XPATH, "//*[@id='pass-error']").text
    print(email_error)
    print(password_error)
    assert "This is a required field." in email_error
    assert "This is a required field." in password_error
    context.browser.quit()

@then('I should see invalid credentials warning message and the login fails')
def step_impl(context):
    invalid_credentials_error = context.browser.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div[2]/div/div/div").text
    print(invalid_credentials_error)
    assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." in invalid_credentials_error
    context.browser.quit()