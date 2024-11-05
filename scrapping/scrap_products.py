import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import multiprocessing as mp
import json
import time
import os

with open('urls/urls.json', 'r') as f:
    pages = json.load(f)

def scrape_page(page):
    keys_specifications_ = []
    full_specifications_ = []
    reviews_ = []
    returns = {page: {}}
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(page)
        keys_specifications = driver.find_elements(By.CLASS_NAME, 'prd-info')
        full_specifications = driver.find_elements(By.ID, 'specificationsTab')
        reviews = driver.find_elements(By.ID, 'quickreview')

        if keys_specifications:
            keys_specifications_.append(keys_specifications[0].text)
            returns[page]['keys_specifications'] = keys_specifications_
        if full_specifications:
            full_specifications_.append(full_specifications[0].text)
            returns[page]['full_specifications'] = full_specifications_
        if reviews:
            reviews_.append(reviews[0].text)
            returns[page]['reviews'] = reviews_
        


    finally:
        driver.close()
        driver.quit()
        time.sleep(3)
    return returns

if __name__ == '__main__':
    with mp.Pool(8) as p:
        results = p.map(scrape_page, pages)

    if not os.path.exists('products'):
        os.makedirs('products')
        with open('products/products.json', 'w') as f:
            json.dump(results, f)