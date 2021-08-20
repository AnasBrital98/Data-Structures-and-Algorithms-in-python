# Queue : FIFO

### Node :

```python
class Node :
    
    def __init__(self,data):
        self.data = data
        self.next = None
```

### Queue :

```python
class Queue :

    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return 1 if self.size == 0 else 0

    def push(self,data):
        if self.head == None :
            self.head = Node(data)
            self.size += 1
            return
        tmp = self.head
        while tmp.next != None :
            tmp = tmp.next
        tmp.next = Node(data)
        self.size += 1
    def peek(self):
        if self.head == None :
            return None
        tmp = self.head
        while tmp.next != None :
            tmp = tmp.next
        return tmp.data

    def pop(self):
        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return val
```

### Queue Test :

```python
list = Queue()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)

print("Size : ",list.getSize())

print("pop : ",list.pop())
print("pop : ",list.pop())
print("pop : ",list.pop())

print("Size : ",list.getSize())
```