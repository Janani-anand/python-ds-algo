#binary search recursion solution
def binarysearch(arr,low,high,key):
    if(low>high or key>high):
        return -1
    mid=(low+high)//2
    if(key==arr[mid]):
        return mid
    elif(key<arr[mid]):
        return binarysearch(arr,low,mid-1,key)
    else:
        return binarysearch(arr,mid+1,high,key)

if __name__=='__main__':
    print('Enter the sorted array:')
    arr=list(map(int,input().split()))
    print('Enter the key:')
    key=int(input())
    low=0
    high=len(arr)
    print(binarysearch(arr,low,high,key))
