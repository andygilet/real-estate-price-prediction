from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from threading import RLock
import csv

def try_find_out_of_index(driver : webdriver.Firefox, rlock_printer : RLock) -> bool:
    try:
        if len(driver.find_elements(By.CLASS_NAME, "pagination__item")) == 0:
            return True
        else:
            return False
    except:
        with rlock_printer:
            print("ERROR : Unable to check the page !")
        return False

def change_page(driver : webdriver.Firefox, page : int, buy_type : str, province : str, rlock_printer : RLock) -> bool:
    try:
        driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/{buy_type}/{province}/province?countries=BE&page={page}&orderBy=relevance")
        if try_find_out_of_index(driver, rlock_printer):
            raise Exception(f"Last page attain : {province} !")
    except Exception as e:
        with rlock_printer:
            print(e)
        return False
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

def link_scrapper(province : str, rlock_csv : RLock, rlock_printer : RLock):
    continue_loop : bool = True
    page = 1
    buy_types = ["for-sale",
                 "for-rent"]
    urls = []
    for buy_type in buy_types:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.implicitly_wait(0.5)
        while continue_loop:
            continue_loop = change_page(driver, page, buy_type, province, rlock_printer)
            if continue_loop:
                try_cookie(driver)
                get_property_urls(driver, urls)
                with rlock_printer:
                    print(f"link scrapper {province} : {buy_type} : page {page}")
                with rlock_csv:
                    with open('.\links.csv', 'a') as links:
                        writer = csv.writer(links)
                        for url in urls:
                            writer.writerow(url)
                page += 1
        page = 1
        driver.close()
        continue_loop = True