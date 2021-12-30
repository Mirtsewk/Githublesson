
from countries_data import countries_data 
from pprint import pprint
#pprint(countries_data)


population = []
for country in countries_data:
    population.append(country['population'])

#sorted

sorted_countries = sorted(population, reverse=True)
top_ten_countries = sorted_countries[:10]
pprint(top_ten_countries) 