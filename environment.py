from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.demoblaze.com/")
    context.driver.implicitly_wait(50)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()

