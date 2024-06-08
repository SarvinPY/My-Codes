import time
class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self,value):
        newNode=Node(value)
        if self.size==0:
            self.tail=newNode
            self.head=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.size+=1
        return self
    def show(self):
        if self.size==0:
            print("List is Empty")
        else:
            print("LinkedList Items: ",end="")
            tempNode=self.head
            while tempNode!=None:
                print(tempNode.value,end=" ")
                tempNode=tempNode.next


# Speed Test !

def timer(func):
    def wrapper(*args,**kwargs):
        x=time.time()
        func(*args,**kwargs)
        y=time.time()
        elapsedTime=y-x
        print(elapsedTime)
    return wrapper

@timer
def f1(n):
    s=list()
    for i in range(n):
        s.append(i)

@timer
def f2(n):
    s=SinglyLinkedList()
    for i in range(n):
        s.append(i)

n=1000000
print("Python List:")
f1(n)
