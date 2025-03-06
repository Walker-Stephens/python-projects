import math
def calculate_volume(radius, height):
    volume = math.pi * radius**2 * height
    print(f'The volume of the cylinder is{volume: ,.2f}.')

calculate_volume(float(input('Enter the radius of the cylinder: ')), float(input('Enter the height of the cylinder: ')))