def binarysearch(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        elif(key<arr[mid]):
            high=mid-1
        else:
            low=mid+1
    return None

if __name__=='__main__':
    print('Enter the sorted array:')
    arr=list(map(int,input().split()))
    print('Enter the key:')
    key=int(input())
    print(binarysearch(arr,key))
