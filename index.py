print('hola world')

def squaring_number(number):
    squared_number = number * number
    return squared_number

input_value = int(input('Input the number you wish to be squared'))

my_squared_number = squaring_number(input_value)
if my_squared_number < 10:
    print('this number is below 10')
else:
    print('This number is different')
