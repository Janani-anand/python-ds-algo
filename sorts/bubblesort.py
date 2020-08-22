def bubblesort(arr):
    passnum=len(arr)-1
    exchange=True
    while exchange and passnum:
        exchange=False
        for i in range(passnum):
            if(arr[i]>arr[i+1]):
                exchange=True
                arr[i],arr[i+1]=arr[i+1],arr[i]
        passnum=passnum-1
    return arr

if __name__=='__main__':
    arr=list(map(int,input().split()))
    print(*bubblesort(arr),sep=" ")
