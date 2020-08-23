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

    def insertlist(self,datalist):
        for data in datalist:
            self.insertend(data)

    def displaylinkedlist(self):
        if(self.head==None):
            print('Empty list')
            return
        itr=self.head
        while itr:
            print(itr.data,end='-->')
            itr=itr.next
        print()

def mergelists(head1,head2):
    itr1=head1
    itr2=head2
    ret=cur=linkedlistnode(0)
    while itr1 and itr2:
        if(itr1.data<itr2.data):
            cur.next=itr1
            itr1=itr1.next
        else:
            cur.next=itr2
            itr2=itr2.next
        cur=cur.next
    cur.next=itr1 or itr2
    # return ret.next
    head=ret.next
    if(head==None):
        print('Empty list')
        return
    itr=head
    while itr:
        print(itr.data,end='-->')
        itr=itr.next
    print()

if __name__=='__main__':
    ll1=linkedlist()
    ll1.insertlist([3,6,9])
    ll1.displaylinkedlist()
    ll2=linkedlist()
    ll2.insertlist([1,2,4,5,7,8])
    ll2.displaylinkedlist()
    mergelists(ll1.head,ll2.head)
