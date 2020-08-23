import number_tools

# 无限循环由用户决定什么时候退出
while True:

    # 显示功能菜单
    number_tools.show_menu()

    action_str = input("你希望执行的操作是：")
    print("你选择的运算是:【%s】" % action_str)

    # 1 2 3 4 5对应的不同的运算操作
    if action_str in ["1", "2", "3", "4", "5"]:

        # 加法运算
        if action_str == "1":
            number_tools.number_add()

        # 减法操作
        elif action_str == "2":
            number_tools.number_subtraction()

        # 乘法运算
        elif action_str == "3":
            number_tools.number_multiplication()

        # 除法运算
        elif action_str == "4":
            number_tools.number_divider()

        # 自定义运算
        elif action_str == "5":
            number_tools.number_custom()

    #  0  退出系统
    elif action_str == "0":

        print("欢迎再次使用【马骏牌计算器v1.0】")

        break

    else:

        print("你输入的指令是错误的，请重新输入")

