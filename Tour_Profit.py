people = int(input('Enter the number of people on the tour: '))
profit = -2 * (people**2) + 268 * people - 6000
print(f'The profit on a tour of {people} people would be ${profit:,.2f}.')