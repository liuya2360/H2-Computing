#Task 1.1 
class Node():
    def __init__(self):
        self.Data = None 
        self.LeftP = 0
        self.RightP = 0

class BinaryTree():
    def __init__(self):
        self.ThisTree = [Node() for i in range(21)]
        self.Root = 0
        self.NextFreePosition = 1
        for i in range(1, 21):
            self.ThisTree[i].LeftP = (i+1)%20 

    #Task 1.2
    def AddItemToBinaryTree(self, NewFreeItem):
        if self.Root == 0:
            self.Root = self.NextFreePosition 
            self.ThisTree[self.Root].Data = NewFreeItem
            self.NextFreePosition = self.ThisTree[self.NextFreePosition].LeftP
            self.ThisTree[self.Root].LeftP = 0 
        else:
            #check if the array is full or not
            if self.NextFreePosition == 0:
                print("The binary tree is full")
                return
            #insert NewFreeItem 
            CurrentPosition = self.Root
            PreviousPosition = CurrentPosition 
            LastMove = 'X'
            while CurrentPosition != 0: 
                PreviousPosition = CurrentPosition 
                if NewFreeItem < self.ThisTree[CurrentPosition].Data:
                    LastMove = 'L'
                    CurrentPosition = self.ThisTree[CurrentPosition].LeftP
                else:
                    LastMove = 'R'
                    CurrentPosition = self.ThisTree[CurrentPosition].RightP
            if LastMove == 'R':
                self.ThisTree[PreviousPosition].RightP = self.NextFreePosition
                self.ThisTree[self.ThisTree[PreviousPosition].RightP].Data = NewFreeItem 
                self.NextFreePosition = self.ThisTree[self.NextFreePosition].LeftP 
                self.ThisTree[self.ThisTree[PreviousPosition].RightP].LeftP = 0 
            else:
                self.ThisTree[PreviousPosition].LeftP = self.NextFreePosition
                self.ThisTree[self.ThisTree[PreviousPosition].LeftP].Data = NewFreeItem
                self.NextFreePosition = self.ThisTree[self.NextFreePosition].LeftP 
                self.ThisTree[self.ThisTree[PreviousPosition].LeftP].LeftP = 0 

    #Task 1.3
    def OutputData(self):
        print("Root: "+str(self.Root))
        print("NextFreePosition"+str(self.NextFreePosition))
        for i in range(1, 21):
            print("Index:{}, Data:{}, LeftP:{}, RightP:{}".format(i, self.ThisTree[i].Data, self.ThisTree[i].LeftP, self.ThisTree[i].RightP)) 

    #Task 1.6
    def InOrder(self):
        InOrderRec(self.Root)

    def InOrderRec(self, current):
        if current = 0:
            return
        else:
            InOrderRec(self.ThisTree[current].LeftP)
            print("Index:{}, Data:{}, LeftP:{}, RightP:{}".format(i, self.ThisTree[i].Data, self.ThisTree[i].LeftP, self.ThisTree[i].RightP))
            InOrderRec(self.ThisTree[current].RightP) 
    
#Task 1.4
BT = BinaryTree()
while True:
    newdata = input()
    if newdata == "XXX":
        break 
    BT.AddItemToBinaryTree(newdata)
BT.OutputData()
BT.InOrder() 



a = BinaryTree()
a.AddItemToBinaryTree(1)
a.AddItemToBinaryTree(2)
print("next free position is",a.NextFreePosition)

a.OutputData() 

for i in range(21):
    print(i, a.ThisTree[i].Data)
    
