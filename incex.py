import random
question = input('Do you want to dice Y/N : ')

while question.upper() == 'Y':
    print(f'your number is {random.randint(1,6)}')
    question = input('Do you want to roll again !!')
else:
    print('Thank you For Playing')
