from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
#count = 1
for page in range(1, 14):
    url = f"https://www.techlandbd.com/brand-laptops?limit=100&page={page}"
    driver.get(url)
    time.sleep(2)
    urls = driver.find_elements('xpath', '//div[@class="name"]//a')
    with open('techLaptopUrls.txt', 'a') as file:
        for url_ in urls:
            file.write(url_.get_attribute('href') + '\n')
            #count += 1
#print(count)