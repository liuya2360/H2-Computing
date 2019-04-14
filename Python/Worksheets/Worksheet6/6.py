fileHandle = open("DATA.TXT")

class student():
    def __init__(self, name, score1, score2, score3, score4):
        self.name = name
        self.score1 = int(score1)
        self.score2 = int(score2)
        self.score3 = int(score3)
        self.score4 = int(score4)
    
    def overall_score(self):
        return (0.1*self.score1 + 0.15*self.score2 + 0.25*self.score3 + 0.5*self.score4 + 0.5) // 1

L = []
for row in fileHandle:
    row = row.strip().split(",")
    L.append(student(row[0],row[1],row[2],row[3],row[4]))

while True:
    search = input("Do you want to perform a search? \n")

    if search.lower() == "no":
        break

    category = input("Which category do u want to search in? \n[0].Overall score\n[1].Test score 1\n[2].Test score 2\n[3].Test score 3\n[4].Test score 4\n")
    parameter = int(input("Which score are you searching for? \n"))
    for i in range(len(L)):
        if category == "0":
            temp = L[i].overall_score()
        elif category == "1":
            temp = L[i].score1
        elif category == "2":
            temp = L[i].score2
        elif category == "3":
            temp = L[i].score3
        elif category == "4":
            temp = L[i].score4
                        
        if temp == parameter:
            print(L[i].name)