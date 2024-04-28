from behave import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LogIn_Page


@when(u'User clicks on the Log in button')
def step_impl(context):
    context.HomePage = HomePage(context.driver)
    context.HomePage.ClickOnLogIn()


@when(u'enters a valid username "{username}" and valid password "{password}" in LogIn window')
def step_impl(context, username, password):
    context.LogIn_Page = LogIn_Page(context.driver)
    context.LogIn_Page.Enter_UserName(username)
    context.LogIn_Page.Enter_Password(password)


@when(u'click on log in button')
def step_impl(context):
    context.LogIn_Page.ClickOnLogInButton()


@then(u'user should display Welcome username message')
def step_impl(context):
    context.HomePage = HomePage(context.driver)
    Welcome_text = context.HomePage.Verify_Welcome_User_Text()

    assert Welcome_text, "Welcome is not present"


@when(u'enters a invalid username "{username}" and invalid password "{password}" in LogIn window')
def step_impl(context, username, password):
    context.LogIn_Page = LogIn_Page(context.driver)
    context.LogIn_Page.Enter_UserName(username)
    context.LogIn_Page.Enter_Password(password)


@then(u'User should display "user does not exist" message')
def step_impl(context):
    alert = Alert(context.driver)

    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.alert_is_present())

    alert.accept()
