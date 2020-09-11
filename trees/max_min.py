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

    def find_max(self,current):
        if(current.right):
            return self.find_max(current.right)
        return current.value

    def find_min(self,current):
        if(current.left):
            return self.find_min(current.left)
        return current.value



if __name__=='__main__':
    tree=bst(4)
    tree.insertlist([2,3,1,7,9])
    tree.insertchild(6)
    print('max:',tree.find_max(tree.root))
    print('min:',tree.find_min(tree.root))
