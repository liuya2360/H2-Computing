#Rock, paper, scissors, lizard, spock game

p1 = input("Player1? ")
p2 = input("Player2? ")

#Rock = 0, paper = 1, scissors = 2, lizard = 3, spock = 4
#draw = 0, win = 1, lose = -1
check = [[0,-1,1,1,-1],
		[1,0,-1,-1,1],
		[-1,1,0,1,-1],
		[-1,1,-1,0,1],
		[1,-1,1,-1,0]]

l = {"rock": 0,
	"paper": 1,
	"scissors": 2,
	"lizard": 3,
	"spock": 4}

l2 = {0: "Draw",
	-1: "Player 2 wins",
	1: "Player 1 wins"}

a = l[p1]
b = l[p2]

'''
if check[a][b] == 1:
	print("Player 1 wins")
if check[a][b] == -1:
	print("player 2 wins")
else:
	print("Draw")
	'''

print(l2[check[a][b]])