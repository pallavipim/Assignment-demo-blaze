from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    buttonSignUp_ID = 'signin2'
    buttonLogIn_ID = 'login2'
    text_WelcomeUser_ID = "nameofuser"
    button_Next_ID = "next2"
    last_product_LINK_TEXT = 'MacBook Pro'
    button_addToCart_LINK_TEXT = 'Add to cart'
    button_Logout_ID = "logout2"
    product_LINK_TEXT = "Nokia lumia 1520"
    button_cart_ID = "cartur"
    text_product_description_XPATH = '//*[@id="tbodyid"]/div[3]'
    text_product_name_XPATH = '//*[@id="tbodyid"]/div[3]/div/div/h4/a'
    categories_ID = 'cat'
    category_TAG_NAME = 'a'
    categories_XPATH = '//*[@id="contcont"]/div/div[1]/div'
    menu_laptop_XPATH = "//a[text()='Laptops']"
    laptop_list_ID = "tbodyid"
    laptop_TAG_NAME = 'div'
    lap_XPATH = "//a[text()='Monitors']"
    phone_XPATH = "//a[text()='Phones']"
    monitor_XPATH = "//a[text()='Laptops']"

    def ClickOnSignUp(self):
        btn_signUp = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.buttonSignUp_ID)))
        btn_signUp.click()

    def ClickOnLogIn(self):
        self.driver.find_element(By.ID, self.buttonLogIn_ID).click()

    def Verify_Welcome_User_Text(self):
        return self.driver.find_element(By.ID, self.text_WelcomeUser_ID)

    def Click_Next_Button_Until_reches_the_last_page(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.button_Next_ID)))
        return next_button

    def Click_on_last_product_of_the_last_page(self):
        last_product_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.last_product_LINK_TEXT)))
        last_product_link.click()

    def Click_on_button_Add_to_Cart(self):
        self.driver.find_element(By.LINK_TEXT, 'Add to cart').click()

    def ClickOnLogOut(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.button_Logout_ID)))
        logout_button.click()

    def Verify_logIn_button(self):
        return self.driver.find_element(By.ID, self.buttonLogIn_ID)

    def Click_on_desired_product(self):
        self.driver.find_element(By.LINK_TEXT, self.product_LINK_TEXT).click()

    def Click_on_menu_Cart(self):
        self.driver.find_element(By.ID, self.button_cart_ID).click()

    def Get_the_product_name_text(self):
        return self.driver.find_element(By.XPATH, self.text_product_name_XPATH).text

    def Get_the_product_description(self):
        return self.driver.find_element(By.XPATH, self.text_product_description_XPATH).text

    def Verify_categoeries_menu(self):
        categories = self.driver.find_element(By.XPATH, self.categories_XPATH)
        return categories

    def Verify_list_of_category(self):
        category_laptop = self.driver.find_element(By.XPATH, self.lap_XPATH)
        category_phones = self.driver.find_element(By.XPATH, self.phone_XPATH)
        category_monitors = self.driver.find_element(By.XPATH, self.monitor_XPATH)

        return category_monitors, category_phones, category_laptop

    def Click_on_menu_laptop(self):
        self.driver.find_element(By.XPATH, self.menu_laptop_XPATH).click()

    def Verify_list_of_items_in_menu_laptop(self):
        return self.driver.find_element(By.ID, self.laptop_list_ID)

    def Verify_element_in_laptop_list(self, laptop_list):
        laptop = laptop_list.find_elements(By.TAG_NAME, self.laptop_TAG_NAME)

        return laptop
