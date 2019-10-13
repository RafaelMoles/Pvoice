from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/home/user/Documentos/HackUPC/chromedriver')

browser.get('http://192.168.137.251') 

inputUser = browser.find_element_by_id('login-user')

inputUser.send_keys('Hacker')

inputUser = browser.find_element_by_id('login-password')

inputUser.send_keys('pepe')

loginButton = browser.find_element_by_id('login-button')

loginButton.click()

miniButton = browser.find_element_by_css_selector("div[title*='Slice']")

miniButton.click()
