#printing rows of the board
def printRow(column):
    for i in range (column):
        print(" |  | ", end="")
    print("\n")
    for i in range(column):
        print(" ----", end=" ")
    print("\n")   
#function to mark Player 2's moves and record them to game list
def placementO(coordList, game):
    row = int(coordList[0])
    column = int(coordList[1])
    game[row][column] = 2
#function to mark Player 1's moves and record them to game list
def placementX(coordList, game):
    row = int(coordList[0])
    column = int(coordList[1])
    game[row][column] = 1
#function to draw board and moves after every turn 
def printProgress(game):
    print(" ----", end=" ")
    print(" ----", end=" ")
    print(" ----", end=" ")
    for i in range(3):
        print("\n")
        for j in range(3):
            if game[i][j] == 1:
                print("  X   ", end="")
            elif game[i][j] == 2:
                print("  O  ", end="")
            else:
                print(" |  | ", end="")
        print("\n")
        print(" ----", end=" ")
        print(" ----", end=" ")
        print(" ----", end=" ")
#function that checks the current board to see if a player has won
def winCheck(game):
    # rowChecks
    for r in game:
       
        s = ""
        for c in r:
            s += str(c)
            
            if s == "111":
                #print("X won!")
                return "X won!" 
                pass
            if s == "222":
                print("O won!")
                pass
        print()
    #columnChecks
    a = ""; b = ""; c = ""
    for i in range(3):
   
        a+=str(game[i][0])
        b+=str(game[i][1])
        c+=str(game[i][2])
        
        if a == "111" or b == "111" or c == "111":
            return "X won!" 
            #print("X won!")
        if a == "222" or b == "222" or c == "222":
            print("O won!")
    
    #diagonalChecks
    first = ""; last = ""
    first = str(game[0][0]) + str(game[1][1]) + str(game[2][2])
    last = str(game[0][2]) + str(game[1][1]) + str(game[2][0])
    
    if first == "111" or last == "111":
        return "X won!" 
        #print("X won!")
    if first == "222" or last == "222":
        print("O won!")