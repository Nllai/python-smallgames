import random

# start
punches = ['Rock','Scissors','Paper']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('Please choose from：（Rock, Scissors, Paper）')  
while user_choice not in punches:
    print('Invalid input type, please input again')
    user_choice = input()

# progress
print('————Progress————')
print('Computer：%s' % computer_choice)
print('You：%s' % user_choice)

# result
print('—————Result—————')
if user_choice == computer_choice:  
    print('Tie！')
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == Scissors and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock'):
    print('You win！')
else:
    print('You lost！')
