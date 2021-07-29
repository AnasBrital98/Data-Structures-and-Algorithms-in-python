
class Node :

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearchTree :

    def __init__(self):
        self.root = None

    def InsertNode(self,root , data):
        if root is None :
            return Node(data)
        if data < root.data :
            root.left = self.InsertNode(root.left,data)       
        elif data > root.data :
            root.right = self.InsertNode(root.right,data)
        else :
            print("Value Already Exist .")
        return root        
    
    def Insert(self,data):
        self.root = self.InsertNode(self.root,data)

    def SearchNode(self,root,data):
        if root is None or root.data == data:
            return root
        if data < root.data :
            return self.SearchNode(root.left,data)    
        elif data > root.data :
            return self.SearchNode(root.right,data)
    
    def Search(self,data):
        if self.SearchNode(self.root,data) is not None:
            print(data," Exist In The Tree ") 
        else :
            print(data," does not existExist In The Tree ")

    def MaxValueOfSubTree(self,node):
        current = node
        while current and current.right :
            current = current.right 
        return current
    def MaxValue(self):
        return self.MaxValueOfSubTree(self.root).data

    def MinValueOfSubTree(self,node):
        current = node
        while current and current.left :
            current = current.left 
        return current       
   
    def MinValue(self):
       return self.MinValueOfSubTree(self.root).data
   
    def max(a,b):
        return a if a>b else b 

    def getHeightOfTree(self,node):
        if node is None:
            return 0
        return 1 + max (self.getHeightOfTree(node.left),self.getHeightOfTree(node.right))

    def Height(self):
        return self.getHeightOfTree(self.root)

    def getSizeOfTree(self,node):
        if node is None:
            return 0
        return self.getSizeOfTree(node.left) + self.getSizeOfTree(node.right) + 1

    def Size(self):
        return self.getSizeOfTree(self.root)

    def RemoveNode(self,node,data):
        if node is None:
            return node
        if data < node.data :
            node.left = self.RemoveNode(node.left,data) 
        elif data > node.data :
            node.right = self.RemoveNode(node.right,data)
        else :
            if node.left is None :
                return node.right
            if node.right is None :
                return node.left
            tmp = self.MaxValueOfSubTree(node.right)
            node.data = tmp.data
            node.right = self.RemoveNode(node.right,tmp.data)
        return node    

    def Delete(self,data):
        self.root = self.RemoveNode(self.root,data)

    def InOrder(self,root):
        if root is not None :
            self.InOrder(root.left)
            print("Value : ",root.data)
            self.InOrder(root.right)

    def RemoveTheEntireTree(self,node):
        if node is None :
            return
        self.RemoveTheEntireTree(node.left)
        self.RemoveTheEntireTree(node.right)
        print("Deleting ",node.data," .")
        node = None
    
    def RemoveTree(self):
        self.RemoveTheEntireTree(self.root)
        self.root = None    

    def displayInOrder(self):
        self.InOrder(self.root)

    def PreOrder(self,root):
        if root is not None :
            print("Value : ",root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def displayPreOrder(self):
        self.PreOrder(self.root)

    def PostOrder(self,root):
        if root is not None :
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print("Value : ",root.data)
            
    def displayPostOrder(self):
        self.PostOrder(self.root)
    

