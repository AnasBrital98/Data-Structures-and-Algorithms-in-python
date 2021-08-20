# Doubly Linked List 

### Node :

```python
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
```

### Doubly Linked List :

```python
class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insertInTheHead(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node
    def insertInTheEnd(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        tmp = self.head
        while tmp.next is not None :
            tmp = tmp.next
        node = Node(data)
        node.prev = tmp
        tmp.next = node
    def display(self):
        if self.head is None:
            print("The List Is Empty .")
            return
        tmp = self.head
        while tmp is not None :
            print("Value : ",tmp.data) 
            tmp = tmp.next
    def Search(self,data):
        if self.head is None:
            return 0
        tmp = self.head
        while tmp is not None :
            if tmp.data == data :
                return 1
            tmp = tmp.next
        return 0 
    def delete(self,data):
        if self.head is None:
            return 0
        if self.head.data == data:
            node = self.head.next
            node.prev = None
            self.head = node
            return 1
        tmp = self.head.next
        while tmp.next is not None :
            if tmp.data == data :
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                return 1
            tmp = tmp.next    
        if tmp.data == data:
            tmp.prev.next = tmp.next 
            return 1 
        self.head = tmp                 
        return 0
    def maxValue(self):
        if self.head is None:
            return None
        max = self.head.data
        tmp = self.head.next
        while tmp is not None :
            if tmp.data > max :
                max = tmp.data
            tmp = tmp.next
        return max        
    def minValue(self):
        if self.head is None:
            return None
        min = self.head.data
        tmp = self.head.next
        while tmp is not None :
            if tmp.data < min :
                min = tmp.data
            tmp = tmp.next
        return min 
```

### Testing Doubly Linked List :

```python
list = DoublyLinkedList()

list.insertInTheEnd(1)
list.insertInTheEnd(2)
list.insertInTheEnd(3)
list.insertInTheEnd(4)
list.insertInTheEnd(5)


print( "Element in The List : ")
list.display()

print("Maximum Value : ",list.maxValue())
print("Minimum Value : ",list.minValue())
```