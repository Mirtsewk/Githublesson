def add_two_nums(a, b):
    total = a+ b
    return total

print(add_two_nums(1,2))

def add_three_numbers(a, b, c):
    total = a + b + c
    return total

print(add_three_numbers(10, 12, 13))




def calculate_area_rectangle(length, width):
    area = length * width
    return area

print(calculate_area_rectangle(10,5))

def calculate__perimeter_of_a_rectangle(lenght, width):
    perimeter = 2 * (lenght + width)
    return perimeter

print(calculate__perimeter_of_a_rectangle(10, 15))



def generate_evens(n):
    evens = list(range(0, n + 1, 2))
    return evens
print(generate_evens(50))


def generate_odds(n):
    odds = list(range(0, n + 1, 2))
    return odds
print(generate_odds(50))

def calculate_weight (mass, gravity=9.81):
    weight = mass * gravity
    return weight
print(calculate_weight(75))
print(calculate_weight(75, 1.65))








