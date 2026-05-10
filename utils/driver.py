
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def chrome_driver():
    service_obj= Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://adnabu-store-assignment1.myshopify.com/")
    driver.maximize_window()
    return driver

