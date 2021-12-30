#import countries_list # to import the list

from pprint import pprint
from countries_list import countries

new_list = []
for country in countries:
    new_list.append([country, country.upper(), country.upper()[:3], len(country)])
print(new_list)

def get_countries_with_ia():
    new_list []
    for c in countries:
        if 'ia' in c:
            new_list.append(c)
    return new_list
print(get_countries_with_ia())

def get_countries_with_five_letter():
    new_list -[]
    for c in countries:
        if 'five_letters' in c:
            new_list.append(c)
    return new_list
print(get_countries_with_five_letter())




