

# 九九乘法表

i = 1
while i<10:
    j = i
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t", end="")
    print("")
    i +=1

