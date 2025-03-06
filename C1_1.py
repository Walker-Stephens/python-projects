import math
num = float(input('Enter a number: '))
def calculate_value(num):
    return ((3 * num - 2) / (math.sqrt(num * num + 5)))
print(f'For an input of {num}, the calculated value is {calculate_value(num):.3f}')