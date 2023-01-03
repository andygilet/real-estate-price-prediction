from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import numpy as np
import time

def change_page(driver : webdriver.Firefox, page : int, buy_type : str, postal_code : int) -> bool:
    try:
        driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/{buy_type}/liege/{postal_code}?countries=BE&page={page}&orderBy=relevance")
        if driver.title != "House for sale - Immoweb":
            raise Exception("Last page attain !")
    except Exception as e:
        print(e)
        return False
    time.sleep(0.5)
    return True
    
def try_cookie(driver : webdriver.Firefox):
    try:
        coockie_button = driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]')
        coockie_button.click()
    except:
        pass
    
def get_property_urls(driver : webdriver.Firefox, urls : list):
    articles_found = driver.find_elements(By.CLASS_NAME, "card__title-link")
    for article in articles_found:
        url = article.get_attribute("href")
        if url not in urls:
            urls.append(url)
            print(url)

def create_csv_file(urls : list):
    try:
        np.savetxt("links.csv", 
               urls,
               delimiter =", ", 
               fmt ='% s')
    except:
        print("Unable to create the CSV file !")
    
def get_urls() -> list:
    continue_loop : bool = True
    page = 1
    urls = []
    buy_types = ["for-sale","for-rent"]
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    while continue_loop:
        continue_loop = change_page(driver, page, "for-sale")
        if continue_loop:
            try_cookie(driver)
            print(f"page {page}")
            get_property_urls(driver, urls)
            page += 1
    page = 1
    while continue_loop:
        continue_loop = change_page(driver, page, "for-rent")
        if continue_loop:
            try_cookie(driver)
            print(f"page {page}")
            get_property_urls(driver, urls)
            page += 1
    
    print(f"You have {len(urls)} properties !")
    create_csv_file(urls)
    return urls