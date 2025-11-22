from random import randint

player_cards = []
player_sum = 0
bot_cards = []
bot_sum = 0
balance = 1000
bet = 0

def main():
    global player_sum, bet
    choice = "y"
    print('Wellcome to BlackJack!')
    while choice == "y" and balance > 0:
        bets()
        player()
        bot()
        winner()
        if balance > 0:
            choice = input("Would you like to continue (y/n)? ")
        else:
            print('You ran out of money.')
        
        player_cards.clear()
        bot_cards.clear()
        bet = 0

def bets():
    global balance, bet
    while bet > balance or bet <= 0:
        bet = int(input(f'Your balance is {balance}$\nHow much would you like to risk? '))
    balance -= bet

def player():
    global player_sum, balance
    want = ""
    for i in range(2):
        more_cards(player_cards)

    print_cards(player_cards, "Your")

    want = input('Would you like more cards (y/n)? ')

    while want == "y" and sum(player_cards) < 21:
        more_cards(player_cards)
        print_cards(player_cards, "Your")
        
        print(f'Your total is {sum(player_cards)}')

        if sum(player_cards) < 21:
            want = input('Would you like more cards (y/n)? ')

    player_sum = sum(player_cards)

    if player_sum > 21:
        print('You lose, because you have too much cards!')

def bot():
    global bot_sum, player_sum, balance
    if player_sum < 22:
        for i in range(2):
            more_cards(bot_cards)
        
        while sum(bot_cards) < 17:
            more_cards(bot_cards)
        
        print_cards(bot_cards, "Bot")
        bot_sum = sum(bot_cards)
        print(f'Bot\'s total is {sum(bot_cards)}')


        if bot_sum > 21:
            print('You won, because the bot has too much cards!')
            balance += bet * 2

def winner():
    global player_sum, bot_sum, balance, bet
    if bot_sum < 22 and player_sum < 21:
        if player_sum > bot_sum:
            print('You won!')
            balance += bet * 2
        elif player_sum <= bot_sum:
            print('You lost!')
    
    print(f'Your new balance is {balance}$')
         
def sum(cards):
    sum = 0
    for card in cards:
        match card:
            case "Jumbo": sum += 10
            case "Dama": sum += 10
            case "King": sum += 10
            case "Ace": sum += 11
            case _: sum += card
        
        if sum > 21 and "Ace" in cards:
            sum -= 10

    return sum

def more_cards(cards):
    x = randint(2, 14)
    match x:
        case 11: cards.append("Jumbo")
        case 12: cards.append("Dama")
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