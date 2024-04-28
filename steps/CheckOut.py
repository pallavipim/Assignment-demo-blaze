from behave import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage


@given(u'User click on the desired product')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.homepage.Click_on_desired_product()


@given(u'add product to cart by clicking on button Add to cart')
def step_impl(context):
    context.homepage.Click_on_button_Add_to_Cart()

    alert = Alert(context.driver)

    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.alert_is_present())

    alert.accept()


@when(u'user click on Cart menu')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.homepage.Click_on_menu_Cart()


@then(u'selected product should be displayed in the product list')
def step_impl(context):
    context.cartpage = CartPage(context.driver)
    product = context.cartpage.Verify_product_is_present_in_cart()

    assert product, "product is not present in the cart"


@given(u'User is on Home Page')
def step_impl(context):
    home_page_title = context.driver.title
    assert home_page_title == 'STORE', "User isn't on product listing page"


@when(u'User navigates to cart page')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.homepage.Click_on_menu_Cart()


@then(u'Cart page should be empty')
def step_impl(context):
    context.cartpage = CartPage(context.driver)

    product_cost = context.cartpage.Verify_product_cost_is_not_present()
    assert product_cost, 'product cost is present in the cart'


@when(u'User clicks on place order button')
def step_impl(context):
    context.cartpage.Click_on_place_order_button()
    new_window = context.driver.window_handles[-1]
    context.driver.switch_to.window(new_window)

    new_window_test = context.cartpage.Verify_text_place_order()

    if new_window_test == 'Place order':
        assert False
    else:
        assert True


@when(u'provide checkout details: "{name}","{country}","{city}","{CC}","{month}","{year}" and click on purchase button')
def step_impl(context, name, country, city, CC, month, year):
    context.cartpage.Fill_information_in_place_order_window(name, country, city, CC, month, year)

    context.driver.execute_script("window.scrollTo(0,1000);")
    context.cartpage.Click_on_purchase_Button()


@then(u'user should see message as unable to checkout with empty cart')
def step_impl(context):
    main_window = context.driver.current_window_handle

    for window in context.driver.window_handles:
        if window != main_window:
            context.driver.switch_to.window(window)

    ThankYou_text = context.cartpage.Get_text_ThankYouForYourPurchase()

    if ThankYou_text == "Thank you for your purchase!":
        assert False, "Unable to proceed with checkout as no products have been added to the cart."
    else:
        assert True
