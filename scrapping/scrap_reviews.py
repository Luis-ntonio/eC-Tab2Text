import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import multiprocessing as mp
import json
import time
import os

with open('urls/reviews_urls.json', 'r') as f:
    pages = json.load(f)

def scrape_page(page):
    reviews_ = []
    returns = {page: {}}
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(page)
        reviews = driver.find_elements(By.ID, 'quickreview')

        if reviews:
            read_more = driver.find_elements(By.XPATH, '//div/div/div/div/div/label')
            if read_more:
                read_more[0].click()
                time.sleep(2)
                reviews = driver.find_elements(By.ID, 'quickreview')
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
    with open('products/products_reviews.json', 'w') as f:
        json.dump(results, f)