#一個專案內的主執行的py檔，必需要使用__name__的判斷式
'''
這是一個猜數字遊戲
'''
import random

if __name__ == '__main__':
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