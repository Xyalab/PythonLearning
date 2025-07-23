

# try:
#     print(name)
# except:
#     print("报错了")


try:
    "yg"+1
except (IndentationError, TypeError) as e:
    print("报错了", e)



# try:
#     1/0
# except Exception as e:
#     print("报错了：", e)
# else:
#     print("没错")
# finally:
#     print("一直会执行")