##2019 CT computing revision

''' ------------- Worksheet 6 -------------- '''
#Search Algorithm 
#linear search 
def linear_search(L, t): 


#binary search 
def binary_search(L, t): 



''' ------------- Worksheet 7 -------------- '''
#k2d
def k2d(s, k):



def d2k(d, k): 



''' ------------- Worksheet 8 -------------- '''
#sort algorithm 
#bubble sort 
def bubbleSort(L): 



#insertion sort 
def insertion sort(L): 



#quicksort 
def quickSort(L): 




''' ------------- Worksheet 9 -------------- '''
#linked list
class Node():
	def __init__(self, data): 



#singly linked list(SLLL)
class SLLL(): 
	def __init__(self):


	def getRoot(self): 


	def setRoot(self, node): 


	def isEmpty(self): 



	def insertFront(self, data): 



	def insertBack(self, data): 



	def exists(self, data): 



	def delete(self, data):




#doubly linked list(DLLL)
class DLLL(SLLL): 
	def insertFront(self, data): 



	def insertBack(self, data): 



	def delete(self, data): 




#doubly linked circular list(DLCLL)
class DLCLL(DLLL): 
	def setRoot(self, node): 



	def insertFront(self, data): 
	


	def insertBack(self, data): 



	def delete(self, data): 



''' ------------- Worksheet 10 -------------- '''
#stack and queue 
#stack
class stack(): 
	def __init__(self, size): 



	def isFull(self): 



	def isEmpty(self): 



	def push(self, data): 



	def pop(self): 



	def peek(self):



#queue 
class queue(): 
	def __init__(self, size): 



	def isFull(self):



	def isEmpty(self): 


	def enqueue(self, data): 


	def dequeue(self): 



	def peek(self): 



''' ------------- Worksheet 11 -------------- '''
#binary search tree 
class Node_bst(): 
	def __init__(self, data): 



class BST(): 
	def __init__(self):



	def insert(self, data):



	def insertRec(self, data, current): 



	def insertItr(self, data): 



	def exists(self, data): 



	def inOrder(self): 



	def inOrderRec(self, current): 



	def preOrder(self): 



	def preOrderRec(self, current): 



	def postOrder(self): 



	def postOrderRec(self, current): 




''' ------------- Worksheet 12 -------------- '''
#hash table 
#open addressing 
class HashTable(): 
	def __init__(self, size): 



	def hash(self, data): 



	def isFull(self): 



	def isEmpty(self): 



	def insert(self, data): 



	def exists(self, data): 



	def delete(self, data): 



#separate lining using DLLL 
class HashTable2(HashTable): 
	def __init__(self, size): 



	def isFull(self): 



	def isEmpty(self): 



	def insert(self, data): 
	


	def exists(self, data): 



	def delete(self, data): 




