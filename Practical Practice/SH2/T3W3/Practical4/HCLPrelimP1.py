#Q3
#Task 3.1
class ListNode():
    def __init__(self):
        self.Name = None
        self.Pointer = None

    def SetName(self, name):
        self.Name = name

    def SetPointer(self, pointer):
        self.Pointer = pointer

    def GetName(self):
        return self.Name

    def GetPointer(self): 
        return self.Pointer

    def __str__(self):
        return self.Name 

class LinkedList():
    def __init__(self):
        self.Node = [ListNode() for i in range(11)]
        self.Start = -1 
        self.NextFree = 1
        for i in range(1, 9):
            self.Node[i].SetPointer(i+1)
        self.Node[10].SetPointer(0)

    def IsEmpty(self):
        return self.Start == -1

    def IsFull(self):
        return self.NextFree == 0 

    def Insert(self, name, position):
        if self.IsEmpty(): 
            self.Start = self.NextFree
            temp_next_free_pointer = self.Node[self.NextFree].GetPointer() 
            self.Node[self.NextFree].SetName(name)
            self.Node[self.NextFree].SetPointer(0)
            self.NextFree = temp_next_free_pointer
        elif self.IsFull():
            pass             
        else:
            previous = self.Start
            count = 0
            while count < position - 1:
                previous = self.Node[previous].GetPointer()
                count += 1 
            temp_next_free_pointer = self.Node[self.NextFree].GetPointer() 
            self.Node[self.NextFree].SetName(name)
            if position == 1:
                self.Node[self.NextFree].SetPointer(self.Start)
                self.Start = self.NextFree 
            else: 
                self.Node[self.NextFree].SetPointer(self.Node[previous].GetPointer())
                self.Node[previous].SetPointer(self.NextFree)
            self.NextFree = temp_next_free_pointer

    def Delete(self, position):
        if self.IsEmpty():
            pass
        else:
            count = 0
            previous = self.Start 
            while count < position - 1: 
                count += 1
                previous = self.Node[previous].GetPointer()
            target = self.Node[previous].GetPointer()
            self.Node[target].SetName(None) 
            self.Node[previous].SetPointer(self.Node[target].GetPointer())
            #insert the deleted node (target) to nextfree linked list
            previous = self.NextFree
            while self.Node[previous].GetPointer() < target:
                previous = self.Node[previous].GetPointer()
            temp_next = self.Node[previous].GetPointer() 
            self.Node[previous].SetPointer(target)
            self.Node[target].SetPointer(temp_next)

    def Display(self):
        print("Start: " + str(self.Start))
        print("NextFree: " + str(self.NextFree))
        for i in range(1, 11):
            if self.Node[i].GetName() != None:
                print(self.Node[i].GetName(), end = " ")
        print()

    def Display2(self):
        current = self.Start
        while self.Node[current].GetPointer() != 0:
            print(self.Node[current].GetName()+" "+str(current)+" "+str(self.Node[current].GetPointer()), end=" ") 
            current = self.Node[current].GetPointer()
        print(self.Node[current].GetName()+" "+str(current)+" "+str(self.Node[current].GetPointer()), end=" ") 
        print()

l = LinkedList()
l.Insert('Ali', 1)
l.Insert('Jack', 1)
l.Insert('Ben', 2)
l.Insert('Me', 2) 
l.Display2() 
l.Delete(1)
l.Insert('Jane', 2)
l.Display2() 
l.Insert('Ken', 3)

l.Delete(2) 
l.Display()

