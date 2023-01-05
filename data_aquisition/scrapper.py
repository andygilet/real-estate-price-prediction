from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from scrapper_thread import link_scrapper
from threading import Thread
from threading import RLock
    
def get_urls_from_scrapper():
    link_scrappers = list()
    rlock_csv = RLock()
    rlock_printer = RLock()
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
    
    create_empty_file = open(".\links.csv", "w")
    create_empty_file.close()
    
    for province in provinces:
        thread = Thread(target= link_scrapper, args=(province, rlock_csv, rlock_printer,))
        link_scrappers.append(thread)
    for thread in link_scrappers:
        thread.start()
    for thread in link_scrappers:
        thread.join()