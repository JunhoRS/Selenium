from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
import time
import os

def take_screenshot(driver, step_name):
    screenshot_dir = "results/screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    screenshot_file = f"{screenshot_dir}/{step_name}.png"
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved: {screenshot_file}")

class AmazonTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.results_dir = "results"

    def get_email(self):
        return "******************"

    def get_password(self):
        return "*********"

    def login(self):
        driver = self.driver
        driver.get("https://www.amazon.com/")
        sign_in_link = driver.find_element(By.ID, "nav-link-accountList")
        sign_in_link.click()
        take_screenshot(driver, "after_sign_in_link_click")

        email_field = driver.find_element(By.ID, "ap_email")
        email_field.send_keys(self.get_email())
        email_field.send_keys(Keys.RETURN)
        take_screenshot(driver, "after_email_input")

        password_field = driver.find_element(By.ID, "ap_password")
        password_field.send_keys(self.get_password())
        password_field.send_keys(Keys.RETURN)
        take_screenshot(driver, "after_password_input")

        WebDriverWait(driver, 10).until(
            element_to_be_clickable((By.ID, "nav-link-accountList"))
        )
        take_screenshot(driver, "after_login")

    def search_product(self, product_name):
        driver = self.driver
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        take_screenshot(driver, "after_search")

        WebDriverWait(driver, 10).until(
            element_to_be_clickable(
                (By.CSS_SELECTOR, "a.s-result-item.s-asin.sg-col-0-of-12.s-col-narrow-width.a-text-normal")
            )
        )
        take_screenshot(driver, "after_search_results")

    def add_product_to_cart(self):
        driver = self.driver
        product_link = driver.find_element(By.CSS_SELECTOR, "a.s-result-item.s-asin.sg-col-0-of-12.s-col-narrow-width.a-text-normal")
        product_link.click()
        take_screenshot(driver, "product_description")

        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        take_screenshot(driver, "added_product")

    def logout(self):
        driver = self.driver
        logout_button = driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/flex/sign-out.html']")
        logout_button.click()
        take_screenshot(driver, "logged_out")

    def teardown(self):
        self.driver.quit()

test = AmazonTests()
test.login()
test.search_product("Libro de programación Python")
test.add_product_to_cart()
test.logout()
test.teardown()
take_screenshot(test.driver, "end")
