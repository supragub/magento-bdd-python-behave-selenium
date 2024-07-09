import time
from selenium.webdriver.common.by import By
from behave import given, when, then
from faker import Faker

@given('I am on the Luma homepage without logged in')
def step_impl(context):
    context.browser.get("https://magento.softwaretestingboard.com")

@given('I navigate to the registration page')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Create an Account").click()
   
@when('I fill in the registration form with valid data')
def step_impl(context):
    fake = Faker()
    context.browser.find_element(By.ID, "firstname").send_keys("Teszt")
    context.browser.find_element(By.ID, "lastname").send_keys("Elek")
    context.browser.find_element(By.ID, "email_address").send_keys(fake.email())
    context.browser.find_element(By.ID, "password").send_keys("Q1w2e3r4")
    context.browser.find_element(By.ID, "password-confirmation").send_keys("Q1w2e3r4")

@when('I fill in the registration form with invalid email format')
def step_impl(context):
    context.browser.find_element(By.ID, "firstname").send_keys("Teszt")
    context.browser.find_element(By.ID, "lastname").send_keys("Elek")
    context.browser.find_element(By.ID, "email_address").send_keys("supraweb.hu")
    context.browser.find_element(By.ID, "password").send_keys("Q1w2e3r4")
    context.browser.find_element(By.ID, "password-confirmation").send_keys("Q1w2e3r4")

@when('I fill in the registration form with invalid "{password}" or "{confirm_password}"')
def step_impl(context, password, confirm_password):
    context.browser.find_element(By.ID, "firstname").send_keys("Teszt")
    context.browser.find_element(By.ID, "lastname").send_keys("Elek")
    context.browser.find_element(By.ID, "email_address").send_keys("supraweb.hu")
    context.browser.find_element(By.ID, "password").send_keys(password)
    context.browser.find_element(By.ID, "password-confirmation").send_keys(confirm_password)

@when('I fill in the registration form with already registered email address')
def step_impl(context):
    context.browser.find_element(By.ID, "firstname").send_keys("Teszt")
    context.browser.find_element(By.ID, "lastname").send_keys("Elek")
    context.browser.find_element(By.ID, "email_address").send_keys("teszt@supraweb.hu")
    context.browser.find_element(By.ID, "password").send_keys("Q1w2e3r4")
    context.browser.find_element(By.ID, "password-confirmation").send_keys("Q1w2e3r4")

@when('I submit the registration form')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()

@then('I should be registered successfully and redirected to My Account page')
def step_impl(context):
    assert "My Account" in context.browser.title

@then('I should see invalid email format warning message and the registration fails')
def step_impl(context):
    email_address_error = context.browser.find_element(By.XPATH, "//*[@id='email_address-error']").text
    print(email_address_error)
    assert "Please enter a valid email address (Ex: johndoe@domain.com)." in email_address_error

@then('I should see invalid password warning message and the registration fails')
def step_impl(context):
    password_error = context.browser.find_element(By.XPATH, "//*[@id='password-error']").text
 #   confirm_password_error = context.browser.find_element(By.XPATH, "//*[@id='password-confirmation-error']").text
    print(password_error)
    assert "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored." or "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters." in password_error

@then('I should see a warning message and the registration fails')
def step_impl(context):
    time.sleep(2)
    registration_error_message = context.browser.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div[2]/div/div/div").text
    print(registration_error_message)
    assert "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account." in registration_error_message

    