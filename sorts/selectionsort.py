def selectionsort(arr):
    end=len(arr)
    while end>1:
        item=max(arr[:end])
        pos=arr[:end].index(item)
        arr[end-1],arr[pos]=arr[pos],arr[end-1]
        end=end-1
    return arr

if __name__=='__main__':
    arr=list(map(int,input().split()))
    print(*selectionsort(arr),sep=" ")
