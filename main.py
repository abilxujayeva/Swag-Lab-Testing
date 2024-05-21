from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
web_driver.maximize_window()
web_driver.get("https://www.saucedemo.com/")
web_driver.implicitly_wait(10)


"""Swag Lab testing"""
username = "performance_glitch_user"
password = "secret_sauce"
element = web_driver.find_element(By.XPATH, "//div[starts-with(text(),'Swag')]")
assert "Swag Labs" in element.text, "page did not open"
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'user')]").send_keys(username)
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'pass')]").send_keys(password)
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'login')]").click()
element = web_driver.find_element(By.XPATH, "//span[starts-with(text(), 'Pro')]")
assert "Products" in element.text, "page did not open"
web_driver.find_element(By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']").click()
web_driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
web_driver.find_element(By.XPATH, "//button[starts-with(@id, 'check')]").click()
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'first')]").send_keys("fatimaxon")
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'last')]").send_keys("abilxujayeva")
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'postal')]").send_keys("150100")
web_driver.find_element(By.XPATH, "//input[starts-with(@id, 'con')]").click()
web_driver.find_element(By.XPATH, "//button[starts-with(@id, 'fin')]").click()
web_driver.find_element(By.XPATH, "//button[starts-with(@id, 'back')]").click()