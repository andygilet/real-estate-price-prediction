import requests
from bs4 import BeautifulSoup
def get_data_from_url(url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Create a list with the data we need, that can be found in the class 'classified-table_data'
    info = soup.find_all(class_ = 'classified-table__data')
    info_utf8 = str(info).encode('utf-8')
    info_list = str(info_utf8).split('<td class="classified-table__data"')
    #clean the data
    pass
    #return the cleaned data
    pass

    '''
    Date de dispo
    Quartier
    Annee construction
    Etage
    Nombre etage
    Etat batiment
    Nombre de facade

    A continuer
    '''
def do_a_csv(data) :
    #do a barr ... do a csv
    pass