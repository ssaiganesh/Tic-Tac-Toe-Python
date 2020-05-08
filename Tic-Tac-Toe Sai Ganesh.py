#Please make improvements in comments. 

import random

#this function decides shape of player(s)/computer
def decideshape(name1, name2):
    while True:
        inputshape = input(f'{name1}, please input X or O: ')
        if inputshape.upper() == "O" or inputshape.upper() == "X":
            if inputshape.upper() == "O":
                name1, name2 = name2, name1
                computershape = "X"
                break
            else:
                computershape = "O"
                break
        else:
            print("Invalid Input. Try again.")
    
    print(name1, "will begin first with X")
    print(name2, "will be after", name1, "with O")
    return (name1,name2,computershape)

#this function prints the tic-tac-toe board
def boardprint():
    print(f'\n{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}\n')

#this function helps the program to check who has won   
def checkwinner(i,name1, name2):
    if board[i] == "X":
        print(name1,'wins.Thanks for playing.')   
    else:
        print(name2, 'wins. Thanks for playing.')

#this function helps the program to place its shape at a random position if required
def computerrandom():
     while True:
            value = random.randint(0,8) #this is for random computer position
            if board[value] == value:
                board[value] = computershape
                break

#this function decides the computer move for single player
def computermove(computershape):
    if board[4] == board[8] or board[3] == board[6] or board[1] == board[2]:
        if board[0] == 0:
            board[0] = computershape
        else:
            computerrandom()

    elif board[0] == board[2] or board[4] == board[7]:
        if board[1] == 1:
            board[1] = computershape
        else:
            computerrandom()

    elif board[0] == board[1] or board[5] == board[8] or board[4] == board[6]:
        if board[2] == 2:
            board[2] = computershape
        else:
            computerrandom()
    
    elif board[0] == board[6] or board[4] == board[5]:
        if board[3] == 3:
            board[3] = computershape
        else:
            computerrandom()
    
    elif board[1] == board[7] or board[3] == board[5] or board[0] == board[8] or board[2] == board[6]:
        if board[4] == 4:
            board[4] = computershape
        else:
            computerrandom()
        
    elif board[2] == board[8] or board[3] == board[4]:
        if board[5] == 5:
            board[5] = computershape
        else:
            computerrandom()
        
    elif board[0] == board[3] or board[7] == board[8] or board[2] == board[4]:
        if board[6] == 6:
            board[6] = computershape
        else:
            computerrandom()
    
    elif board[1] == board[4] or board[6] == board[8]:
        if board[7] == 7:
            board[7] = computershape
        else:
            computerrandom()

    elif board[0] == board[4] or board[2] == board[5] or board[6] == board[7]:
        if board[8] == 8:
            board[8] = computershape
        else:
            computerrandom()

    else:
        computerrandom()
       

def winner(name1, name2):
    if board[0] == board[1] == board[2]:
        checkwinner(0,name1,name2)
        
    elif board[0] == board[3] == board[6]:
        checkwinner(0,name1,name2)
        
    elif board[0] == board[4] == board[8]:
        checkwinner(0,name1,name2)
        
    elif board[1] == board[4] == board[7]:
        checkwinner(1,name1,name2)
        
    elif board[2] == board[5] == board[8]:
        checkwinner(2,name1,name2)
        
    elif board[2] == board[4] == board[6]:
        checkwinner(2,name1,name2)
        
    elif board[3] == board[4] == board[5]:
        checkwinner(3,name1,name2)
        
    elif board[6] == board[7] == board[8]:
        checkwinner(6,name1,name2)
        
    else:
        return 0
    
def checkboard(s):
    while True:
        if s=="X":
            positionX = int(input(f'{name1}, which position do you want X to be in? '))
            if board[positionX] == positionX:
                board[positionX] = s
                break
            else:
                print("Invalid Input. Try Again.")
            
        elif s == "O":
            positionO = int(input(f'{name2}, which position do you want O to be in? '))
            if board[positionO] == positionO:
                board[positionO] = s
                break
            else:
                print("Invalid Input. Try Again.")



replay = True
while replay:
    print("Welcome to the Tic Tac Toe Game by SAI GANESH")
    board = [0,1,2,3,4,5,6,7,8]
    while True:
        name1 = input("First Player, enter your name: ")
        if not name1.strip():
            print("Invalid. Try again")
        else:
            break
        
        #This block of code confirms if user is playing with computer or another player
    while True:
        playchoice = input(name1+", will you be playing Multi-player(M) or Single-player(S). ")
        if playchoice.upper().startswith("M"):
            while True:
                name2 = input("Second Player, enter your name: ")
                if not name2.strip():
                    print("Invalid. Try again")
                else:
                    break
            break
        elif playchoice.upper().startswith("S"):
            name2 = "Computer"
            break
        else:
            print("Invalid Input. Try again.")
    
    name1, name2, computershape = decideshape(name1,name2) 
    boardprint()
    q  = 0
    while True:
        if playchoice.upper().startswith("M"):
            checkboard("X")
            boardprint()
            q+=1
            if winner(name1, name2) != 0:
                break
            elif q == 9:
                print("It's a draw.")
                break
            else:
                checkboard("O")
                boardprint()
                q += 1
                if winner(name1,name2) != 0:
                    break
        elif playchoice.upper().startswith("S"):
            if computershape == "X":
                computermove(computershape)
                boardprint()
                q+=1
                if winner(name1, name2) != 0:
                    break
                elif q == 9:
                    print("It's a draw.")
                    break
                else:
                    checkboard("O")
                    boardprint()
                    q += 1
                    if winner(name1,name2) != 0:
                        break
        
            elif computershape == "O":
                checkboard("X")
                boardprint()
                q+=1
                if winner(name1,name2) != 0:
                    break
                elif q == 9:
                    print("It's a draw.")
                    break
                else:
                    computermove(computershape)
                    print("Computer is thinking..")
                    boardprint()
                    q+=1
                    if winner(name1, name2) != 0:
                        break
    replay_input = input("Would you like to play again? Y/N: ")
    if replay_input.upper().startswith("N"):
        break
    elif replay_input.upper().startsiwth("Y"):
        print("Game will now restart.")
