from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.add_argument('--headless')
service = Service('./chrome/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)


try:
    driver.get('https://www.olx.ua/d/uk/transport')
    driver.maximize_window()
    #Get number of pages
    num_of_pages = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/li[5]/a')
    num_of_pages = int(num_of_pages.text)
    print(num_of_pages)
    for page in range(2, num_of_pages+1):
        announcements = driver.find_elements(By.CLASS_NAME, "css-rc5s2u")
        driver.implicitly_wait(5)
        with open('links.txt', 'a') as f:
            for url in announcements:
                f.write(url.get_attribute('href') + '\n')
        driver.get(f'https://www.olx.ua/d/uk/transport/?page={page}')
        
except Exception as Err:
    print(f"Error: {Err}")
finally:
    driver.quit()


