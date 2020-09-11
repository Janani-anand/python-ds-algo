def cyclic_shift(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if(arr[mid]>arr[high]):
            low=mid+1
        elif(arr[mid]<=arr[high]):
            high=mid
    return low

if __name__=='__main__':
    print(cyclic_shift([6,7,8,1,2,3,4,5]))
