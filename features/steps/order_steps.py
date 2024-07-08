import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('I am on the Luma homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://magento.softwaretestingboard.com")
    assert "Home Page" in context.browser.title

@given('I login to my user account')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Sign In").click()
    context.browser.find_element(By.ID, "email").send_keys("teszt@supraweb.hu")
    context.browser.find_element(By.ID, "pass").send_keys("Q1w2e3r4")
    context.browser.find_element(By.CSS_SELECTOR, "button.action.login.primary").click()
    time.sleep(2)
    welcome_message = context.browser.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span").text
    print(welcome_message)
    assert "Welcome," in welcome_message

@when('I select the first product from Hot Sellers')
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/a/span/span/img").click()

@then('I add to cart a size XS and color blue product')
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[@id='option-label-size-143-item-166']").click()
    time.sleep(2)
    context.browser.find_element(By.XPATH, "//*[@id='option-label-color-93-item-50']").click()
    time.sleep(2)
    context.browser.find_element(By.XPATH, "//*[@id='product-addtocart-button']").click()
    time.sleep(2)
    context.browser.find_element(By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div/a").click()
    time.sleep(2)
    
@then('I apply a Discount Code in the Shopping cart')
def step_impl(context):
    assert "Shopping Cart" in context.browser.title
    if context.browser.find_element(By.XPATH, "//*[@id='discount-coupon-form']/div/div[2]/div/button").text == "Cancel Coupon":
        context.browser.find_element(By.XPATH, "//*[@id='discount-coupon-form']/div/div[2]/div/button").click()
       
    context.browser.find_element(By.XPATH, "//*[@id='block-discount-heading']").click()
    context.browser.find_element(By.ID, "coupon_code").send_keys("20poff")
    context.browser.find_element(By.XPATH, "//*[@id='discount-coupon-form']/div/div[2]/div/button").click()
    time.sleep(3)
    assert "Discount (Get flat 20% off on all products)" in context.browser.find_element(By.XPATH, "//*[@id='cart-totals']/div/table/tbody/tr[2]/th/span[1]").text
    
@then('I click Proceed to Checkout button in the Shopping cart')
def step_impl(context):
    context.browser.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[1]/ul/li[1]/button").click()
    time.sleep(2)

@then('I confirm the Shipping and Payments details for my order')
def step_impl(context):
    assert "Checkout" in context.browser.title
    context.browser.find_element(By.XPATH, "//*[@id='shipping-method-buttons-container']/div/button").click()
    time.sleep(2)
    context.browser.find_element(By.XPATH, "//*[@id='checkout-payment-method-load']/div/div/div[2]/div[2]/div[4]/div/button").click()
    time.sleep(3)
    assert "Thank you for your purchase!" in context.browser.find_element(By.XPATH, "//*[@id='maincontent']/div[1]/h1/span").text
    time.sleep(3)
    context.browser.quit()
