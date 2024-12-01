import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import multiprocessing as mp
import json
import os

pages = [x for x in range(1, 214)]

def scrape_page(page):
    urls = []
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(f'https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india?page={page}')
        products = driver.find_element(By.ID, 'productsCnt')
        urls_ = products.find_elements(By.XPATH, '//div/div/div/div/div/div/h2/a')
        urls.extend([url.get_attribute('href') for url in urls_])
    finally:
        driver.close()
        driver.quit()
    
    return urls

if __name__ == '__main__':
    with mp.Pool(4) as p:
        results = p.map(scrape_page, pages)
    
    urls = [url for sublist in results for url in sublist]
    if not os.path.exists('urls'):
        os.makedirs('urls')
    with open('urls/urls.json', 'w') as f:
        json.dump(urls, f)