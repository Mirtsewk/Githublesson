count = 0
while count < 10:
    count += 1

    name = input('Enter Employee name: ')
    payrate = float(input('Enter payrate: '))
    hours = float(input('Enter hours: '))

    if hours <= 40:
        gross = payrate * hours
    elif hours > 40:
        gross = payrate * hours
        gross = (hours - 40) * 1.5 * payrate + gross 

    federal = gross * .1
    state = gross * .06
    fica = gross * .03

    print(f'Employee name: {name}')
    print(f'gross pay: {gross}')
    print(f'federal: {federal}')
    print(f'state: {state}')
    print(f'fica: {fica}')
    print(f'net pay: {gross  - federal - state - fica}') 