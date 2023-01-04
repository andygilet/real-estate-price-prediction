from data_aquisition.data_analyse_pandas import get_data_from_url, data_to_pandas
from data_aquisition.data_cleaning import reference_dic_needed, clean_escape_characters
import pandas as pd
import csv
import threading
from threading import RLock
import os 
lock = RLock()
def data_to_csv(pass_row) :
    count = 0
    ploted_frame = {}
    with open('links.csv', 'r') as links_file : 
        reader = csv.reader(links_file)
        for i in range(pass_row) :
            next(reader)
        for row in reader :
            the_data = get_data_from_url(row[0])
            ploted_frame = data_to_pandas(the_data,ploted_frame)
            count += 1
            print(f"I'm at {count + pass_row} page done")
            if count == 50 : 
                break
    for key in ploted_frame:
        ploted_frame[key] = [clean_escape_characters(value) for value in ploted_frame[key]]
    ploted_frame = reference_dic_needed(ploted_frame)

    df = pd.DataFrame(ploted_frame)
    
    with lock :
        with open('immo_data.csv','a') as data_file : 
            df.to_csv(data_file, mode='a', header=False)

            
def main() :
    with open('immo_data.csv', 'w') as data_file : 
        data_file.write(',locality,Type_property,Price,Sale_type,Number_bedrooms,Living_area,fully_equipped_kitchen,Furnished,terrace,garden,surface_land,surface_area_plot,facades_number,Swimming_pool,building_state,fire_place\n')
    thread = threading.Thread(target = data_to_csv,args =(0,))
    thread2 = threading.Thread(target = data_to_csv,args =(150,))
    thread.start()
    thread2.start()

    thread.join()
    thread2.join()
if __name__ == '__main__' :
    main()