
first_name = 'Mirtsew'
last_name = 'Worku'
Country = 'USA'
city = 'Virginia'
skills = ['linux', 'MS word', 'MS Excel', 'Python', 'Chef']
first_skills=', '.join(skills[0:-1])
last_skill=skills[-1] 
age = 90 
print(f'I am {first_name} {last_name}. \nI live in {city} {Country}. \nI am {age} years old. \nMy skills are {first_skills} and {last_skill}.')

