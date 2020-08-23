#sorted linkedlist
#to detect the deleteduplicate
#in a sorted linkedlist to find dupliactes check previous value
#time-complexity = O(n)
#space-complexity = O(1)
def del_duplicate(head):
    itr=head
    prev=itr
    itr=itr.next
    while itr:
        if(itr.data==prev.data):
            prev.next=itr.next
        else:
            prev=itr
        itr=itr.next
    return head
