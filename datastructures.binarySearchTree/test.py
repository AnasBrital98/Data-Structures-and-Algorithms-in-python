
from BST import BinarySearchTree

mybSearchTree = BinarySearchTree()

mybSearchTree.Insert(50)
mybSearchTree.Insert(60)
mybSearchTree.Insert(10)
mybSearchTree.Insert(9)
mybSearchTree.Insert(55)
mybSearchTree.Insert(70)
mybSearchTree.Insert(16)

print("Before Delete : ")
mybSearchTree.displayInOrder()

print("After Delete : ")
mybSearchTree.Delete(50)
mybSearchTree.displayInOrder()

print("Maximum Value : ",mybSearchTree.MaxValue())

print("Minimum Value : ",mybSearchTree.MinValue())

print("Size : ",mybSearchTree.Size())
print("Height ",mybSearchTree.Height())
