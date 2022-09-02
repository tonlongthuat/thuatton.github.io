from game_data import data
from art import logo,vs
import random

def printable(ran_choice):
    name=ran_choice['name']
    # follower_count = ran_choice['follower_count']
    description = ran_choice['description']
    country = ran_choice['country']
    return f' {name}, {description}, from {country}'

def check_answer(guess,a_follower,b_follower):
    if a_follower > b_follower:
        return guess=='a'
    else:
        return guess=='b'

def play_game():
    game_on=True
    current_score=0
    b=random.choice(data)
    while game_on:
        a=b
        b=random.choice(data)
        while a == b:
            b=random.choice(data)
        print(logo)
        print(f'Compare A,{printable(a)}')
        print(vs)
        print(f'Against B,{printable(b)}')
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct=check_answer(guess,a['follower_count'],b['follower_count'])
        if is_correct:
            current_score =current_score + 1
            print(f'you are right, current_score {current_score}')
        else:
            game_on=False
            print(f'you are wrong, current_score {current_score}')
            
play_game()


