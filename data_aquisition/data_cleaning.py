from data_analyse_pandas import get_data_from_url, data_to_pandas
needed_data_dic = {
    'locality' : [],
    'Type_property' : [],
    'Price' : 'Price, ',
    'Sale_type' : [],
    'Number_rooms' : [],
    'Living_area' : '\\n Living area\\n , ',
    'fully_equipped_kitchen' : 'Kitchen type, ',#Yes no
    'Furnished' : 'Furnished, ',
    'terrace' : 'Terrace surface, ',
    'garden' : 'Garden surface, ', 
    'surface_land' : [],
    'surface_area_plot' : 'Surface of the plot, ',
    'facades_number' : '\\n Number of frontages\\n , ',
    'Swimming_pool' : '\\n Swimming pool\\n , ',
    'building_state' : '\\n Building condition\\n , '
}
the_frame = {}
the_data = get_data_from_url("https://www.immoweb.be/en/classified/apartment-block/for-sale/ans/4430/10300959")

the_frame = data_to_pandas(the_data,the_frame)
the_data = get_data_from_url("https://www.immoweb.be/en/classified/house/for-sale/molenbeek-saint-jean/1080/10303905")
the_frame = data_to_pandas(the_data,the_frame)

print(the_frame)