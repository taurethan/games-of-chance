#!/usr/bin/env python3
import random

money = 100

#Write your game of chance functions here
def coinFlip(bet, choice):
    if bet <= 0:
        print('====================================================')
        print('Your bet must be higher than zero.')
        print('====================================================')
        return 0

    global money

    flip = random.randint(1,2)
    flipAsText = ''

    print('**Welcome to Coin Flip**')

    if flip == 1:
        flipAsText += 'heads'
    else:
        flipAsText += 'tails'

    print('You chose ' + choice + ' and the flip is ' + flipAsText)

    if (choice.lower() == 'heads' and flip == 1) or (choice.lower() == 'tails' and flip == 2):
        money += bet
        print('You won ' + str(bet))
        return bet 
    elif (choice.lower() == 'heads' and flip == 2) or (choice.lower() == 'tails' and flip == 1):
        money -= bet
        print('You lost ' + str(bet))
        return -bet
    else:
        print('Please select one of "heads" or "tails."')
        return 0

def choHan(bet, choice):
    # check bet
    if bet <= 0:
        print('====================================================')
        print('Your bet must be higher than zero.')
        print('====================================================')
        return 0

    global money

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    result = die1 + die2

    print('**Welcome to Cho Han**')

    print('You chose ' + choice + ' and the sum of the roll is ' + str(result))

    if (choice.lower() == 'odd' and result % 2 == 1) or (choice.lower() == 'even' and result % 2 == 0):
        money += bet
        print('You won ' + str(bet))
        return bet
    elif (choice.lower() == 'odd' and result % 2 == 0) or (choice.lower() == 'even' and result % 2 == 1):
        money -= bet
        print('You lost ' + str(bet))
        return -bet
    else:
        print('Please enter one of "odd" or "even".')
        return 0

def cards(bet):
    # check bet
    if bet <= 0:
        print('====================================================')
        print('Your bet must be higher than zero.')
        print('====================================================')
        return 0

    global money

    deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,
           9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
    
    print('**welcome to cards**')

    # shuffle deck for player, player draws, drawn card removed from deck
    random.shuffle(deck)
    playerDraw = random.randint(1, len(deck)-1)
    playerCard = deck.pop(playerDraw)

    # shuffle deck for computer, computer draws, drawn card removed from deck
    random.shuffle(deck)
    computerDraw = random.randint(1, len(deck)-1)
    computerCard = deck.pop(computerDraw)

    print('You chose ' + str(playerCard) + ' and the computer chose ' + str(computerCard))

    if playerCard > computerCard:
        money += bet
        print('You won ' + str(bet))
        return bet
    elif playerCard < computerCard:
        money -= bet
        print('You lost ' + str(bet))
        return -bet
    else:
        print('A draw...how lame :(')
        return 0

def roulette(bet, choice):
    # check bet
    if bet <= 0:
        print('====================================================')
        print('Your bet must be higher than zero.')
        print('====================================================')
        return 0

    global money

    print('**Welcome to roulette**')

    roll = random.randint(0,36)
    color = ''
    parity = ''

    # assign odd nums to black and even nums to red
    if roll % 2 == 1:
        color += 'black'
        parity += 'odd'
    else:
        color += 'red'
        parity += 'even'

    print('You chose ' + str(choice) + ' the roll is ' + str(roll) + ', ' + color + ', ' + parity)

    # if player chooses red or black
    if choice == 'red' and roll % 2 == 0 and roll != 0:
        money += bet
        print('You won ' + str(bet))
        return bet
    elif choice == 'black' and roll % 2 == 1 and roll != 0:
        money += bet
        print('You won ' + str(bet))
        return bet
    # if player chooses odd or even
    elif choice == 'even' and roll % 2 == 0 and roll != 0:
        money += bet
        print('You won ' + str(bet))
        return bet
    elif choice == 'odd' and roll % 2 == 1 and roll != 0:
        money += bet
        print('You won ' + str(bet))
        return bet
    # if player chooses to guess a number
    elif choice == roll:
        money += bet * 35
        print('You won ' + str(bet))
        return bet * 35
    # otherwise the player loses
    else:
        money -= bet
        print('You lost ' + str(bet))
        return -bet


#Call your game of chance functions here
print('====================================================')
coinFlip(10, 'tails')
print('Total: ' + str(money))
print('====================================================')

print('====================================================')
choHan(10, 'even')
print('Total: ' + str(money))
print('====================================================')

print('====================================================')
cards(10)
print('Total: ' + str(money))
print('====================================================')

print('====================================================')
roulette(10, 'odd')
print('Total: ' + str(money))
print('====================================================')

