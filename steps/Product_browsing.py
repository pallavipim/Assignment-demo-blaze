from behave import *
from PageObjects.HomePage import HomePage


@given(u'the User is on the homepage')
def step_impl(context):
    homepage_title = context.driver.title
    assert homepage_title == 'STORE', "User isn't on homepage"


@when(u'the User hovers over a product and captures its title and description')
def step_impl(context):
    context.homepage = HomePage(context.driver)

    context.product_name = context.homepage.Get_the_product_name_text()
    context.driver.execute_script("window.scrollBy(0,500);")
    context.product_desc = context.homepage.Get_the_product_description()


@then(u'the User verifies that the product description should contain the product title')
def step_impl(context):
    words_in_product_name = context.product_name.split()
    words_in_product_desc = context.product_desc.split()

    for i in words_in_product_name:
        if i in words_in_product_desc:
            assert True
        else:
            assert False


@then(u'User should display Categories on homepage')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    assert context.homepage.Verify_categoeries_menu(), "categories menu is not present on homepage"


@then(u'the list of Product Categories')
def step_impl(context):
    category_items = context.homepage.Verify_list_of_category()
    assert category_items


@when(u'the user click on a category from the list')
def step_impl(context):
    context.homepage.Click_on_menu_laptop()


@then(u'the user should be taken to the page displaying products in that category')
def step_impl(context):
    context.homepage.Verify_list_of_items_in_menu_laptop()


@then(u'user should display relevant products listed')
def step_impl(context):
    laptop_list = context.homepage.Verify_list_of_items_in_menu_laptop()

    laptop = context.homepage.Verify_element_in_laptop_list(laptop_list=laptop_list)

    assert laptop
