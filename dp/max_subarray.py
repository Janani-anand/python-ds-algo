#kadanes algorithm

def maxsub(arr):
    curmax=globalmax=arr[0]
    sub=[]
    sub.append(arr[0])
    for i in range(1,len(arr)):
        if(curmax<arr[i]):
            sub.clear()
            sub.append(arr[i])
            curmax=arr[i]
        elif(curmax<curmax+arr[i]):
            sub.append(arr[i])
            curmax=curmax+arr[i]
        if(globalmax<curmax):
            ans=sub
            globalmax=curmax
    return globalmax,ans

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print('The value of maximum subarry:')
    print(maxsub(arr))
