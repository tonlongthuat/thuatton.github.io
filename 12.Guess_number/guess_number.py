import random

def random_num():
    lis_of_num=[]
    for i in range(1,101):
        lis_of_num.append(i)
    return random.choice(lis_of_num)

# def compare(num,ran_num):
#     # while game_on:
#     if num==ran_num:
#         print('that right!')
#     elif num > ran_num:
#         print('too high')
#     else:
#         print('too low')      


def play_game():
    choosing=True
    while choosing:
        difficulty =input('hard or nor:   ')
        if difficulty=='hard':
            attemp=5
            print(f'you have {attemp} attemp')
            choosing=False
        elif  difficulty=='nor':
            attemp=10
            print(f'you have {attemp} attemp')
            choosing=False
        else:
            print('just choose hard or nor')
        
    ran_num = random_num()
    num = int(input('Enter number:   '))
    game_on=True
    while game_on:
        if attemp==1:
            print('you lose!')
            break
        if num==ran_num:
            print('that right!')
            game_on=False
        elif num > ran_num:
            attemp=attemp-1
            print(f'too high you have {attemp} attemp')
            num = int(input('Enter number another number:   '))
            continue
        else:
            attemp=attemp-1
            print(f'too low you have {attemp} attemp')
            num = int(input('Enter number another number:   '))
            continue

play_game()
