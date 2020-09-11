class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class bst(object):
    def __init__(self,root):
        self.root=Node(root)
        
    def height(self,current):
        if(current is None):
            return -1
        left_height=self.height(current.left)
        right_height=self.height(current.right)
        return 1+max(left_height,right_height)


if __name__=='__main__':
    tree=bst(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.height(tree.root))
