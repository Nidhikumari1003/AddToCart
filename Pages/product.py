import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login import *


wait=WebDriverWait(driver,10)
def searchaddproduct(productsearch,validproduct):
    driver.find_element(By.CSS_SELECTOR,".modal__toggle-open").click()
    driver.find_element(By.XPATH,"//input[@id='Search-In-Modal']").send_keys(productsearch)
    products=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div/ul[@id='predictive-search-results-products-list']/li/a")))
    print(len(products))
    for product in products:
        if product.text==validproduct:
            print(product.text)
            product.click()
            break


def go_to_cart():
    cart=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[name='add']"))).click()

def cart_value_verification(validproduct):
    cart_value=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"cart-item__name")))
    if cart_value.text==validproduct:
        return print("item added to cart",validproduct)
