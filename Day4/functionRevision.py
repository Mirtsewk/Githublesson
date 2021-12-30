#Two kinds of funcetion 1. Builtin function and custom function
#it makes code resuseable, maintainable, testable

def name_of_func():
    print('This is a func and its is name_of_func')

def xyz ():
    print('I am a function')

def get_stud_info ():
    
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

print(get_stud_info())

def calc_area_circle():
    import math
    pi = math.pi
    radius = float(input('Enter the radius '))
    area = pi * radius * radius
    return round(area, 2)

print(calc_area_circle()) 

def create_fullname ():
    first_name = 'Mirt'
    last_name = "Worku"
    full_name = first_name + ' ' + last_name
    return full_name.upper()

print(create_fullname)('Mirt', 'Worku') 


