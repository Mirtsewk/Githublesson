#if condition excercise
#She is Mirtsew. She is 90 years old. She lives in Virginia, USA. 


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you from? ')
city = input('What is the capital city? ')
year_born = int(input('When were you born ? '))
current_year = 2021

gender = input('What is your gender ? ').lower()

pronoun=' '
if gender == 'female':
    pronoun ='She'
else:
    pronoun ='He'

print(f'{pronoun} is {first_name} {last_name}. {pronoun} is {current_year - year_born} old. {pronoun} lives in {city}, {country}')
