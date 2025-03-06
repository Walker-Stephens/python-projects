income = float(input('Enter your taxable income:  '))
amount_due = 0
if income >= 0 and income <= 9525:
    amount_due = income * .10
elif income >= 9526 and income <= 38700:
    amount_due = 952.5 + .15 * (income - 9525)
elif income >= 38701 and income <= 93700:
    amount_due = 5328.75 + .25 * (income - 38700)
elif income >= 93701 and income <= 195450:
    amount_due = 19078.75 + .28 * (income - 93700)
elif income >= 195451 and income <= 424950:
    amount_due = 47568.75 + .33 * (income - 195450)
elif income >= 424951 and income <= 426700:
    amount_due = 123303.75 + .35 * (income - 424950)
elif income >= 426701:
    amount_due = 123916.25 + .396 * (income - 426700)
else:
    print('The amount entered cannot be negative.')
if income >= 0:
    print(f'The tax due on ${income:,.2f} is ${amount_due:,.2f}.')