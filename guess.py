import random

r = random.randint(1, 100)
count = 0

while True:
    count += 1
    num = input('請猜一個介於1~100的數字: ')
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



