from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import numpy as np
import time

def change_page(driver : webdriver.Firefox, page : int, buy_type : str, province : str) -> bool:
    try:
        driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/{buy_type}/{province}/province?countries=BE&page={page}&orderBy=relevance")
        if province == "antwerp" and driver.title != "House and apartment for sale - Antwerp (Province) - Immoweb":
            raise Exception("Last page attain - Antwerp !")
        elif province == "limburg" and driver.title != "House and apartment for sale - Limburg (Province) - Immoweb":
            raise Exception("Last page attain - Limburg !")
        elif province == "east-flanders" and driver.title != "House and apartment for sale - East Flanders (Province) - Immoweb":
            raise Exception("Last page attain - East-Flanders !")
        elif province == "flemish-brabant" and driver.title != "House and apartment for sale - Flemish Brabant (Province) - Immoweb":
            raise Exception("Last page attain - Flemish-Brabant !")
        elif province == "west-flanders" and driver.title != "House and apartment for sale - West Flanders (Province) - Immoweb":
            raise Exception("Last page attain - West-Flanders !")
        elif province == "walloon-brabant" and driver.title != "House and apartment for sale - Walloon Brabant (Province) - Immoweb":
            raise Exception("Last page attain - Walloon-Brabant !")
        elif province == "hainaut" and driver.title != "House and apartment for sale - Hainaut (Province) - Immoweb":
            raise Exception("Last page attain - Hainaut !")
        elif province == "liege" and driver.title != "House and apartment for sale - Liège (Province) - Immoweb":
            raise Exception("Last page attain - Liège !")
        elif province == "luxembourg" and driver.title != "House and apartment for sale - Luxembourg (Province) - Immoweb":
            raise Exception("Last page attain - Luxembourg !")
        elif province == "namur" and driver.title != "House and apartment for sale - Namur (Province) - Immoweb":
            raise Exception("Last page attain - Namur !")
        elif province == "brussels" and driver.title != "House and apartment for sale - Brussels (Province) - Immoweb":
            raise Exception("Last page attain - Brussels !")
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
            driver = webdriver.Firefox()
            
    print(f"You have {len(urls)} properties !")
    create_csv_file(urls)
    return urls