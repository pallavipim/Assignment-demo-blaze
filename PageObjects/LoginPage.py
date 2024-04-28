from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogIn_Page:

    def __init__(self, driver):
        self.driver = driver

    username_ID = 'loginusername'
    password_ID = 'loginpassword'
    buttonLogIn_XPATH = "//button[@onclick='logIn()']"

    def Enter_UserName(self, username):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.username_ID)))
        username_input.send_keys(username)

    def Enter_Password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.password_ID)))
        password_input.send_keys(password)

    def ClickOnLogInButton(self):
        self.driver.find_element(By.XPATH, self.buttonLogIn_XPATH).click()
