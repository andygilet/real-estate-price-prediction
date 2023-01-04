from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import numpy as np

def try_find_out_of_index(driver : webdriver.Firefox, page : int) -> bool:
    try:
        if len(driver.find_elements(By.CLASS_NAME, "pagination__item")) == 0:
            return True
        else:
            return False
    except:
        print("ERROR : Unable to check the page !")
        return False

def change_page(driver : webdriver.Firefox, page : int, buy_type : str, province : str) -> bool:
    try:
        driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/{buy_type}/{province}/province?countries=BE&page={page}&orderBy=relevance")
        if try_find_out_of_index(driver, page):
            raise Exception(f"Last page attain : {province} !")
    except Exception as e:
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
    buy_types = ["for-sale",
                 "for-rent"]
    provinces = ["antwerp",
                 "limburg",
                 "east-flanders",
                 "flemish-brabant",
                 "west-flanders",
                 "walloon-brabant",
                 "hainaut",
                 "liege",
                 "luxembourg",
                 "namur",
                 "brussels"]
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(0.5)
    
    for province in provinces:
        for buy_type in buy_types:
            while continue_loop:
                continue_loop = change_page(driver, page, buy_type, province)
                if continue_loop:
                    try_cookie(driver)
                    print(f"page {page}")
                    get_property_urls(driver, urls)
                    page += 1
            page = 1
            driver.close()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            driver.implicitly_wait(0.5)
            continue_loop = True
            
    print(f"You have {len(urls)} properties !")
    create_csv_file(urls)
    return urls