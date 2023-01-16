import pandas as pd

def remove_empty_space(dataframe : pd.DataFrame):
    for i in range(len(dataframe)):
        for j in range(len(dataframe.columns)):
            dataframe.iloc[i][j] = str(dataframe.iloc[i][j]).strip()
                
def error_managment(dataframe : pd.DataFrame):
    for i in range(len(dataframe)):
        for j in range(len(dataframe.columns)):
            if dataframe.iloc[i][j] == "" or dataframe.iloc[i][j] == "NaN":
                dataframe.iloc[i][j] = "None" 
    dataframe.isnull().sum()

def cleaning():
    dataframe = pd.read_csv("./immo_data.csv")
    remove_empty_space(dataframe)
    error_managment(dataframe)