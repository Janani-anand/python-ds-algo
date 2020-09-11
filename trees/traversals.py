class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class bst(object):
    def __init__(self,root):
        self.root=Node(root)

    def insertchild(self,child):
        self.inserthelper(self.root,child)

    def inserthelper(self,current,child):
        if(current.value==child):
            return

        if(current is None):
            current=Node(child)

        if(current.value<child):
            if(current.right):
                self.inserthelper(current.right,child)
            else:
                current.right=Node(child)
        if(current.value>child):
            if(current.left):
                self.inserthelper(current.left,child)
            else:
                current.left=Node(child)

    def insertlist(self,elements):
        for i in elements:
            self.insertchild(i)

    def printtree(self,traversal):
        if(traversal=='inorder'):
            ls=self.inordertraversal(self.root,[])
        elif(traversal=='postorder'):
            ls=self.postordertraversal(self.root,[])
        elif(traversal=='preorder'):
            ls=self.preordertraversal(self.root,[])
        else:
            ls=[]
        print(*ls,sep=' ')

    def preordertraversal(self,start,elements):
        if start:
            elements+=[start.value]
            self.preordertraversal(start.left,elements)
            self.preordertraversal(start.right,elements)
        return elements

    def inordertraversal(self,start,elements):
        if start:
            self.inordertraversal(start.left,elements)
            elements+=[start.value]
            self.inordertraversal(start.right,elements)
        return elements

    def postordertraversal(self,start,elements):
        if start:
            self.postordertraversal(start.left,elements)
            self.postordertraversal(start.right,elements)
            elements+=[start.value]
        return elements


if __name__=='__main__':
    tree=bst(1)
    tree.insertlist([2,3,6,4,9])
    tree.printtree('inorder')
    tree.printtree('postorder')
    tree.printtree('preorder')
