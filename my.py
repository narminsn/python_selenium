import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import math

from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd




data = pd.read_excel (r'Öğrenciler - Bursa Uludağ Üniversitesi.xlsx',) 
df = pd.DataFrame(data, columns= ['Öğrenci No'])

# print(df)
codes = []
x = float('nan')
for row in df.iterrows():
    if str(type(row[1][0])) == "<class 'str'>":
        # if not math.isnan(row[1][0]):

        codes.append(row[1][0])
    elif str(type(row[1][0])) == "<class 'int'>":
        codes.append(row[1][0])







driver = webdriver.Firefox(executable_path='./geckodriver')



driver.set_window_size(900,900)
# codes = ['17998827','17211454','16AB90594']
result = []
for field in codes:
    try:

        driver.get("https://yos.uludag.edu.tr/sonuc/")
        driver.find_element_by_name('ctl00$cphC$txtIdentty').send_keys(field)


        python_button = driver.find_element_by_name("ctl00$cphC$btnSorgula")
        python_button.click()

        my_button = driver.find_element(By.XPATH, '//a[text()="SINAV SONUÇ BELGESİ"]')
        my_button.click()
        my_name = driver.find_elements_by_tag_name('td')[8].text
        my_surname = driver.find_elements_by_tag_name('td')[10].text
        my_td = driver.find_elements_by_tag_name('td')[-1].text
        result.append([f"{my_name} {my_surname}",my_td]) 
    # {'full_name':f"{my_name} {my_surname}",'score':my_td}
    
        time.sleep(2)
    except:
        pass
    
df = pd.DataFrame(result, columns = ['Ad Soyad', 'Bal'])

df.to_excel (r'my.xlsx', index = False, header=True)

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()