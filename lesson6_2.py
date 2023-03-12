import random

def play_one():
    min = 1
    max = 10
    random_value = random.randint(min,max)
    print('猜數字')
    while True:
        keyin = int(input(f'猜數字的範圍{min}~{max}:'))
        if(keyin == random_value):
            print(f'猜對了，答案是{random_value}')
            break
        else:
            print('猜錯了')

    print('結束')

def play_game():
    while True:
        play_one() 
        play_again = input('還要繼續玩嗎？{y,n}')
        if play_again == 'n':
            break;

if __name__ == '__main__':
   play_game()
