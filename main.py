from myfile import printRow, placementO, placementX, printProgress, winCheck
from array import *

#drawing the board
rows = int(input("How many rows would you like? "))
columns = int(input("How many columns would you like? "))

for i in range(columns):
    print(" ----", end=" ")
print("\n")

for i in range(rows):
    printRow(columns)
    
#setting up list for board values, 0 = blank, 1 = X, 2 = O
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#gameplay, receiving inputs from player
for i in range(4):
    # Player 1 = X
    marker = input("Player 1, enter your next move in the row, column order ")
    counter = marker.split(",")
    game[int(counter[0])][int(counter[1])] = 1
    placementX(counter, game)
    printProgress(game)
    if((winCheck(game)) == "X won!"):
        print(winCheck(game))
        break
    #Player 2 = O
    marker1 = input("Player 2, enter your next move in the row, column order ")
    counter1 = marker1.split(",")
    game[int(counter1[0])][int(counter1[1])] = 2
    placementO(counter1, game)
    printProgress(game)
    winCheck(game)

winCheck(game)