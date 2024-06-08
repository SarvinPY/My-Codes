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
    def __len__(self):
        return self.size()


s=SinglyLinkedList()
s.append(5)
s.append(23)
s.append(78)
s.append(34)
s.append(5)
s.append(23)
s.append(78)
s.append(34)
s.append(5)
s.append(23)
s.append(78)
s.append(34)
s.show()
print(len(s))