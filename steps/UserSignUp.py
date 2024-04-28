from behave import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.HomePage import HomePage
from PageObjects.SignUpPage import SignUp_Page


@when(u'User clicks on the Sign Up button')
def step_impl(context):
    context.HomePage = HomePage(context.driver)
    context.HomePage.ClickOnSignUp()


@when(u'enters a valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.signUpPage = SignUp_Page(context.driver)

    context.signUpPage.Enter_userName(username)
    context.signUpPage.Enter_password(password)


@when(u'click on sign-up button')
def step_impl(context):
    context.signUpPage.ClickOnSignUpButton()


@then(u'It should display confirmation message')
def step_impl(context):
    alert = Alert(context.driver)

    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.alert_is_present())

    assert alert.text == 'Sign up successful.', "SignUp successful message doesn't match"

    alert.accept()


# Negative Scenario:
@when(u'enters a already registered username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.signUpPage = SignUp_Page(context.driver)

    context.signUpPage.Enter_userName(username)
    context.signUpPage.Enter_password(password)


@then(u'It should display user already exist message')
def step_impl(context):
    alert = Alert(context.driver)

    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.alert_is_present())

    assert alert.text == 'This user already exist.', "SignUp confirmation massage user already exist doesn't match"

    alert.accept()
