def show_menu():

    print("*" * 50)
    print("欢迎使用【马骏牌计算器】v1.0")
    print("")
    print("1.加法运算")
    print("2.减法运算")
    print("3.乘法运算")
    print("4.除法运算")
    print("5.自定义运算")
    print("6.退出系统")
    print("*" * 50)


def number_add():

    """加法运算"""
    print("*" * 50)
    print("加法运算")
    # 1.提示用户输入第一个数字
    first_number = float(input("请输入第一个数字："))
    # 2.提示用户输入第二个数字
    second_number = float(input("请输入第二个数字："))
    # 3.求和运算
    add_result = first_number + second_number
    # 4.结果显示
    print(add_result)


def number_subtraction():

    """减法运算"""
    print("*" * 50)
    print("减法运算")
    # 1.提示用户输入第一个数字
    first_number = float(input("请输入第一个数字："))
    # 2.提示用户输入第二个数字
    second_number = float(input("请输入第二个数字："))
    # 3.求差运算
    subtraction_result = first_number - second_number
    # 4.结果显示
    print(subtraction_result)


def number_multiplication():

    """乘法运算"""
    print("*" * 50)
    print("乘法运算")
    # 1.提示用户输入第一个数字
    first_number = float(input("请输入第一个数字："))
    # 2.提示用户输入第二个数字
    second_number = float(input("请输入第二个数字："))
    # 3.求积运算
    multiplication_result = first_number * second_number
    # 结果显示
    print(multiplication_result)


def number_divider():

    """除法运算"""
    print("*" * 50)
    print("除法运算")
    # 1.提示用户输入第一个数字
    first_number = float(input("请输入第一个数字："))
    # 2.提示用户输入第二个数字
    second_number = float(input("请输入第二个数字："))
    # 3.求商运算
    divider_result = first_number / second_number
    # 4.显示结果
    print(divider_result)


def number_custom():
    formula = input("请输入公式：")
    item = ''
    for i in formula:
        if i.isspace():
            pass
        else:
            item += i
    num01 = ''
    num_list = []  # 用来存储数字
    symbol_list = []  # 用来存储运算符号
    count = 0  # 计数器，判断是否连续出现运算符
    for i in item:
        if count > 1:
            print('输入有误，请重新输入')
            break
        elif i.isdigit() or i == '.':
            num01 += i  # 判断单个字符，对于连续的数字字符，将会组合在一起，即'789' 变为数字
            count = 0  # 出现数字符号，计数器重置为0
        elif i == '*' or i == '/' or i == '+' or i == '-':
            num_list.append(float(num01))
            num01 = ''
            symbol_list.append(i)
            count += 1  # 出现运算符，计数器加1，连续出现，count>1，第一个if条件生效
        else:
            print('输入有误，请重新输入')
            break
    num_list.append(float(num01))  # 在公式最后不会出现运算符，所以需要将最后一个存入列表

    # 对num_list和symbol_list两个列表进行处理，进行运算
    while symbol_list:
        while "*" in symbol_list or "/" in symbol_list:  # 先寻找*和/运算
            for i in symbol_list:
                if i == "*":
                    # 找到运算符对应位置的symbol列表下标，对num_list里面对应位置的两个相邻数据进行运算，
                    # 并用结果覆盖原数据，同时删除symbol列表里的运算符
                    j = symbol_list.index("*")
                    result = num_list[j] * num_list[j+1]
                    del num_list[j:j+2]
                    num_list.insert(j, result)
                    symbol_list.remove("*")
                    break
                if i == "/":
                    j = symbol_list.index("/")
                    result = num_list[j] / num_list[j + 1]
                    del num_list[j:j + 2]
                    num_list.insert(j, result)
                    symbol_list.remove("/")
                    break

        while "+" in symbol_list or "-" in symbol_list:
            for i in symbol_list:
                if i == "+":
                    j = symbol_list.index("+")
                    result = num_list[j] + num_list[j+1]
                    del num_list[j:j + 2]
                    num_list.insert(j, result)
                    symbol_list.remove("+")
                    break
                if i == "-":
                    j = symbol_list.index("-")
                    result = num_list[j] - num_list[j + 1]
                    del num_list[j:j + 2]
                    num_list.insert(j, result)
                    symbol_list.remove("-")
                    break
    print(num_list)










