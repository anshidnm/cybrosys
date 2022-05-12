import random
def guess():
    num = random.randint(1000, 9999)
    print(num)
    tr = True
    con = "y"
    while con == "y" or con == "Y":
        while tr == True:
            try:
                inp = int(input("enter a 4 digit number\n"))
                tr = False
            except ValueError:
                print("please enter a valid number")
        strnum = str(num)
        strinp = str(inp)
        rcount=0
        tcount=0
        for i in range(0, 4):
            if len(strinp) != 4:
                print("Number is not a 4 digit number....try again")
                break
            elif strnum == strinp:
                print('you win......!')
                con=input("press y for continue game or press n to exit game:\n")
                a = True
                while a == True:
                    if con == "y" or con == "Y" or con == "n" or con == "N":
                        a = False
                    else:
                        print("Invalid input....try again")
                        con = input("press y for continue game or press n to exit game:\n")
                    if con == "n" or con == "N":
                        print("Thank you")
                        exit()
                    else:
                        guess()

            elif strinp[i] == strnum[i]:
                rcount=rcount+1
                print('you got rabbit ' + 'at', (i + 1), "th position")
            elif strinp[i] in strnum:
                tcount = tcount + 1
                print('you got tortoise ' + 'at', (i + 1), "th position")
        print("you got total ",rcount," rabbit\nyou got total",tcount,"tortoise")
        con = input("press y for continue game or press n to exit game:\n")
        a = True
        while a == True:
            if con == "y" or con == "Y" or con == "n" or con == "N":
                a = False
            else:
                print("Invalid input....try again")
                con = input("press y for continue game or press n to exit game:\n")
        if con == "n" or con == "N":
            print("Thank you")
            exit()
        tr = True


guess()
