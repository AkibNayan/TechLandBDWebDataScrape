from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import pandas as pd

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

data = []
with open('techLaptopUrls.txt', 'r') as file:
    for line in file:
        driver.get(line.strip())
        time.sleep(2)
        
        title = driver.find_element('xpath', '//div[@class="title page-title"]').text
        #print(title)
        productDetails = driver.find_elements(
            'xpath', '//table[@class="table table-bordered"]//tr//td')
        count = 1
        for index, product in enumerate(productDetails, start=1):
            if count > 20:
                break
            sys.stdout.reconfigure(encoding='utf-8')
            if product.text == 'Product Price':
                product_price = driver.find_element(
                    'xpath', f'(//table[@class="table table-bordered"]//tr//td)[{index+1}]').text
                #print(product_price)
            elif product.text == "Special Price":
                special_price = driver.find_element(
                    'xpath', f'(//table[@class="table table-bordered"]//tr//td)[{index+1}]').text
                #print(special_price)
            elif product.text == "Stock Status":
                stock_status = driver.find_element(
                    'xpath', f'(//table[@class="table table-bordered"]//tr//td)[{index+1}]').text
                #print(stock_status)
            elif product.text == "Brand":
                brand = driver.find_element(
                    'xpath', f'(//table[@class="table table-bordered"]//tr//td)[{index+1}]').text
                #print(brand)
            elif product.text == "Product Model":
                product_model = driver.find_element(
                    'xpath', f'(//table[@class="table table-bordered"]//tr//td)[{index+1}]').text
                #print(product_model)
            elif product.text == "Warranty":
                warranty = driver.find_element(
                    'xpath', f'(//table[@class="table table-bordered"]//tr//td)[{index+1}]').text
                #print(warranty)
            count += 1
        short_description = driver.find_elements(
            'xpath', '//div[@class="block-content  block-short_description"]//li')
        short_des = []
        for des in short_description:
            short_des.append(des.text)
        #print(short_des)
        long_description = driver.find_elements(
            'xpath', '//td[@class="attribute-name"]')
        for index, long_desc in enumerate(long_description, start=1):
            if long_desc.text == "Chipset":
                chipset = driver.find_element(
                    'xpath', f'(//td[@class="attribute-value"])[{index}]').text
            elif long_desc.text == "Memory":
                memory = driver.find_element(
                    'xpath', f'(//td[@class="attribute-value"])[{index}]').text
            elif long_desc.text == "Storage":
                storage = driver.find_element(
                    'xpath', f'(//td[@class="attribute-value"])[{index}]').text
            elif long_desc.text == "Battery":
                battery = driver.find_element(
                    'xpath', f'(//td[@class="attribute-value"])[{index}]').text
            elif long_desc.text == "Operating System":
                operating_system = driver.find_element(
                    'xpath', f'(//td[@class="attribute-value"])[{index}]').text
            elif long_desc.text == "Color":
                color = driver.find_element(
                    'xpath', f'(//td[@class="attribute-value"])[{index}]').text
        #print(color)
        dict_ = {
            "title": title,
            "product_price": product_price,
            "special_price": special_price,
            "stock_status": stock_status,
            "brand": brand,
            "product_model": product_model,
            "warranty": warranty,
            "short_description": short_des,
            "chipset": chipset,
            "memory": memory,
            "storage": storage,
            "battery": battery,
            "operating_system": operating_system,
            "color": color
        }
        #print(dict_)
        data.append(dict_)
        #break
#print(data)
df = pd.DataFrame(data)
df.to_csv('techLandBDLaptopDataSelenium.csv', index=False)