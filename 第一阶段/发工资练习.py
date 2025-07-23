# 发工资
import random

salary = 10000
for id in range(1, 21):
    score = random.randint(1, 10)
    if salary == 0:
        print("工资发完了，下个月领取吧。")
        break
    if score < 5:
        print(f"员工{id}，绩效分{score}，低于5，不发工资，下一位。")
        continue
    else:
        salary -= 1000
        print(f"向员工{id}发放工资1000元，账户余额还剩余{salary}元。")
