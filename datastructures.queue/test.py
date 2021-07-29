from queue import Queue

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