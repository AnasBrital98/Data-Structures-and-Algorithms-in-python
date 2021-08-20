# Simply Linked List 

### Node :

```python
class Node :
    def __init__(self , data):
        self.data = data
        self.next = None
```

### Simply Linked List :

```python
class SSL :
    
    def __init__(self):
        self.head = None
    
    def insertInTheEnd(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next != None :
            temp = temp.next         
        temp.next = Node(data)
    
    
    def display(self):
        temp = self.head
        while temp != None :
            print("value : ",temp.data) 
            temp = temp.next  
    
    def insertInTheHead(self,data):
        if self.head == None :
            self.head = Node(data) 
            return 
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def delete(self , data):
        if self.head == None :
            return
        if self.head.data == data :
            self.head = self.head.next
        temp2 = self.head
        while temp2.next != None :
            temp1 = temp2
            temp2 = temp2.next
            if temp2.data == data :
                temp1.next = temp2.next
                return
    
    def reverse(self):
        current = self.head
        prev = None
        while current != None : 
            next = current.next
            current.next = prev
            prev = current
            current = next
        if prev is None :
            print("Is None")         
        self.head = prev
```

### Testing Simply Linked List :

```python
SSL = SSL()

SSL.insertInTheEnd(1)
SSL.insertInTheEnd(2)
SSL.insertInTheEnd(3)
SSL.insertInTheEnd(4)
SSL.insertInTheEnd(5)

print("Before reverse : ")
SSL.display()

print("After reverse : ")
SSL.reverse()
SSL.display()
```