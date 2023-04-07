from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://lms.ou.edu.vn/')
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, 'main-btn').click()
driver.find_element(By.CLASS_NAME, 'login100-form-btn').click()
user_type=Select(driver.find_element(By.ID,'form-usertype'))
user_type.select_by_index(0)

username = driver.find_element(By.ID, 'form-username')
username.send_keys('2051052090')
password = driver.find_element(By.ID, 'form-password')
password.send_keys('231455070')

driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn').click()
title = WebDriverWait(driver,10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.dashboard-card-deck span.multiline'))
)
# driver.implicitly_wait(10)
# title = driver.find_elements(By.CSS_SELECTOR, '.dashboard-card-deck span.multiline')
for i in title:
    print(i.text)

driver.quit()
