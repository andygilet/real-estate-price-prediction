import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

def analyze_url(url : str) -> list:
    data = []
    try:
        if len(url) == 0:
            raise Exception("ERROR : Url entered is empty !")
        splitted_url = url.split('/')
        if len(splitted_url) != 10:
            raise Exception("ERROR : url format incorrect !")
        if(splitted_url[5] != "new-real-estate-project-houses" and
        splitted_url[5] != "new-real-estate-project-apartments"):
            data.append(splitted_url[5])
            data.append(splitted_url[6])
            data.append(splitted_url[7])
            data.append(splitted_url[8])
    except Exception as e:
        print(e)
    return data

def Create_soup(url : str) -> BeautifulSoup:
    try:
        page = requests.get(url)
        if page.status_code != 200:
            raise Exception("Error : Unable to load the content of the page correctly !")
        return BeautifulSoup(page.content, 'html.parser')
    except Exception as e:
        print(e)
        return None
        

def get_data_from_table_data(soup : BeautifulSoup) -> list:
    #get the data we need from the class 'classified-table_data' (wich are the data)
    info = soup.find_all(class_ = 'classified-table__data')
    info_utf8 = str(info).encode('utf-8')
    return str(info_utf8).split('<td class="classified-table__data"')

def get_data_from_table_header(soup) -> list:
    #get the data we need from the class 'classified-table_header (wich is the description)
    info = soup.find_all(class_ = 'classified-table__header')
    info_utf8 = str(info).encode('utf-8')
    return str(info_utf8).split('<th class="classified-table__header" scope="row">')

def get_bedrooms(soup : BeautifulSoup) -> str:
    for elem in soup.find_all("p", attrs={"class": "classified__information--property"}):
        temp = elem.text
        temp = temp.replace("\n", '')
        temp = temp.replace(" ", '')
        result += temp
        new_result = result.split("|")
        try :
            bedroom = re.sub("[^0-9]", "", new_result[0])
        except : 
            bedroom = 'None'
    return bedroom

def get_size_of_house(soup : BeautifulSoup) -> str:
    for elem in soup.find_all("p", attrs={"class": "classified__information--property"}):
        temp = elem.text
        temp = temp.replace("\n", '')
        temp = temp.replace(" ", '')
        result += temp
        new_result = result.split("|")
        try :
            size_of_house = re.sub("[^0-9]", "", new_result[1])
        except : 
            size_of_house = 'None'
    return size_of_house

def get_price(soup : BeautifulSoup) -> str:
    try:
        for elem in soup.find_all("p", attrs={"class": "classified__price"}):
            for prices in elem.find_all("span", attrs={"class": "sr-only"}):
                price =  re.sub(r'[^\d]', '', str(prices))
        if len(price) == 0:
            price = "P.O.R"
    except Exception as e:
        print(e)
        return None
    return price

def create_dictionnary(url_info : list, bedrooms : str, size_of_house : str, price : str) -> dict:
    return {'property_type' : url_info[0],
            'sale_type' : url_info[1],
            'locality' : url_info[2],
            'bedroom' : bedrooms,
            'size_of_house' : size_of_house,
            'Price' : price}

def remove_html_tags(s):
    new_s = re.sub('\s+', ' ', s)
    return re.sub("<[^<]+?>", "", new_s)

def data_cleaner(the_dic : dict, info_list : list, description_list : list) -> dict:
    for description,data in zip(description_list[1:],info_list[1:]) :
        the_dic[remove_html_tags(description)] = remove_html_tags(data)
        
def get_data_from_url(url : str) :
    #get the data from the url
    url_info = analyze_url(url)
    if url_info == []:
        return
    soup = Create_soup(url)
    if soup == None:
        return
    
    info_list = get_data_from_table_data(soup)
    description_list = get_data_from_table_header(soup)
    bedroom = get_bedrooms(soup)
    size_of_house = get_size_of_house(soup)
    price = get_price(soup)
    the_dic = create_dictionnary(url_info, bedroom, size_of_house, price)
    
    return data_cleaner(the_dic, info_list, description_list)

    
def data_to_pandas(data_dic,data_frame) :
    '''
    Parameters:
    data_dic (dict): A dictionary containing the key-value pairs to be added to the dataframe.
    data_frame (pandas.DataFrame): The dataframe to which the key-value pairs from `data_dic` will be added.
    
    Returns:
    pandas.DataFrame: The modified dataframe with the key-value pairs from `data_dic` added.
    '''
    #Adding the none in the list of the key that doesn't match
    len_items = False
    if len(data_frame) > 0 : 
        for key,value in data_frame.items() :
            len_items = len(data_frame[key])
            if key not in data_dic :
                data_frame[key].append('None')
    #Adding the value in the dic, if the key doesn't exist, create a list with x * none at the beginning    
    for key,value in data_dic.items() :
        if key in data_frame :
            data_frame[key].append(value)
        else : 
            data_frame[key] = []
            if len_items : 
                for _ in range(len_items) :
                    data_frame[key].append('None')
            data_frame[key].append(value)
    
    return data_frame