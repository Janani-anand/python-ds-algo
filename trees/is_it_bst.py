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

    def is_it_bst(self):
        ls=self.inordertraversal(self.root,[])
        if(ls==sorted(ls)):
            return True
        return False

    def inordertraversal(self,start,elements):
        if start:
            self.inordertraversal(start.left,elements)
            elements+=[start.value]
            self.inordertraversal(start.right,elements)
        return elements


if __name__=='__main__':
    tree=bst(1)
    tree.insertlist([2,3,6,4,9])
    print(tree.is_it_bst())
