#Task 1.1
class ListNode():
    def __init__(self):
        self.Name = "" #string 
        self.Pointer = 0 #integer 

    def SetName(self, name):
        self.Name = name

    def SetPointer(self, pointer):
        self.Pointer = pointer

    def GetName(self):
        return self.Name

    def GetPointer(self):
        return self.Pointer

class LinkedList():
    def __init__(self):
        self.Node = [None for i in range(11)]
        self.Start = 0 #integer
        self.NextFree = 1 #integer
        for i in range(1, 11):
            self.Node[i] = (i+1)%11 

    def Insert(self, item, p):
        newNode = ListNode()
        newNode.SetName(item)
        #set the pointer for self.NextFree 
        if self.NextFree == p:
            position = self.NextFree
            self.NextFree = self.Node[self.NextFree]
            self.Node[position] = newNode 
        else:
            prev = self.NextFree
            while self.Node[prev] != p:
                prev = self.Node[prev]
                if prev == 0: 
                    return False
            current = self.Node[prev]
            self.Node[prev] = self.Node[current]
            self.Node[current] = newNode
        #set the pointer for self.start 
        if self.Start == 0: #if tthe linked list is empty 
            self.Start = p
        else:
            current = self.Start
            while self.Node[current].GetPointer() != 0:
                current = self.Node[current].GetPointer()
            self.Node[current].SetPointer(p)

    def Delete(self, p):
        if self.Start == p:
            self.Start = self.Node[p].GetPointer()
        else:
            prev = self.Start
            while self.Node[prev].GetPointer() != p:
                prev = self.Node[prev].GetPointer()            
            self.Node[prev].SetPointer(self.Node[self.Node[prev].GetPointer()].GetPointer())
        #set the next free 
        current = self.NextFree
        while self.Node[current] < p:
            current = self.Node[current]
        nextNode = self.Node[current]
        self.Node[current] = p
        self.Node[p] = nextNode

            
l = LinkedList()
print(l.Node) 
l.Insert("a", 1)
l.Insert('b', 2) 
print(l.Node)
print(l.Node[1].GetPointer())
l.Delete(1)
print(l.Node)
print(l.Start)
print(l.NextFree) 
