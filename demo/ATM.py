# ATM

money = 500000
name = input("请输入您的姓名：")


def save_money(money_in):
    if money_in < 0:
        global exit_flag
        exit_flag = False
        print("输入有误，系统已退出，谢谢使用！！！")
        # money_in = input("输入金额有误，请重新输入：")
        # save_money(money_in)
    else:
        global money
        money += money_in
        print(f"当前账户余额为{money}")

def get_money(money_in):
    if money_in < 0:
        global exit_flag
        exit_flag = False
        print("输入有误，系统已退出，谢谢使用！！！")
        # money_in = input("输入有误，请重新输入：")
        # get_money(money_in)
    else:
        global money
        money -= money_in
        print(f"当前账户余额为{money}")

exit_flag = True
while exit_flag:
    print("主菜单 \n 1、查询余额\n 2、存款\n 3、取款\n 4、退出")
    choice = input("请选择需要办理的业务：")
    if choice == "1":
        print(f"当前账户余额为{money}")
    elif choice == "2":
        money_input = input("请输入要存入的金额：")
        money_input = int(money_input)
        save_money(money_input)
    elif choice == "3":
        money_input = input("请输入要取出的金额：")
        money_input = int(money_input)
        get_money(money_input)
    elif choice == "4":
        exit_flag = False
        print("系统已退出，谢谢使用！！！")


