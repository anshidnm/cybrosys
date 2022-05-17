import random

name = input("Enter your name : ")
usr_score = 0
com_score = 0


def input_function():
    global com_score
    global usr_score
    global name

    def exit_fun():
        global com_score
        global usr_score
        global name
        if com_score == 3:
            print("Computer win")
            exit()
        elif usr_score == 3:
            print(name, " win")
            exit()

    random_guess = random.randint(1, 3)
    print(random_guess)
    print("options\n.............\n1.Rock\n2.Paper\n3.Scissors")
    loop_var = True
    while loop_var:
        try:
            user_guess = int(input("Enter your option :"))
            if user_guess not in range(1, 4):
                print("Invalid option")
            else:
                loop_var = False
        except ValueError:
            print("Please type a valid Number")
    if user_guess == random_guess:
        print("Tied")
        input_function()
    if user_guess == 1:
        if random_guess == 2:
            com_score = com_score + 1
            print("Computer get 1 point..Total :", com_score)
            exit_fun()
            input_function()
        elif random_guess == 3:
            usr_score = usr_score + 1
            print(name," get 1 point..Total :", usr_score)
            exit_fun()
            input_function()
    elif user_guess == 2:
        if random_guess == 1:
            usr_score = usr_score + 1
            print(name, " get 1 point..Total :", usr_score)
            exit_fun()
            input_function()
        elif random_guess == 3:
            com_score = com_score + 1
            print("Computer get 1 point..Total :", com_score)
            exit_fun()
            input_function()
    elif user_guess == 3:
        if random_guess == 1:
            com_score = com_score + 1
            print("Computer get 1 point..Total :", com_score)
            exit_fun()
            input_function()
        elif random_guess == 2:
            usr_score = usr_score + 1
            print(name, " get 1 point..Total :", usr_score)
            exit_fun()
            input_function()


input_function()
