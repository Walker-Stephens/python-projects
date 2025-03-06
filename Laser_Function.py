def laser(*args):
    big = []
    odds = args[0:len(args):2]
    square = []
    for num in args:
        if num > 7:
            big.append(num)
        if num in odds:
            square_num = num**2
            square.append(square_num)
            
    return (big, square)
print(laser(10, 1, 22, 9, 5, 76, 25, 81, 10))




        