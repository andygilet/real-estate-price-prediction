from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from threads import link_scrapper
from threading import Thread
from threading import RLock
import numpy as np
import csv

def create_csv_file(urls : list):
    try:
        np.savetxt("links.csv", 
               urls,
               delimiter =", ", 
               fmt ='% s')
    except:
        print("Unable to create the CSV file !")
    
def get_urls_from_scrapper() -> list:
    urls = []
    link_scrappers = list()
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
    for province in provinces:
        thread = Thread(target= link_scrapper, args=(province,))
        link_scrappers.append(thread)
            
    print(f"You have {len(urls)} properties !")
    create_csv_file(urls)
    return urls
    
def get_urls_from_file() -> list:
    urls = []
    try:
        with open('.\links.csv', 'r') as links_file: 
            reader = csv.reader(links_file)
            for row in reader:
                urls.append(row[1])
    except:
        print("ERROR : no file found to get urls from !")
    return urls