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


    def search(self,find_val):
        return self.searchhelper(self.root,find_val)

    def searchhelper(self,current,find_val):
        if current:
            if(current.value==find_val):
                return True
            if(current.value<find_val):
                return self.searchhelper(current.right,find_val)
            else:
                return self.searchhelper(current.left,find_val)

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
    tree=bst(1)
    tree.insertlist([2,3,6,4,9])
    tree.inorder_print()
    tree.insertchild(5)
    tree.inorder_print()
    print(tree.search(6))
    print(tree.search(8))
