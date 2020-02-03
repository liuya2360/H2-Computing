'''
def makeStack(n):
    size = n;
    return []

def push(stack, data):
    if len(stack) < n:
        stack.append(data)

def pop(stack):
    if len(stack):
        return stack.pop

def isFull(stack):
    return len(stack) == n

def isEmpty(stack):
    return len(stack) == 0
'''

def makeStack():
    stack = [None] * 10 
    top = -1
    return [stack, top]

def isEmpty(s) 
