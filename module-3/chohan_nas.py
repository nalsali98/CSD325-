"""
chohan_nas.py
Author: Noor Al Salihi
Course: CSD-325
Assignment: Module 3 – Brownfield + Flowchart(s)

Changes made from the original chohan.py:
1. Input prompt changed to 'nas:' instead of '>'.
2. House percentage changed from 10% to 12%.
3. Added bonus rule: if the dice total is 2 or 7, player gets +10 mon.
4. Added new intro line explaining the bonus rule.
"""

import random, sys

# Japanese dice number names
JAPANESE_NUMBERS = {
    1: 'ICHI', 2: 'NI', 3: 'SAN',
    4: 'SHI', 5: 'GO', 6: 'ROKU'
}

print('''Cho-Han (NAS Edition), by Noor Al Salihi

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (CHO) or odd (HAN) number.

New Rule: If you roll a total of 2 or 7, you get a 10 mon bonus!
''')

purse = 5000  # starting money

while True:  # main game loop
    # Ask the player how much they want to bet
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('nas: ')  # changed prompt to 'nas:'
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2  # total for bonus rule

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.\n')
    print('    CHO (even) or HAN (odd)?')

    # Player chooses CHO or HAN
    while True:
        bet = input('nas: ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Bonus rule for total of 2 or 7
    if total == 2 or total == 7:
        print(f'BONUS! You rolled a total of {total} and get +10 mon.')
        purse += 10

    # Determine the correct bet
    rollIsEven = (total % 2 == 0)
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = (bet == correctBet)

    # Display results
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        house_cut = int(pot * 0.12)  # changed from 10% to 12%
        print('The house collects a', house_cut, 'mon fee (12%).')
        purse = purse - house_cut
    else:
        purse = purse - pot
        print('You lost!')

    # Check for empty purse
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()

    print()  # blank line for readability
