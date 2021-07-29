class Node :

    def __init__(self , data):
        self.data = data
        self.next = None


class Stack :

    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return 1 if self.size == 0 else 0

    def peek(self):
        return self.head

    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data 

