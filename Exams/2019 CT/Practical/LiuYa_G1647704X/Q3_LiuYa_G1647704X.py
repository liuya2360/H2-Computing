#Task 3.1
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList():
    def __init__(self):
        self.start = None

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.start
        self.start = newNode

    def delete(self, data):
        if self.start == None:
            return False
        previous = self.start
        if self.start.data == data:
            self.start = previous.next
            return True 
        while previous.next != None and previous.next.data != data:
            previous = previous.next
        if previous == None:
            return False
        else:
            previous.next = previous.next.next
            return True

    def exist(self, data):
        if self.start == None:
            return False
        else:
            current = self.start
            while current != None and current.data != data:
                current = current.next
            if current == None:
                return False
            else:
                return True 

    def print(self):
        if self.start == None:
            print("LinkList is empty")
        else:
            current = self.start
            temp = []
            while current != None:
                temp.append(current.data)
                current = current.next
            line = "["
            for i in range(len(temp)):
                line = line + str(temp[i])
                if i != len(temp)-1:
                    line = line + ";"
            line = line + "]"
            print(line)

#Task 3.2
ll = LinkList()
ll.insert("ABC")
ll.insert(2)
ll.insert(1)
ll.delete(1)
ll.print()

#Task 3.3
class Post():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print(self):
        print(self.title+":"+self.content)

    def __str__(self):
        return self.title+":"+self.content

class HashTable():
    def __init__(self, size):
        self._size = size
        self._array = [None for i in range(size)]

    def hash(self, title):
        return hash(title)%self._size

    def isFull(self):
        for i in range(self._size):
            if self._array[i] == None:
                return False
        return True 

    def insert(self, newPost):
        target = self.hash(newPost.title)
        if self.isFull():
            return False
        else:
            current = target
            while True:
                if self._array[current]  == None:
                    self._array[current] = newPost
                    return True
                else:
                    current = (current+1)%self._size
                    if current == target:
                        return False

    def getValue(self, title):
        target = self.hash(title)
        current = target
        while True:
            if self._array[current].title == title:
                return self._array[current]
            else:
                current = (current+1)%self._size
                if current == target:
                    return None 

    def getTitles(self):
        titles = []
        for i in range(self._size):
            if self._array[i] != None:
                titles.append(self._array[i].title)
        return titles

#Task 3.4
ht = HashTable(10)
post1 = Post("test1","This is a test")
post2 = Post("number2","Another post")
ht.insert(post1)
ht.insert(post2)
print(str(ht.getValue("test1")))
print(str(ht.getValue("number2")))

#Task 3.5
class User():
    def __init__(self, name, subType):
        self.name = name
        self._friends = LinkList()
        type = {"trial": 10, "basic": 100, "premier": 1000}
        self._posts = HashTable(type[subType])

    def addFriend(self, friend):
        self._friends.insert(friend)
        friend._friends.insert(self)

    def unfriend(self, friend):
        self._friends.delete(friend)
        friend._friends.delete(self)

    def isFriend(self, friend):
        return self._friends.exist(friend)

    def showFriends(self):
        print(self.name + "'s friends:", end="")
        self._friends.print()

    def addPost(self, newPost):
        self._posts.insert(newPost)

    def getTitles(self):
        return self._posts.getTitles()

    def getPosts(self, title):
        return self._posts.getValue(title)

    def __str__(self):
        return str(self.name)

#Task 3.6
john = User("John","trial")
mary = User("Mary","basic")
alan = User("Alan","premier")
john.addFriend(mary)
john.addFriend(alan)
john.showFriends()
mary.showFriends()
alan.unfriend(john)
john.showFriends()
