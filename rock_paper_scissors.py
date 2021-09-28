while True:
    a= input("player 1 enter rock, paper, scissors as r,p,s ")
    b= input("player 2 enter rock, paper, scissors as r,p,s")
    if(a==b):
        print("It is a tie")
        x= input("new game ?  y/n")
        if(x=='y'):
            continue
        else:
            break
    elif(a=='s'):
        if(b=='p'):
            print("player 1 is the winner")
            x = input("new game ?  y/n")
            if (x == 'y'):
                continue
            else:
                break
        else:
            print("player 2 is the winner")
            x = input("new game ?  y/n")
            if (x == 'y'):
                continue
            else:
                break
    elif (a =='r'):
        if (b == 's'):
            print("player 1 is the winner")
            x = input("new game ?  y/n")
            if (x == 'y'):
                continue
            else:
                break
        else:
            print("player 2 is the winner")
            x = input("new game ?  y/n")
            if (x == 'y'):
                continue
            else:
                break
    elif(a =='p'):
        if (b == 'r'):
            print("player 1 is the winner")
            x = input("new game ?  y/n")
            if (x == 'y'):
                continue
            else:
                break
        else:
            print("player 2 is the winner")
            x = input("new game ?  y/n")
            if (x == 'y'):
                continue
            else:
                break
    else:
        print("invalid input")