
from selenium.webdriver.common.by import By
from utils import driver
    
driver=driver.chrome_driver()
def logintopage(password):
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    





