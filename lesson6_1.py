def sayHello():# 沒有參數的 function
    print('Hello')

def sayHello_withName(name):# 定義一個參數的 function
    print(f'Hello {name}')

def square_area(side): # 定義一個參數
    area = side ** 2 # function 內的變數
    return area

if __name__ == '__main__':
    side = eval(input('請輸入一個正方形的邊：'))
    area = square_area(side) # 文件變數
    print(f'正方形，一邊為10，面積為{area}')