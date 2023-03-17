"""binary search tree(BST)"""

class BTSNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) :
        self.root = None

    def is_empty(self) :
        if self.root == None:
            return True
        else:
            return False

    def insert(self, data) :
    #insert data into BST
        pNew = BTSNode(data)
        if self.root == None:
            self.root = pNew
            return

        pos = self.root
        while pos is not None:
            if data < pos.data:
                if pos.left is None:
                    pos.left = pNew
                    return
                else:
                    pos = pos.left

            else:
                if pos.right is None:
                    pos.right = pNew
                    return
                else:
                    pos = pos.right

        
    def delete(self, de_data):
        #delete data from BST
        prev = None
        start = self.root
        while start != None:
            if start.data == de_data:
                break
            elif start.data > de_data:
                prev = start
                start = start.left
            elif start.data < de_data:
                prev = start
                start = start.right
        if start == None:
            return None
        
        if start.left == None and start.right == None:
            if start == self.root:
                self.root = None
            elif prev.left == start:
                prev.left = None
            elif prev.right == start:
                prev.right = None
        
        elif start.left != None and start.right == None:
            if start == self.root:
                self.root = start.left
            elif prev.left == start:
                prev.left = start.left
            elif prev.right == start:
                prev.right = start.left
        
        elif start.left == None and start.right != None:
            if start == self.root:
                self.root = start.right
            elif prev.left == start:
                prev.left = start.right
            elif prev.right == start:
                prev.right = start.right
        
        else:
            king = start
            maxleft = start.left

            while maxleft.right != None:
                king = maxleft
                maxleft = maxleft.right
            
            start.data = maxleft.data

            if king.right == maxleft:
                king.right = maxleft.left
            else:
                king.left = maxleft.left


    def preorder(self, root):
        #preorder traversal
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        #inorder traversal
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        #postorder traversal
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def traverse(self):
        #call preorder(), inorder(), postorder()
        print("Preorder : ", end="")
        self.preorder(self.root)
        print()
        print("Inorder : ", end="")
        self.inorder(self.root)
        print()
        print("Poseorder : ", end="")
        self.postorder(self.root)
        print()

    def findMin(self):
        #return minimum value
        if self.root == None:
           return None
        else:
            start = self.root
            while start.left is not None:
                start = start.left
            return start.data

    def findMax(self):
        #return maximum value
        if self.root == None:
            return None
        else:
            start = self.root
            while start.right is not None:
                start = start.right
            return start.data


myBST = BST()
myBST.insert(14); myBST.insert(23)
myBST.insert(7); myBST.insert(10)
myBST.insert(33); myBST.insert(5)
myBST.insert(20); myBST.insert(13)
myBST.delete(5)
myBST.delete(33)
myBST.delete(14)
myBST.delete(7)
myBST.delete(23)
myBST.traverse()
#myBST.delete(33)
#myBST.traverse()
#print("Min: ", myBST.findMin())
#print("Max: ", myBST.findMax())