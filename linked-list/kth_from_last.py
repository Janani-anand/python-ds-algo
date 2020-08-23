#method-1
#by taking two pointers p1 and p2
#move one p1 forward by k nodes
#now move both p1 and p2 until p1 reaches the end
#the distance between them would be k
#Genius right :O
#return p2.data
def getNode(head,k):
    p1=head
    p2=head
    while k:
        p1=p1.next
        k=k-1
    while p1.next:
        p1=p1.next
        p2=p2.next
    return p2.data

#method-2
#using dictionary
# is a brute force
def getNodedict(head,k):
    count=0
    d=dict()
    itr=head
    while itr:
        d[count]=itr.data
        itr=itr.next
        count=count+1
    return d[count-k-1]
