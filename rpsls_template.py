#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "��":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
    else :
        return print("Error: No Correct Name")


def number_to_name(number):
    if number == 0:
        return"ʯͷ"
    elif number == 1:
        return"ʷ����"
    elif number == 2:
        return"��"
    elif number == 3:
        return"����"
    elif number == 4:
        return"����"

def rpsls(player_choice):
    computer = random.randint(0, 4)

    comouters=number_to_name(computer)
    print("���Ե�ѡ��:%s"%(comouters))

    player_choice = name_to_number(player_choice)

    if player_choice != computer:
        if player_choice >= 2:
            if player_choice - computer == 2 or player_choice - computer == 1:
                print("��Ӯ��")
            else:
                return print("������")
        else:
            player_choice = player_choice + 5
            if player_choice - computer == 2 or player_choice - computer == 1:
                print("��Ӯ��")
            else:
                return print("������")
    else:
        print("���͵��Գ���һ��")


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("���������ѡ��:")
choice_name=input()
rpsls(choice_name)
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
