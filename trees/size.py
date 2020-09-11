class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class bst(object):
    def __init__(self,root):
        self.root=Node(root)

    def size(self,node):
        if node is None:
            return 0
        return 1+self.size(node.left)+self.size(node.right)


if __name__=='__main__':
    tree=bst(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.size(tree.root))
