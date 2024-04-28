from behave import *
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LogIn_Page


@given(u'User clicks on the Log in button')
def step_impl(context):
    context.HomePage = HomePage(context.driver)
    context.HomePage.ClickOnLogIn()


@given(u'enters a valid username "{username}" and valid password "{password}" in LogIn window')
def step_impl(context, username, password):
    context.LogIn_Page = LogIn_Page(context.driver)
    context.LogIn_Page.Enter_UserName(username)
    context.LogIn_Page.Enter_Password(password)


@given(u'click on log in button')
def step_impl(context):
    context.LogIn_Page.ClickOnLogInButton()


@when(u'User click on Logout button')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.homepage.ClickOnLogOut()


@then(u'user should display Log in button')
def step_impl(context):
    login_button = context.HomePage.Verify_logIn_button()
    assert login_button, "Log In Button is not present"
