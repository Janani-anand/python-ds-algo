#kadanes algorithm

def maxsub(arr):
    curmax=globalmax=arr[0]
    sub=[]
    for i in range(1,len(arr)):
        curmax=max(arr[i],curmax+arr[i])
        globalmax=max(globalmax,curmax)
    return globalmax

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print('The value of maximum subarry:')
    print(maxsub(arr))
