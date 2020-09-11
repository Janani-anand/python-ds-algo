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
    def levelorder(self):
        self.levelorderhelper(self.root)
    def levelorderhelper(self,root):
        if root is None:
            print('')
            return
        q=[]
        q.insert(0,root)
        while len(q)>0:
            print(q[-1].value,end=' ')
            elem=q.pop()
            if(elem.left):
                q.insert(0,elem.left)
            if(elem.right):
                q.insert(0,elem.right)



if __name__=='__main__':
    tree=bst(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.levelorder()
