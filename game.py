import random

length = 0
A_num = 0
B_num = 0
player = ""


def player_play():
    print("==========Your Term==========")
    plot()
    global A_num, B_num
    if (player == "A"):
        print("You now at {}".format(A_num + 1))
        print("AI now at {}".format(B_num + 1))
        if (A_num == 0):
            print("You can take a forward step to ", end="")
            if (A_num + 1 == B_num):
                print((A_num + 1) + 2)
            else:
                print((A_num + 1) + 1)
            print("Type \"f\" to take a forward step :")
            command = input()
            while (command != "f"):
                print("Type \"f\" to take a forward step :")
                command = input()
            if (command == "f"):
                if (A_num + 1 == B_num):
                    A_num = A_num + 2
                else:
                    A_num = A_num + 1
        elif ((A_num + 1 == B_num) and B_num == length - 1):
            print(" You can take a backward step to {}".format((A_num + 1) - 1))
            print("Type \"b\" to take a backward step :")
            command = input()
            while (command != "b"):
                print("Type \"b\" to take a backward step :")
                command = input()
            A_num = A_num - 1
        else:
            print("You can take a forward step to ", end="")
            if (A_num + 1 == B_num):
                print((A_num + 1) + 2, end="")
            else:
                print((A_num + 1) + 1, end="")
            print(" or take a backward step to ", end="")
            if (A_num - 1 == B_num):
                print((A_num + 1) - 2)
            else:
                print((A_num + 1) - 1)

            print("Type \"f\" to take a forward step or \"b\" to take a backward step :")
            command = input()
            while (command != "f" and command != "b"):
                print("Type \"f\" to take a forward step or \"b\" to take a backward step :")
                command = input()
            if (command == "f"):
                if (A_num + 1 == B_num):
                    A_num = A_num + 2
                else:
                    A_num = A_num + 1
            else:
                if (A_num - 1 == B_num):
                    A_num = A_num - 2
                else:
                    A_num = A_num - 1
    else:  # player is B
        print("You now at {}".format(B_num + 1))
        print("AI now at {}".format(A_num + 1))
        if (B_num == length - 1):
            print("You can take a forward step to ", end="")
            if (B_num - 1 == A_num):
                print((B_num + 1) - 2)
            else:
                print((B_num + 1) - 1)
            print("Type \"f\" to take a forward step :")
            command = input()
            while (command != "f"):
                print("Type \"f\" to take a forward step :")
                command = input()
            if (command == "f"):
                if (B_num - 1 == A_num):
                    B_num = B_num - 2
                else:
                    B_num = B_num - 1
            print("You are now at {}".format(B_num + 1))
        elif ((B_num - 1 == A_num) and (A_num == 0)):
            print("You can take a backward step to {}".format((B_num + 1) + 1))
            print("Type \"b\" to take a backward step :")
            command = input()
            while (command != "b"):
                print("Type \"b\" to take a backward step :")
                command = input()

            B_num = B_num + 1
            print("You are now at {}".format(B_num + 1))
        else:
            print("You can take a forward step to ", end="")
            if (B_num - 1 == A_num):
                print((B_num + 1) - 2, end="")
            else:
                print((B_num + 1) - 1, end="")
            print(" or take a backward step to ", end="")
            if (B_num + 1 == A_num):
                print((B_num + 1) + 2)
            else:
                print((B_num + 1) + 1)

            print("Type \"f\" to take a forward step or \"b\" to take a backward step :")
            command = input()
            while (command != "f" and command != "b"):
                print("Type \"f\" to take a forward step or \"b\" to take a backward step :")
                command = input()
            if (command == "f"):
                if (B_num - 1 == A_num):
                    B_num = B_num - 2
                else:
                    B_num = B_num - 1
            else:
                if (B_num + 1 == A_num):
                    B_num = B_num + 2
                else:
                    B_num = B_num + 1
            print("You are now at {}".format(B_num + 1))
    print("=============================")


def AI_play():
    print("===========AI Term===========")
    global A_num, B_num
    if (player == "A"):  # AI is B
        if (B_num == length - 1):
            if (B_num - 1 == A_num):
                B_num = B_num - 2
            else:
                B_num = B_num - 1
            print("AI go forward now at {}".format(B_num + 1))
        elif ((B_num - 1 == A_num) and (A_num == 0)):
            B_num = B_num + 1
            print("AI go backward now at {}".format(B_num + 1))
        else:
            command = random.randint(1, 2)
            if (command == 1):
                if (B_num - 1 == A_num):
                    B_num = B_num - 2
                else:
                    B_num = B_num - 1
                print("AI go forward now at {}".format(B_num + 1))
            else:
                if (B_num + 1 == A_num):
                    B_num = B_num + 2
                else:
                    B_num = B_num + 1
                print("AI go backward now at {}".format(B_num + 1))
    else:  # AI is A
        if (A_num == 0):
            if (A_num + 1 == B_num):
                A_num = A_num + 2
            else:
                A_num = A_num + 1
            print("AI go forward now at {}".format(A_num + 1))
        elif ((A_num + 1 == B_num) and B_num == length - 1):
            A_num = A_num - 1
            print("AI go backward now at {}".format(A_num + 1))
        else:
            command = random.randint(1, 2)
            if (command == 1):
                if (A_num + 1 == B_num):
                    A_num = A_num + 2
                else:
                    A_num = A_num + 1
                print("AI go forward now at {}".format(A_num + 1))
            else:
                if (A_num - 1 == B_num):
                    A_num = A_num - 2
                else:
                    A_num = A_num - 1
            print("AI go backward now at {}".format(A_num + 1))
    print("=============================")


def plot():
    for i in range(length):
        if (i != length - 1):
            print(i + 1, end=" ")
        else:
            print(i + 1)
    if (A_num > B_num):  # print B first
        for i in range(B_num):
            print("  ", end="")
        print("B", end="")
        print(" ", end="")
        for i in range(A_num - B_num - 1):
            print("  ", end="")
        print("A")
    else:  # print A first
        for i in range(A_num):
            print("  ", end="")
        print("A", end="")
        print(" ", end="")
        for i in range(B_num - A_num - 1):
            print("  ", end="")
        print("B")


def main():
    global length, A_num, B_num, player
    correct = False
    while not correct:
        print("Chose the length of path (>=3) :")
        length = int(input())
        try:
            if (length >= 3):
                correct = True
        except:
            print("Please type an integer")

    print("You choose path is {}".format(length))
    correct = False
    while not correct:
        print("Chose player (A or B)(A will play first) :")
        player = input()
        if (player == "A" or player == "B"):
            correct = True
        else:
            print("Please type A or B")

    print("You choose {}".format(player))
    A_num = 0
    B_num = length - 1

    stop = False
    while not stop:
        if (player == "A"):
            player_play()
            if (A_num == length - 1 or B_num == 0):
                if ((A_num == length - 1 and player == "A") or (B_num == 0 and player == "B")):
                    print("Player wins!")
                    break
                else:
                    print("AI wins!")
                    break
            AI_play()
            if (A_num == length - 1 or B_num == 0):
                if ((A_num == length - 1 and player == "A") or (B_num == 0 and player == "B")):
                    print("Player wins!")
                    break
                else:
                    print("AI wins!")
                    break
        else:
            AI_play()
            if (A_num == length - 1 or B_num == 0):
                if ((A_num == length - 1 and player == "A") or (B_num == 0 and player == "B")):
                    print("Player wins!")
                    break
                else:
                    print("AI wins!")
                    break
            player_play()
            if (A_num == length - 1 or B_num == 0):
                if ((A_num == length - 1 and player == "A") or (B_num == 0 and player == "B")):
                    print("Player wins!")
                    break
                else:
                    print("AI wins!")
                    break

    plot()


if __name__ == '__main__':
    main()
