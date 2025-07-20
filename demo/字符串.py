# 单引号
str1 = '牛逼'
print(str1)

# 双引号
str2 = "牛逼"
print(str2)

# 多引号
str3 = """牛逼
卡拉斯"""
print(str3)

str4 = "\"牛逼克拉斯\""
print(str4)

str4 = "\'牛逼克拉斯'\"'"
print(str4)

s1 = "克"
s2 = "斯"
# +拼接，不可拼接其他类型
str6 = s1+s2
print(str6)

# 占位拼接，可拼接其他类型
str5 = "牛逼%s拉%s" %(s1,s2)
print(str5)

# %s %d %f
# 拼接字符串   拼接整数   拼接浮点数
# %2.6f     %5d

 # f"{xxx}" 拼接
str6 = "逼"
str7 = "克"
str8 = "丝"
print(f"牛{str6}{str7}拉{str8}, aaa")

print("当前股价为%5.12f, %d天后股价达到了%5.2f" %(19.999999999999, 7, 19.99*(1.2**7)))



print(str5.replace("牛逼", "超级NB"))

print(str5.split("逼"))

str9 = " fhsfslf sfsfsfs   "

print(str9.strip())
print(str9.strip().strip("f"))








for s in str5:
    print(s)


#range(10)  012345689

#range(0, 10) 0123456789

r = range(0, 10, 2)
for n in r:
    print(n)
#02468








