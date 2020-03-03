import random 

class cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bomb = False
        self.neighbour_bomb = 0

    def setBomb(self):
        self.bomb = True

    def isBomb(self):
        return self.bomb

    def addNeighbourBomb(self):
        self.neighbour_bomb += 1 

    def __str__(self):
        if not self.bomb: 
            return str(self.neighbour_bomb)
        else:
            return "X" 
    
class game():
    def __init__(self, size):
        self.size = size
        self.grid = [[cell(i, j) for j in range(size)] for i in range(size)]
        self.check = [[False for j in range(size)] for i in range(size)]
        self.score = 0
        self.no_bomb = None 
        
    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.check[i][j]:
                    print(str(self.grid[i][j])+" ", end="")
                else:
                    print("- ", end="") 
            print()
        if self.score: 
            print("Your Score is {}".format(self.score)) 

    def placeBomb(self, k):
        self.no_bomb = k 
        for i in range(k): 
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            #print(x, y) 
            self.grid[x][y].setBomb()
            
            #update points around the bomb 
            if x > 0:
                self.grid[x-1][y].addNeighbourBomb()
                if y > 0:
                    self.grid[x-1][y-1].addNeighbourBomb()
                if y < self.size-1:
                    self.grid[x-1][y+1].addNeighbourBomb() 
            if x < self.size-1:
                self.grid[x+1][y].addNeighbourBomb()
                if y > 0:
                    self.grid[x+1][y-1].addNeighbourBomb()
                if y < self.size-1:
                    self.grid[x+1][y+1].addNeighbourBomb() 
            if y > 0:
                self.grid[x][y-1].addNeighbourBomb()
            if y < self.size-1:
                self.grid[x][y+1].addNeighbourBomb()

    def checkBomb(self, x, y):
        if self.grid[x][y].isBomb():
            print("Game over! You've hit the bomb at: ({},{}).".format(x+1,y+1)) #game is 1 indexing 
            print("Your Score is {}".format(self.score))
            return False 

        else:
            self.check[x][y] = True
            if self.score == pow(self.size, 2) - self.no_bomb:
                self.display()
                self.displayScore() 
                Print("Congratulations! You have won!")
                return False
            return True

    def displayScore(self):
        print("Your score is: {}.".format(self.score)) 

print("Welcome to MineSweeper!\nLet's start the game!")
while True:
    difficulty_level = input("Please select the level of difficulty ([B]eginer, [I]ntermediate, or [E]xpert)")
    if difficulty_level.upper() == "B":
        grid_size = 5
        no_bombs = 3
    elif difficulty_level.upper() == "I":
        grid_size = 6
        no_bombs = 8
    elif difficulty_level.upper() == "E":
        grid_size = 8
        no_bombs = 20
    else:
        continue

    myGame = game(grid_size)
    myGame.placeBomb(no_bombs) 
    myGame.display() 
    while True:
        print("Enter your cell you want to open:")
        x = int(input("X (1 to {}): ".format(grid_size))) -1
        y = int(input("Y (1 to {}): ".format(grid_size))) -1
        if myGame.checkBomb(x, y):
            myGame.display()
            myGame.displayScore()
        else:
            break

    #check with the user if he want to start another game
    flag = input(print("Do you want to try again? ([Y]es or [N]o)"))
    if flag.upper() == "Y":
        continue
    else:
        break 
