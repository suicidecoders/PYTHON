#import random module to use random function
import random
sky_is_blue = True

#added while loop to keep on repeating game until user enters n to stop playing
while sky_is_blue:

    option = ('rock', 'paper', 'scissors')  #list of possible choices
    cpu = random.choice(option)     #function to generate random values from the list above

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

#this is to prompt user if he want to continue playing
    play_again = input('Continue playing? (y/n): ').lower()
    if not play_again == 'y':   #same as if play_again != 'y' in c language
        sky_is_blue = False

print('thank you for playing')