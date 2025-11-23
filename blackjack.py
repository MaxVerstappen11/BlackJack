from random import randint

player1_cards = []
player1_sum = 0
name1 = ""
player2_cards = []
player2_sum = 0
name2 = ""
bot_cards = []
bot_sum = 0
balance1 = 1000
bet1 = 0
balance2 = 1000
bet2 = 0
players = 5
choice = "y"

def main():
    global player1_sum, bot_sum, balance1, balance2, choice
    print('Wellcome to BlackJack!')

    while choice == "y" and balance1 > 0 and balance2 > 0:
        bets()
        player1()
        player2()
        bot()
        if players == 0:
            winner(bot_sum)
        else:
            winner(player2_sum)
        after_rounds()

def bets():
    global balance1, bet1, balance2, bet2, players, name1, name2
    while players != 0 and players != 1:
        players = int(input('Would you like to play against a bot (0) or against your friend (1)? '))
    print()

    if players == 0:
        name1 = input('What\'s your name? ')
    else:
        name1 = input('Player 1\'s name: ')
        name2 = input('Player 2\'s name: ')

    while bet1 > balance1 or bet1 <= 0:
        bet1 = int(input(f'{name1} balance is {balance1}$\nHow much would you like to risk? '))
    balance1 -= bet1

    if players == 1:
        print()
        while bet2 > balance2 or bet2 <= 0:
            bet2 = int(input(f'{name2} balance is {balance2}$\nHow much would you like to risk? '))
        balance2 -= bet2

def player1():
    global player1_sum, balance1, name1
    print(f'\n{name1}\'s turn')
    want = ""
    for i in range(2):
        more_cards(player1_cards)

    print_cards(player1_cards, "Your")
    print(f'Your total is {sum(player1_cards)}')

    want = input('Would you like more cards (y/n)? ')

    while want == "y" and sum(player1_cards) < 21:
        more_cards(player1_cards)
        print_cards(player1_cards, "Your")
        
        print(f'Your total is {sum(player1_cards)}')

        if sum(player1_cards) < 21:
            want = input('Would you like more cards (y/n)? ')

    player1_sum = sum(player1_cards)

    if player1_sum > 21:
        print('You lost, because you have too much cards!')

def player2():
    global player1_sum, player2_sum, balance2, name2
    if player1_sum < 22 and players == 1:
        print(f'\n{name2}\'s turn')
        want = ""
        for i in range(2):
            more_cards(player2_cards)

        print_cards(player2_cards, "Your")
        print(f'Your total is {sum(player2_cards)}')

        want = input('Would you like more cards (y/n)? ')

        while want == "y" and sum(player2_cards) < 21:
            more_cards(player2_cards)
            print_cards(player2_cards, "Player 2")
            
            print(f'Your total is {sum(player2_cards)}')

            if sum(player2_cards) < 21:
                want = input('Would you like more cards (y/n)? ')

        player2_sum = sum(player2_cards)

        if player2_sum > 21:
            print('You lost, because you have too much cards!')

def bot():
    global bot_sum, player1_sum, balance1, players
    if player1_sum < 22 and players == 0:
        print('\nBot\'s turn')
        for i in range(2):
            more_cards(bot_cards)
        
        while sum(bot_cards) < 17:
            more_cards(bot_cards)
        
        print_cards(bot_cards, "Bot")
        bot_sum = sum(bot_cards)
        print(f'Bot\'s total is {sum(bot_cards)}')


        if bot_sum > 21:
            print('You won, because the bot has too much cards!')
            balance1 += bet1 * 2

def winner(sum2):
    global player1_sum, player2_sum, bot_sum, balance1, bet1, balance2, bet2, players, name1, name2
    if sum2 < 22 and player1_sum < 22:
        print()
        if player1_sum > sum2:
            print(f'{name1} won!')
            balance1 += bet1 * 2
        elif player1_sum < player2_sum:
            print(f'{name2} won!')
            balance2 += bet2 * 2
        elif player1_sum <= bot_sum:
            print('You lost!')
    
        if players == 0:
            print(f'Your new balance is {balance1}$')
        elif players == 1:
            print(f'{name1} new balance is {balance1}$')
            print(f'{name2} new balance is {balance2}$')
        print()
    elif players == 1:
        print(f'{name1} new balance is {balance1}$')
        print(f'{name2} new balance is {balance2}$')
        print()
    elif players == 0:
        print(f'{name1} new balance is {balance1}$')
        print()
         
def after_rounds():
    global balance1, balance2, choice, players, bet1, bet2
    if balance1 > 0 and balance2 > 0:
        choice = input("Would you like to continue (y/n)? ")

    if balance1 == 0 and players == 0 and choice == "n":
        print('The winner is you!')
    elif balance1 == 0 and players == 1:
        print(f'The winner is {name2}!')
    elif balance2 == 0 and players == 1:
        print(f'The winner is {name1}!')
    elif balance1 <= 0 and players == 0:
        print(f'{name1} ran out of money.')

    if (choice == "n" or (balance1 == 0 or balance2 == 0)) and players == 1:    
        if balance1 < balance2:
            print(f'\nThe absolute winner is {name2}!\n')
        else:
            print(f'\nThe absolute winner is {name1}!\n')
        
        player1_cards.clear()
        player2_cards.clear()
        bot_cards.clear()
        bet1 = 0
        bet2 = 0
        
def sum(cards):
    sum = 0
    for card in cards:
        match card:
            case "Jack": sum += 10
            case "Queen": sum += 10
            case "King": sum += 10
            case "Ace": sum += 11
            case "Ace(1)": sum += 1
            case _: sum += card
        
    if sum > 21 and "Ace" in cards:
        cards.remove("Ace")
        cards.append("Ace(1)")
        sum -= 10

    return sum

def more_cards(cards):
    x = randint(2, 14)
    match x:
        case 11: cards.append("Jack")
        case 12: cards.append("Queen")
        case 13: cards.append("King")
        case 14: cards.append("Ace")
        case _: cards.append(x)

def print_cards(cards, whose):
    print(f'{whose} cards:', end=" ")
    for i,card in enumerate(cards):
        if i == len(cards) - 1:
            print(card)
        else:
            print(card, end=", ")


main()