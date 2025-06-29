from random import *


def random_number():
    num = [str(randint(1, 9))]
    for i in range(1, 3):
        num.append(str(randint(0, 9)))
    return num


print('Bagels, a deductive logic game.\nBy Al Sweigart al@inventwithpython.com')
while True:
    print('\nwhat do you wish to do..?')
    print('1. New game\n2. Rules\n3. Exit Game')
    choice = input('enter choice: ')
    if choice == '1':
        print('-' * 72)
        t, x = ['_', '_', '_'], '______'
        data = {1: [t, x], 2: [t, x], 3: [t, x], 4: [t, x], 5: [t, x], 6: [t, x], 7: [t, x], 8: [t, x], 9: [t, x]}
        original_number = random_number()
        status = str()
        n, flag = 1, 0
        while 11 - n:
            print('\n\tWELCOME TO BAGELS')
            print('\nguess the correct number')
            print(f'you have {10 - n} chances left!!\n')
            print(f'1. {data[1][0]} \t--- {data[1][1]}')
            print(f'1. {data[2][0]} \t--- {data[2][1]}')
            print(f'3. {data[3][0]} \t--- {data[3][1]}')
            print(f'4. {data[4][0]} \t--- {data[4][1]}')
            print(f'5. {data[5][0]} \t--- {data[5][1]}')
            print(f'6. {data[6][0]} \t--- {data[6][1]}')
            print(f'7. {data[7][0]} \t--- {data[7][1]}')
            print(f'8. {data[8][0]} \t--- {data[8][1]}')
            print(f'9. {data[9][0]} \t--- {data[9][1]}')

            try:
                number = input('\nenter a 3 digit number: ')
                assert 100 <= int(number) <= 999
            except AssertionError or ValueError:
                print('\ninvalid number entered')
                input('press enter to go back')
                print('-' * 72)
                continue

            number = list(number)

            if number == original_number:
                flag = 1
                print('\n\n\t !!Congratulations!!')
                print('you have won the game, the correct number is', original_number)
                break

            status = ''
            for i in range(3):
                if number[i] == original_number[i]:
                    status = 'Fermi'
                    break
                elif number[i] in original_number:
                    status = 'Pico'
                elif status != 'Pico':
                    status = 'Bagels'

            data[n] = [number, status]
            n += 1
            print('-' * 72)
        if flag == 0:
            print('\n\n\t---GAME OVER---')
            print('the correct number was ', original_number)

    elif choice == '2':
        print('-' * 72)
        print('''\nIn Bagels, a deductive logic game, you must guess a secret 
three-digit number based on clues.

The game offers one of the following hints in response to your guess:
1. “Pico” when your guess has a correct digit in the wrong place
2.“Fermi” when your guess has a correct digit in the correct place
3. “Bagels” if your guess has no correct digits.

You have 10 tries to guess the secret number.''')
        input('\npress enter to go back')
    elif choice == '3':
        print('\nyou have exited the program')
        print('*' * 72)
        quit()
    else:
        input('\nInvalid choice, press enter to go back')
    print('-' * 72)
