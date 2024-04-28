import geopy
from geopy.geocoders import Nominatim

def get_location(zip_code):

    ZIP = zip_code
    geolocator = Nominatim(user_agent="DataDoor")
    location = geolocator.geocode("United States {}".format(ZIP))
    address = location.address
    print(address)
    address_list = address.split(", ")

    us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


    for subdivision in address_list:
        if subdivision in us_states:
            state = subdivision


    if len(address_list)<5:
        if "County" in address_list[1]  :
            address_dict = {
                "ZIP":address_list[0],
                "City":None,
                "County":address_list[1],
                "State":state,
                "Country":"United States"
            }
        else:
            address_dict = {       
                "ZIP":address_list[0],
                "City":address_list[1],
                "County":None,
                "State":state,
                "Country":"United States"
            }
    else:
        address_dict = {
            "ZIP":address_list[0],
            "City":address_list[1],
            "County":address_list[2],
            "State":state,
            "Country":"United States"
        }

    return(address_dict)