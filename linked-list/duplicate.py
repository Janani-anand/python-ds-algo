#to detect duplicate for unsorted linkedlist
#method-1 hashset
# time-complexity = O(n)
# space-complexity = O(n)
def deleteduplicate(head):
    h=set()
    itr=head
    prev=itr
    while itr:
        if itr.data in h:
            nextnode=prev.next.next
            prev.next=nextnode
            itr=nextnode
        else:
            h.add(itr.data)
            prev=itr
            itr=itr.next
    return head

# method-2 without hashset
# time-complexity = O(n^2)
# space-complexity = O(1)

def deldup_wo_set(head):
    current=head
    while current:
        runner=current
        while runner.next:
            if runner.next.val==current.val:
                runner.next=runner.next.next
            else:
                runner=runner.next
        current=current.next
        
