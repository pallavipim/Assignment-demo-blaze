from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp_Page:

    def __init__(self, driver):
        self.driver = driver

    username_ID = 'sign-username'
    password_ID = 'sign-password'
    buttonSignUp_XPATH = "//button[@onclick='register()']"

    def Enter_userName(self, username):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.username_ID)))
        username_input.send_keys(username)

    def Enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.password_ID)))
        password_input.send_keys(password)

    def ClickOnSignUpButton(self):
        self.driver.find_element(By.XPATH, self.buttonSignUp_XPATH).click()
