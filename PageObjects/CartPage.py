from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    product_cost_ID = 'totalp'
    button_placeOrder_XPATH = "//button[@class='btn btn-success']"
    button_purchase_XPATH = "//button[@onclick='purchaseOrder()']"
    text_placeOrder_ID = "orderModalLabel"
    row_XPATH = '// *[ @ id = "tbodyid"] / tr / td[1] / img'
    name_ID = "name"
    country_ID = 'country'
    city_ID = "city"
    CreditCard_ID = 'card'
    month_ID = 'month'
    year_ID = 'year'
    text_ThankYou_XPATH = '/html/body/div[10]/h2'

    def Verify_product_is_present_in_cart(self):
        return self.driver.find_element(By.XPATH, self.row_XPATH)

    def Verify_product_cost_is_not_present(self):
        return self.driver.find_element(By.ID, self.product_cost_ID)

    def Click_on_place_order_button(self):
        self.driver.find_element(By.XPATH, self.button_placeOrder_XPATH).click()

    def Click_on_purchase_button(self):
        self.driver.find_element(By.XPATH, self.button_placeOrder_XPATH)

    def Verify_text_place_order(self):
        self.driver.find_element(By.ID, self.text_placeOrder_ID)

    def Fill_information_in_place_order_window(self,name, country, city, CC, month, year):
        name = self.driver.find_element(By.ID, self.name_ID).send_keys(name)

        wait = WebDriverWait(self.driver, 10)
        country_name = wait.until(EC.presence_of_element_located((By.ID, self.country_ID)))
        country_name.send_keys(country)

        city_name = self.driver.find_element(By.ID, self.city_ID)
        city_name.send_keys(city)

        CC_number = self.driver.find_element(By.ID, self.CreditCard_ID)
        CC_number.send_keys(CC)

        CC_month = self.driver.find_element(By.ID, self.month_ID)
        CC_month.send_keys(month)

        wait = WebDriverWait(self.driver, 10)
        CC_year = wait.until(EC.presence_of_element_located((By.ID, self.year_ID)))
        CC_year.send_keys(2025)

        return name, country_name, city_name, CC_number, CC_month, CC_year

    def Click_on_purchase_Button(self):
        self.driver.find_element(By.XPATH, self.button_purchase_XPATH).click()

    def Get_text_ThankYouForYourPurchase(self):
        return self.driver.find_element(By.XPATH, self.text_ThankYou_XPATH).text
