"""用python 设计第一个游戏"""
import random

guess = 0;
r = random.randint(1, 10)
while guess != r:

    temp = input("不妨猜一下小鲫鱼心里想的是什么数字：")
    guess = int(temp)

    if guess == r:
        print("牛逼克拉斯")
        print("猜对也没奖励！")
    else:
        if guess < r:
            print("小了")
        else:
            print("大了")

print("游戏结束！！！")
