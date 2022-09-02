from random import shuffle,choice

lis_of_card=[2,3,4,5,6,7,8,9,10,10,10,10,11]
def card():
    return choice(lis_of_card)

def caculate_score(card):
    if sum(card) == 21 and len(card)==2:
        return 21
    if 11 in card and sum(card) >21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare_card(user_score,computer_score):
    if user_score >21 and computer_score >21:
        return "went over, you lose!"
    if user_score ==computer_score :
        return 'DRAW'
    elif user_score == 0:
        return 'you win'
    elif computer_score == 0:
        return 'compute win'
    elif user_score > 21:
        return 'you lose'
    elif computer_score > 21:
        return 'you win'    
    elif user_score > computer_score:
        return 'you win'
    else:
        return 'you lose'

def play_game():
    user_card =[]
    computer_card=[]
    game_on=True
    for i in range(2):
            user_card.append(card())
            computer_card.append(card())
        
    while game_on:
        user_score=caculate_score(user_card)
        computer_score=caculate_score(computer_card)
        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   Computer's first card: {computer_card[0]}")
        if user_score==21 or computer_score==21 or user_score >21 :
            game_on=False
        else:
            user_deal=input('type y to hit or n to stand:  ')
            if user_deal=='y':
                user_card.append(card())
            else:
                game_on=False
    while computer_score!=0 and computer_score<17:
        computer_card.append(card())
        computer_score=caculate_score(computer_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare_card(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()


