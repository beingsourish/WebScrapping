from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://github.com/')
driver.maximize_window()
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
user_id = driver.find_element(By.ID, "login_field")
user_id.send_keys("sourishsmile@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("Kolkata@98746")
password.submit()
assert "beingsourish" in driver.page_source
input("Press Enter to close the browser...")
driver.quit()