import pandas as pd
from pandas_ods_reader import read_ods
import seaborn as sns
from statistics import median
import matplotlib.pyplot as plt

def create_graph_price_difference_renovated(dataFrame : pd.DataFrame):
    """_summary_

    Args:
        dataFrame (pd.DataFrame): _description_
    
    Description:
        This function create the graph for the question :
        In which province is it more beneficial to renovate properties?
    """
    sns.catplot(data= dataFrame, kind="bar", x="Provinces", y="Price", hue="Status")
    plt.title("Comparison between the median price of new or renovated properties to to be renovated properties")
    plt.xlabel("Provinces")
    plt.xticks(rotation=45)
    plt.ylabel("Prices(€)")
    plt.show()
    
def create_graph_compare_price_crime_rates(dataFrame : pd.DataFrame):
    """_summary_

    Args:
        dataFrame (pd.DataFrame): _description_
        
    Description:
        This function create the graph for the question :
        Is the crimes rates of a province in Belgium influancing the price of the properties in that province ?
    """
    sns.scatterplot(x="Crimes Rates", y="Price", data=dataFrame)
    plt.title("Median price of properties by provinces compare to the crime rates")
    plt.xlabel("Crimes Rates (for 10 000 habitants)")
    plt.ylabel("Prices(€)")
    plt.show()
    
def transform_locality_to_provinces(postal_code : str) -> str:
    """_summary_

    Args:
        postal_code (str): _description_

    Returns:
        str: _description_
        
    Description:
        This function take a postal code and return the province in belgium it belongs to
    """
    temp = int(postal_code)
    if temp >= 1000 and temp <= 1299:
        return "Bruxelles"
    elif temp >= 1300 and temp <= 1499:
        return "Brabant wallon"
    elif (temp >= 1500 and temp <= 1999) or (temp >= 3000 and temp <= 3499):
        return "Brabant flamand"
    elif temp >= 2000 and temp <= 2999:
        return "Anvers"
    elif temp >= 3500 and temp <= 3999:
        return "Limbourg"
    elif temp >= 4000 and temp <= 4999:
        return "Liege"
    elif temp >= 5000 and temp <= 5680:
        return "Namur"
    elif (temp >= 6000 and temp <= 6599) or (temp >= 7000 and temp <= 7999):
        return "Hainaut"
    elif temp >= 6600 and temp <= 6999:
        return "Luxembourg"
    elif temp >= 8000 and temp <= 8999:
        return "Flandre occidentale"
    elif temp >= 9000 and temp <= 9999:
        return "Flandre orientale"
    else:
        return "Error"
    
def create_dataset_price_difference_renovated(dataFrame : pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        dataFrame (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
        
    Description:
        This function take the brut dataset of immoweb to return a new dataset that can be used to answer the question : 
        In which province is it more beneficial to renovate properties?
    """
    new_dataFrame = pd.DataFrame()

    type_property = []
    locality = []
    price = []
    building_state = []
    
    provinces = ["Bruxelles", "Anvers", "Limbourg",
                 "Flandre orientale", "Brabant flamand",
                 "Flandre occidentale", "Brabant wallon",
                 "Hainaut", "Liege", "Luxembourg", "Namur"]
    
    provinces_to_renovate_price_list =[[], [], [], [], [], [], [], [], [], [], []]
    provinces_renovated_price_list =[[], [], [], [], [], [], [], [], [], [], []]
    
    for key, value in dataFrame.items():
        if key == "Type_property":
            type_property = value
        elif key == "locality":
            locality = value
        elif key == "Price":
            price = value
        elif key == "building_state":
            building_state = value
    
    for i in range(len(locality)):
        if type_property[i] == "house" or type_property[i] == "country-cottage" or type_property[i] == "villa" or type_property[i] == "chalet" or type_property[i] == "town-house" or type_property[i] == "loft" or type_property[i] == "pavilion":
            province = transform_locality_to_provinces(locality[i])
            if building_state[i] == "As new" or building_state[i] == "Good" or building_state[i] == "Just renovated":
                for j in range(len(provinces)):
                    if province == provinces[j]:
                        provinces_renovated_price_list[j].append(price[i])
            elif building_state[i] == "To restore" or building_state[i] == "To be done up" or building_state[i] == "To renovate":
                for j in range(len(provinces)):
                    if province == provinces[j]:
                        provinces_to_renovate_price_list[j].append(price[i])

    for i in range(len(provinces)):
        new_row1 = pd.Series({"Provinces" : provinces[i], "Price" : median(provinces_to_renovate_price_list[i]), "Status" : "To be renovated"})
        new_row2 =pd.Series({"Provinces" : provinces[i], "Price" : median(provinces_renovated_price_list[i]), "Status" : "Renovated or new"})
        new_dataFrame = pd.concat([new_dataFrame, new_row1.to_frame().T], ignore_index=True)
        new_dataFrame = pd.concat([new_dataFrame, new_row2.to_frame().T], ignore_index=True)
        
    return new_dataFrame

def immoweb_median_price(immoweb_data : pd.DataFrame) -> list:
    """_summary_

    Args:
        immoweb_data (pd.DataFrame): _description_

    Returns:
        list: _description_
        
    Description:
        This function returns a list containing the median price of the properties on each province in belgium.
    """
    locality = []
    price = []
    type_property = []
    building_state = []
    provinces_price_list =[[], [], [], [], [], [], [], [], [], [], []]
    return_list = []
    provinces = ["Bruxelles", "Anvers", "Limbourg",
                 "Flandre orientale", "Brabant flamand",
                 "Flandre occidentale", "Brabant wallon",
                 "Hainaut", "Liege", "Luxembourg", "Namur"]
    
    for key, value in immoweb_data.items():
        if key == "locality":
            locality = value
        elif key == "Price":
            price = value
        elif key == "Type_property":
            type_property = value
        elif key == "building_state":
            building_state = value
            
    for i in range(len(locality)):
        if type_property[i] == "house" or type_property[i] == "country-cottage" or type_property[i] == "villa" or type_property[i] == "chalet" or type_property[i] == "town-house" or type_property[i] == "loft" or type_property[i] == "pavilion":
            if building_state[i] == "As new" or building_state[i] == "Good" or building_state[i] == "Just renovated":
                province = transform_locality_to_provinces(locality[i])
                for j in range(len(provinces)):
                    if province == provinces[j]:
                        provinces_price_list[j].append(price[i])
    
    for i in range(len(provinces_price_list)):
        return_list.append(median(provinces_price_list[i]))

    return return_list
                
            
def create_dataset_compare_price_crime_rates(immoweb_data : pd.DataFrame, demography_data : pd.DataFrame, crimes_data : pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        immoweb_data (pd.DataFrame): _description_
        demography_data (pd.DataFrame): _description_
        crimes_data (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
        
    Description:
        This function take the brut dataset of immoweb, the demography in belgium, and the crimes in belgium
        to return a new dataset that can be used to answer the question : 
        Is the crimes rates of a province in Belgium influancing the price of the properties in that province ?
    """
    new_dataFrame = pd.DataFrame()
    provinces = []
    habitants = []
    total_crimes = []
    mediane_prices = []
    
    for key, value in demography_data.items():
        if key == "Provinces":
            provinces = value
        elif key == "Habitants":
            habitants = value
    
    for key, value in crimes_data.items():
        if key == "Total":
            total_crimes = value
    
    mediane_prices = immoweb_median_price(immoweb_data)
    
    for i in range(len(provinces)):
        new_row = pd.Series({"Provinces" : provinces[i], "Price" : int(mediane_prices[i]), "Crimes Rates" : int(float(total_crimes[i]) / habitants[i] * 10000)})
        new_dataFrame = pd.concat([new_dataFrame, new_row.to_frame().T], ignore_index=True)
        
    return new_dataFrame

def create_graph(price_renovated_dataframe : pd.DataFrame, price_crime_rate : pd.DataFrame):
    """_summary_

    Args:
        price_renovated_dataframe (pd.DataFrame): _description_
        price_crime_rate (pd.DataFrame): _description_
        
    Description : 
        Call the functions that creates the plots and show them in a window.
    """
    create_graph_price_difference_renovated(price_renovated_dataframe)
    create_graph_compare_price_crime_rates(price_crime_rate)
    plt.show()

def immoweb_data_to_graph():
    """_summary_
    
        Description : 
            The function to call to generate the plots for my two questions : Is the crimes rates of a province in Belgium influancing the price of the properties
            in that province ? And in which province is it more beneficial to renovate properties?
            For that i've imported two more dataset, one on the criminality in belgium in 2021 and another one about the demography in belgium.
    """
    immoweb_dataframe = pd.read_csv(".\immo_data.csv")
    crime_dataframe = read_ods(".\criminality_belgium_2021.ods")
    demography_belgium = read_ods(".\demographie_belgique_2021.ods")
    
    price_renovated_dataframe = create_dataset_price_difference_renovated(immoweb_dataframe)
    price_crime_rate = create_dataset_compare_price_crime_rates(immoweb_dataframe, demography_belgium, crime_dataframe)
    create_graph(price_renovated_dataframe, price_crime_rate)
    

immoweb_data_to_graph()