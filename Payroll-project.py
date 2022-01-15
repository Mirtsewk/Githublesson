count = 0
while count < 10:
    count += 1

    name = input('Enter Employee name: ')
    payrate = float(input('Enter payrate: '))
    hours = float(input('Enter hours: '))

#calculate gross
    if hours <= 40:
        gross = payrate * hours
        regular = gross
        overtime = 0
    elif hours > 40:
        regular = payrate * 40
        overtime = (hours - 40) * (payrate * 1.5)   
        gross = overtime + regular

    federal = gross * .1
    state = gross * .06
    fica = gross * .03

    print(f'Employee name: {name}')
    print(f'regular: {regular}')
    print(f'overtime: {overtime}')
    print(f'gross: {gross}')
    print(f'federal: {federal}')
    print(f'state: {state}')
    print(f'fica: {fica}')
    print(f'net pay: {gross  - federal - state - fica}')