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


    def calculate_sum(self,current):
        left_sum=self.calculate_sum(current.left) if current.left else 0
        right_sum=self.calculate_sum(current.right) if current.right else 0
        return current.value+left_sum+right_sum



if __name__=='__main__':
    tree=bst(1)
    tree.insertlist([2,3,6,4,9])
    tree.insertchild(5)
    print(tree.calculate_sum(tree.root))
