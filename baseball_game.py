# -*- coding: utf-8 -*-

import random
from collections import Counter


def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    result = True if user_input_number.isdigit() else False
    return result


def is_between_100_and_999(user_input_number):
    result = True if int(user_input_number) >= 100 and int(user_input_number) < 1000 else False 
    return result


def is_duplicated_number(three_digit):
    c = Counter(three_digit)
    result = True if any(cnt > 1 for elem, cnt in c.items()) else False
    return result


def is_validated_number(user_input_number):
    result = True if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number) else False
    return result


def get_not_duplicated_three_digit_number():
    random_number = get_random_number()
    while is_duplicated_number(str(random_number)):
        random_number = get_random_number()
    result = random_number
    return result


def get_strikes_or_ball(user_input_number, random_number):
    strike = 0
    strikes = []
    ball = 0
    for i, (a, b) in enumerate(zip(list(user_input_number), list(random_number))):
        if a == b: 
            strike += 1
            strikes.append(i)

    if strike == 0:
        for c in user_input_number:
            if c in random_number:
                ball += 1
    elif strike == 1 or strike == 2:
        for i, c in enumerate(user_input_number): 
            for j, d in enumerate(random_number):
                if c == d and j != i:
                    ball += 1

    result = [strike, ball]
    return result


def is_yes(one_more_input):
    modified = one_more_input.strip().lower()
    result = True if modified == 'y' or modified == 'yes' else False
    return result


def is_no(one_more_input):
    modified = one_more_input.strip().lower()
    result = True if modified == 'n' or modified == 'no' else False
    return result


def main():
    user_continue = True
    print("Play Baseball")
    while user_continue:                                                # 게임을 시작하거나 이어서 하는 조건
        user_input = 999

        random_number = str(get_not_duplicated_three_digit_number())    # 중복되지 않는 수를 가진 임의의 3자리수를 반환
        print("Random Number is : ", random_number)
    
        strike = None
        while strike != 3:                                              # 게임이 시작할때는 3 strikes가 아니므로 게임시작 / 3 strikes 나오면 게임종료
            user_input = input("Input guess number: ")
            if user_input == '0':                                       # 0을 입력하면 게임 종료
                print("Thank you for using this program")
                print("End of the Game")
                user_continue = False
                break
            if not is_validated_number(user_input):                     # wrong input 판단되면 다시 물어보는 로직
                print("Wrong Input, Input again")
                continue
            result = get_strikes_or_ball(user_input, random_number)     # 결과 로직
            strike, ball = result
            print(f"Strikes: {strike}, Balls: {ball}")                  # 결과 출력
        
        while strike == 3:                                              # 게임 종료 후 다시 진행하는지 묻는 loop / wrong input이면 다시 물어본다
            answer = input("You won the game ! One more? (Y/N)")
            if is_yes(answer):
                user_continue = True
                break
            elif is_no(answer):
                print("Thank you for using this program")
                print("End of the Game")
                user_continue = False
                break
            else:
                print("Wrong Input, Input again")                       # wrong input 이면 continue를 실행해서 while 첫줄로 돌아간다 
                continue
                

if __name__ == "__main__":
    main()
