import pandas as pd
import numpy as np

def remove_empty_cells_in_df(df : pd.DataFrame) -> pd.DataFrame:
    return df.fillna("None")

def remove_str_data(data : pd.DataFrame) -> pd.DataFrame:
    df = data
    
    house_dict = {"house": 1,
                  "apartment" : 2,
                  "villa" : 3,
                  "apartment-block": 4,
                  "duplex" : 5,
                  "ground-floor" : 6,
                  "mixed-use-building" : 7,
                  "penthouse" : 8,
                  "exceptional-property" : 9,
                  "flat-studio" : 10,
                  "mansion" : 11,
                  "service-flat" : 12,
                  "town-house" : 13,
                  "loft" : 14,
                  "bungalow" : 15,
                  "country-cottage" : 16,
                  "triplex" : 17,
                  "chalet" : 18,
                  "manor-house" : 19,
                  "kot" : 20,
                  "other-property" : 21,
                  "None" : 21,
                  "farmhouse" : 22,
                  "castle" : 23,
                  "pavilion" : 24}
    
    state_dict = {"Good" : 1,
                  "As new" : 2,
                  "To renovate" : 3,
                  "To be done up" : 4,
                  "Just renovated" : 5,
                  "To restore" : 6,
                  "None" : "None"}
    
    df.drop(["Sale_type",
             "surface_land",
             "surface_area_plot"], axis="columns", inplace=True)
    
    df = df.loc[df["facades_number"] != "None"]
    df = df.loc[df["building_state"] != "None"]
    
    df.reset_index(drop= True, inplace= True)
    
    for i in range(len(df)):
        df.at[i, "Type_property"] = house_dict[df.at[i, "Type_property"]]
        df.at[i, "building_state"] = state_dict[df.at[i, "building_state"]]
        df.at[i, "Price"] = int(df.at[i, "Price"] / 10000)
        if df.at[i, "fire_place"] == "None":
            df.at[i, "fire_place"] = 0
        if df.at[i, "garden"] == "None":
            df.at[i, "garden"] = 0
        if df.at[i, "fully_equipped_kitchen"] == "None":
            df.at[i, "fully_equipped_kitchen"] = 0
        if df.at[i, "Furnished"] == "None":
            df.at[i, "Furnished"] = 0
        if df.at[i, "Swimming_pool"] == "None":
            df.at[i, "Swimming_pool"] = 0
        if df.at[i, "terrace"] == "None":
            df.at[i, "terrace"] = 0
        if df.at[i, "Number_bedrooms"] == "None":
            df.at[i, "Number_bedrooms"] = 0
        if df.at[i, "Living_area"] == "None":
            df.at[i, "Living_area"] = 0
    
    df = df.loc[df["Price"] < 10000]
            
    df[["locality", "Price", "Type_property", "Number_bedrooms", 
        "Living_area", "fully_equipped_kitchen", "Furnished", "terrace", 
        "garden", "facades_number", "Swimming_pool", "building_state", "fire_place"]] = df[["locality", "Price", "Type_property", "Number_bedrooms", 
                                                                                            "Living_area", "fully_equipped_kitchen", "Furnished", "terrace", 
                                                                                            "garden", "facades_number", "Swimming_pool", "building_state", 
                                                                                            "fire_place"]].astype(int)
    
    return df

def check_data_correlation(df : pd.DataFrame):
    data = pd.DataFrame(list(zip(df.columns.tolist(), [df["Price"].corr(df["locality"]),
                                                       df["Price"].corr(df["Price"]),
                                                       df["Price"].corr(df["Type_property"]),
                                                       df["Price"].corr(df["Number_bedrooms"]),
                                                       df["Price"].corr(df["Living_area"]),
                                                       df["Price"].corr(df["fully_equipped_kitchen"]),
                                                       df["Price"].corr(df["Furnished"]),
                                                       df["Price"].corr(df["terrace"]),
                                                       df["Price"].corr(df["garden"]),
                                                       df["Price"].corr(df["facades_number"]),
                                                       df["Price"].corr(df["Swimming_pool"]),
                                                       df["Price"].corr(df["building_state"]),
                                                       df["Price"].corr(df["fire_place"])])),
                        columns=["Colums", "val"])
    print(data)

def check_data(data : pd.DataFrame) -> pd.DataFrame:
    df = data
    if df.duplicated().any():
        df.drop_duplicates(inplace=True)
    df = remove_empty_cells_in_df(df)
    df = remove_str_data(df)
    #check_data_correlation(df)
    return df

def data_clean_for_price_range() -> list:
    data = pd.read_csv(".\immo_data.csv")
    data = check_data(data)
    target = data["Price"]
    data = data.drop(columns=["Price"])
    return [data, target]