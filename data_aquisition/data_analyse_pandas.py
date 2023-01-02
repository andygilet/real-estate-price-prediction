import requests
from bs4 import BeautifulSoup
import re
def remove_html_tags(s):
    new_s = re.sub('\s+', ' ', s)
    return re.sub("<[^<]+?>", "", new_s)
def get_data_from_url(url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #get the data we need from the class 'classified-table_data
    info = soup.find_all(class_ = 'classified-table__data')
    info_utf8 = str(info).encode('utf-8')
    info_list = str(info_utf8).split('<td class="classified-table__data"')
    #Clean the data
    clean_data = []
    for elem in info_list :
        clean_data.append(remove_html_tags(elem))
    print(clean_data[1:])
    #return the data cleaned
    return clean_data[1:]

def data_to_pandas(data) :
    pass

get_data_from_url('https://www.immoweb.be/en/classified/apartment/for-sale/schaerbeek/1030/10303386')