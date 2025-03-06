def returnMiddle(x, y, z):
    if x > y and x < z or x < y and x > z:
        return x
    if y > x and y < z or y < x and y > z:
        return y
    if z > x and z < y or z < x and z > y:
        return z
    
        
num_1 = int(input('Enter the first integer: '))
num_2 = int(input('Enter the second integer: '))
num_3 = int(input('Enter the third integer: '))
print(f'The middle value is {returnMiddle(num_1, num_2, num_3)}.')