
#get random value
import random

option = ('rock', 'paper', 'scissors')
cpu = random.choice(option)

print('//////////////////-------------------------xSUI---------------')
user = input('\n\nPlease choose rock,paper or scissor: ')

#reprompt incase does not type what is among choices
while user not in option:
    user = input('Invalid Entry! Please pick among choices: ')

#if statements 
if user == 'rock' and cpu == 'scissor':
    print(f'cpu: {cpu}')
    print(f'user: {user}')
    print('you won!')
elif user == 'paper' and cpu == 'rock':
    print(f'cpu: {cpu}')
    print(f'user: {user}')
    print('you won!')
elif user == 'scissors' and cpu == 'paper':
    print(f'cpu: {cpu}')
    print(f'user: {user}')
    print('you won')
elif user == cpu:
    print(f'cpu: {cpu}')
    print(f'user: {user}')
    print('you tied')
else:
   print(f'cpu: {cpu}')
   print(f'user: {user}')
   print('you lost')

print('thank you for playing')