from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://vnexpress.net/')

el = driver.find_elements(By.CSS_SELECTOR, '#automation_TV0 article.item-news')
for q in el:
    try:
        title = q.find_element(By.CLASS_NAME, 'title-news').text
        des = q.find_element(By.CLASS_NAME, 'description').text
        img = q.find_element(By.CSS_SELECTOR, '.thumb-art img').get_attribute('src')
    except:
        pass
    else:
        print(title)
        print(des)
        print(img)
        print('=======')

driver.execute_script("window.scrollTo(0, 500)")
driver.save_screenshot('vnexpress.png')
driver.quit()