from pygal.maps.world import COUNTRIES
 # returns the 2-digit country code
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None