class Node :
    
    def __init__(self,data):
        self.data = data
        self.next = None

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