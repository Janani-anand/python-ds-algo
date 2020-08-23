class linkedlistnode:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def insertend(self,data):
        if(self.head==None):
            return self.insertbegining(data)
        itr=self.head
        while itr.next:
            itr=itr.next
        node=linkedlistnode(data,None)
        itr.next=node

    def insertbegining(self,data):
        if(self.head==None):
            node=linkedlistnode(data,None)
            self.head=node
            return
        node=linkedlistnode(data,self.head)
        self.head=node

    def deletebegining(self):
        if(self.head==None):
            return
        itr=self.head
        self.head=itr.next

    def deleteend(self):
        if(self.head==None):
            return
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

    def sizeof(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count=count+1
        return count

    def insertat(self,data,index):
        if(index<0 or index>(self.sizeof()-1)):
            raise Exception("invalid index")
        if(self.head==None or index==0):
            return self.insertbegining(data)
        if(index==self.sizeof()-1):
            return self.insertend(data)
        count=0
        itr=self.head
        while count!=index-1:
            itr=itr.next
            count=count+1
        nextnode=itr.next
        itr.next=linkedlistnode(data,nextnode)

    def insertlist(self,datalist):
        for data in datalist:
            self.insertend(data)

    def deleteat(self,index):
        if(index<0 or index>(self.sizeof()-1)):
            raise Exception("invalid index")
        if(self.head==None):
            return
        if(index==0):
            return self.deletebegining()
        if(index==self.sizeof()-1):
            return self.deleteend()
        count=0
        itr=self.head
        while count!=index-1:
            itr=itr.next
            count=count+1
        nextnode=itr.next.next
        itr.next=nextnode

    def displaylinkedlist(self):
        if(self.head==None):
            print('Empty list')
            return
        itr=self.head
        while itr:
            print(itr.data,end='-->')
            itr=itr.next
        print()

if __name__=='__main__':
    ll=linkedlist()
    ll.insertbegining(0)
    ll.insertend(1)
    ll.insertend(2)
    ll.insertend(3)
    ll.insertbegining(4)
    ll.insertat(5,2)
    ll.displaylinkedlist()
    ll.deleteat(2)
    ll.displaylinkedlist()
    ll.insertlist([6,7,8])
    ll.displaylinkedlist()
