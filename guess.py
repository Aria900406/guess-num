import random

start = input('請輸入隨機數字開始值: ')
end = input('請輸入隨機數字結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
    count += 1
    num = input('請猜一個數字: ')
    num = int(num)
    if num == r:
        print('你猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif num < r:
            print('答案比數字大')
    else:
       print('答案比數字小') 
    print('這是你猜的第', count, '次\n')



