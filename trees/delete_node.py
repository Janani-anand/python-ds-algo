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

    def delete_node(self,current,node):
        if(node<current.value):
            if(current.left):
                current.left=self.delete_node(current.left,node)
        elif(node>current.value):
            if(current.right):
                current.right=self.delete_node(current.right,node)
        else:
            
            if(current.left is None and current.right is None):
                return None
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            min_val=self.find_min(current.right)
            current.value=min_val
            current.right=self.delete_node(current.right,min_val)
        return current

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
    tree=bst(4)
    tree.insertlist([2,3,1,7,9])
    tree.insertchild(6)
    tree.inorder_print()
    tree.delete_node(tree.root,7)
    tree.inorder_print()
