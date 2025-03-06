total_word = ''
word = ''
while word != 'halt':
    word = input('Enter a word or enter "halt" to quit: ')
    if word != 'halt':
        total_word = total_word + word + ' '
print(total_word)