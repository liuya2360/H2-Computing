#Q1
#Task 1.1
import random 

class IslandClass():
    def __init__(self):
        self.grid = [['.' for i in range(30)] for j in range(10)]

    def GetSquare(self, row, column):
        return self.grid[row][column]

    def DisplayGrid(self): 
        temp = "" 
        for i in range(10):
            for j in range(30):
                temp = temp + self.GetSquare(i, j) 
            temp = temp + "\n"
        print(temp, end="")

    #Task 1.2 
    def HideTreasure(self):
        temp = []
        while len(temp) < 3:
            newSquare = [random.randint(0,9), random.randint(0, 30)]
            if newSquare not in temp:
                temp.append(newSquare)
        for i in range(3): 
            self.grid[temp[i][0]][temp[i][1]] = 'T'

    def DigHole(self, row, column):
        if self.GetSquare(row, column) == "T":
            self.grid[row][column] = "X"
        else:
            self.grid[row][column] = "O"
            
#Task 1.3 
game = IslandClass()
game.HideTreasure() 
game.DisplayGrid() 
#Task 1.5
while True: 
    row_input = int(input("Please input a row (between 0 to 9) to dig:")) 
    if row_input >=0 and row_input <= 9:
        break
while True: 
    col_input = int(input("Please input a column (between 0 to 29) in the row to dig:")) 
    if col_input >= 0 and col_input <= 29:
        break
game.DigHole(row_input, col_input)
game.DisplayGrid()
