from DLL import DoublyLinkedList


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
