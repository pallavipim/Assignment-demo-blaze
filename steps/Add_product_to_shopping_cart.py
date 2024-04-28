from behave import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage


@given(u'User on the product listing page')
def step_impl(context):
    product_listing_page_title = context.driver.title
    assert product_listing_page_title == 'STORE', "User isn't on product listing page"


@when(u'user clicks on next button until reaches the last page')
def step_impl(context):
    context.homepage = HomePage(context.driver)

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
    next_button = context.homepage.Click_Next_Button_Until_reches_the_last_page()

    while next_button.is_enabled():
        next_button.click()
        context.driver.implicitly_wait(2)
        break


@when(u'clicks on the last product')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.homepage.Click_on_last_product_of_the_last_page()


@when(u'user clicks on Add to Cart button')
def step_impl(context):
    context.homepage.Click_on_button_Add_to_Cart()


@then(u'user should display product added message')
def step_impl(context):
    alert = Alert(context.driver)

    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.alert_is_present())
    Product_added = alert.text

    assert Product_added == "Product added", "Product does not added to the cart"
