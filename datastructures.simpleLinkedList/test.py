from SimplyLinkedList import SSL

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
