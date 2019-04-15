while True:##修改测试#####################3
    print("Please enter a positive integer")
    user_input = input(":")
    if user_input == "1":
        print("0")
    elif user_input >= "1":
        Qnum = int(float(user_input) ** 0.5)  # 标记以1位中心的圈数，1为0圈，以此类推
        tt = float(user_input) ** 0.5  # 过程变量
        if (Qnum % 2 != 0) & (tt - int(tt) == 0):  # 开方是奇数(这是迷宫右下角的拐点)
            Qnum = (Qnum - 1) / 2
        elif (Qnum % 2 == 0):
            Qnum = Qnum / 2
        else:
            Qnum = (Qnum + 1) / 2
        Gd = (Qnum * 2 + 1) ** 2
        d1 = Gd - Qnum  # 定位正方形四个中点
        d2 = Gd - Qnum - Qnum * 2
        d3 = Gd - Qnum - Qnum * 2 - Qnum * 2
        d4 = Gd - Qnum - Qnum * 2 - Qnum * 2 - Qnum * 2
        e1 = abs(int(user_input) - d1)
        e2 = abs(int(user_input) - d2)
        e3 = abs(int(user_input) - d3)
        e4 = abs(int(user_input) - d4)
        e = min(e1, e2, e3, e4)
        Qnum = Qnum + e
        print(int(Qnum))
