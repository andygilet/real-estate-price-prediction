from data_aquisition.data_analyse_pandas import get_data_from_url, data_to_pandas
from data_aquisition.data_cleaning import reference_dic_needed, clean_escape_characters
import pandas as pd
import csv
def main() :
    ploted_frame = {}
    count = 0
    with open('links.csv', 'r') as links_file : 
        reader = csv.reader(links_file)
        for row in reader : 
            the_data = get_data_from_url(row[0])
            ploted_frame = data_to_pandas(the_data,ploted_frame)
            count += 1
            print(f"I'm at {count} page done")
            if count == 50 : 
                break
    for key in ploted_frame:
        ploted_frame[key] = [clean_escape_characters(value) for value in ploted_frame[key]]
    ploted_frame = reference_dic_needed(ploted_frame)

    df = pd.DataFrame(ploted_frame)

    df.to_csv('test.csv')

if __name__ == '__main__' :
    main()