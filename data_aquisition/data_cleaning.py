import re
def reference_dic_needed(the_frame):
    needed_data_dic = {
    'locality' : 'locality',
    'Type_property' : 'property_type',
    'Price' : 'Price, ',
    'Sale_type' : 'sale_type',
    'Number_bedrooms' : "bedroom",
    'Living_area' : '\\n Living area\\n , ',
    'fully_equipped_kitchen' : 'Kitchen type, ',#Yes no
    'Furnished' : 'Furnished, ',
    'terrace' : 'Terrace surface, ',
    'garden' : 'Garden surface, ', 
    'surface_land' : 'size_of_house',
    'surface_area_plot' : 'Surface of the plot, ',
    'facades_number' : '\\n Number of frontages\\n , ',
    'Swimming_pool' : '\\n Swimming pool\\n , ',
    'building_state' : '\\n Building condition\\n , '
    }
    last_frame = {}
    for key,value in needed_data_dic.items() :
        last_frame[key] = the_frame[value]

    
    return last_frame
def clean_escape_characters(string):
    return re.sub(r'\\n|\\x..', '', string)