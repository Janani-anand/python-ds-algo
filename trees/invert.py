class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class bst(object):
    def __init__(self,root):
        self.root=Node(root)

    def invert(self,node):
        if node==None:
            return
        else:
            temp=node
            self.invert(node.left)
            self.invert(node.right)
            temp=node.left
            node.left=node.right
            node.right=temp

    def inorder_print(self):
        ls=self.inordertraversal(self.root,[])
        print(*ls,sep=' ')


    def inordertraversal(self,start,elements):
        if start:
            self.inordertraversal(start.left,elements)
            elements+=[start.value]
            self.inordertraversal(start.right,elements)
        return elements


if __name__=='__main__':
    tree=bst(2)
    tree.root.left = Node(1)
    tree.root.right = Node(4)
    tree.root.right.left = Node(3)
    tree.root.right.right = Node(5)
    tree.inorder_print()
    tree.invert(tree.root)
    tree.inorder_print()
