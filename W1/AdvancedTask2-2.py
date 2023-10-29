# 猜数字游戏

import random

number = random.randint(1, 100)
count = 0
while True:
    guess = int(input("从1到100，请输入你要猜的数字："))
    count += 1
    print(count)
    if guess < number:
        print("大一点")
    elif guess > number:
        print("小一点")
    else guess == number:
        print("猜对了")
        print(f"你一共猜了{count}次")
        break
    