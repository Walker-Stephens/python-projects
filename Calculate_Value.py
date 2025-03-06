import math
def calculate_value(v):
    value = (3 * v - 2) / math.sqrt(v**2 + 5)
    print(f'For an input of {v}, the calculated value is {value: ,.3f}.')
calculate_value(float(input('Enter a number.\n')))
