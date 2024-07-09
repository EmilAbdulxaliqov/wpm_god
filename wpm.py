#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get('https://monkeytype.com/')

time.sleep(3)

while True:
    words = driver.find_elements(By.XPATH, '/html/body/div[10]/main/div/div[3]/div[7]/div[4]/div')
    print(len(words))
    count = len(words)
    
    for i in range(len(words)):
        if 'active' in words[i].get_attribute('class'):
            active_idx = i
            break

    words = words[active_idx:]

    for word in words:
        count -= 1
        letters = ''
        chars = word.find_elements(By.XPATH, './letter')
        for char in chars:
            letters += char.text
        letters += " "
        ActionChains(driver).send_keys(letters).perform()
        time.sleep(0.1)
    
