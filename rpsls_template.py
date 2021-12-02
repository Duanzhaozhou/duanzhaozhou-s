#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：段照洲
"""

import random


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if name == "石头":
        return 0
    elif name == "史波克":
        return 1
    elif name == "布":
        return 2
    elif name == "蜥蜴":
        return 3
    elif name == "剪刀":
        return 4
    else :
        return print("Error: No Correct Name")


def number_to_name(number):
    if number == 0:
        return"石头"
    elif number == 1:
        return"史波克"
    elif number == 2:
        return"布"
    elif number == 3:
        return"蜥蜴"
    elif number == 4:
        return"剪刀"

def rpsls(player_choice):
    computer = random.randint(0, 4)

    comouters=number_to_name(computer)
    print("电脑的选择:%s"%(comouters))

    player_choice = name_to_number(player_choice)

    if player_choice != computer:
        if player_choice >= 2:
            if player_choice - computer == 2 or player_choice - computer == 1:
                print("您赢了")
            else:
                return print("您输了")
        else:
            player_choice = player_choice + 5
            if player_choice - computer == 2 or player_choice - computer == 1:
                print("您赢了")
            else:
                return print("您输了")
    else:
        print("您和电脑出的一样")


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入你的选择:")
choice_name=input()
rpsls(choice_name)
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”




# 对程序进行测试
