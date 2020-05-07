#Please make improvements in comments. 


print("Welcome to the Multi-Player Tic Tac Toe Game by SAI GANESH")
board = [0,1,2,3,4,5,6,7,8]
name1 = input("First Player, enter your name: ")
name2 = input("Second player, enter your name: ")


def decideshape(name1, name2):
        inputshape = input(f'{name1}, please input X or O: ')
        if inputshape.upper() == "O":
            name1, name2 = name2, name1
        print(name1, "will begin first with X")
        print(name2, "will be after", name1, "with O")


def boardprint():
    print(f'{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}')

def checkwinner(i,name1, name2):
    if board[i] == "X":
        print(name1,'wins.')   
    else:
        print(name2, 'wins.')

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
    else:
        return 0

decideshape(name1, name2)
boardprint()
q  = 0
while (q<9):
    positionX = int(input(f'{name1}, which position do you want X to be in? '))
    board[positionX] = "X"
    boardprint()
    if winner(name1, name2):

        break
    else:
        positionO = int(input(f'{name2}, Which position do you want O to be in? '))
        board[positionO] = "O"
        boardprint()
        if winner(name1,name2):
            break
    q += 1
else:
    print("It's a draw")



