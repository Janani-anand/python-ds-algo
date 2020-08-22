def countingsort(arr):
    if(len(arr)<=1):
        return arr
    length=len(arr)
    start=min(arr)
    end=max(arr)
    indexes=[0]*(end-start+1)
    for i in arr:
        indexes[i-start]+=1
    for i in range(1,len(indexes)):
        indexes[i]=indexes[i]+indexes[i-1]
    ordered=[0]*length
    for i in range(0,length):
        ordered[indexes[arr[i]-start]-1]=arr[i]
        indexes[arr[i]-start]-=1
    return ordered



if __name__ == "__main__":
    arr=list(map(int,input().split()))
    print(*countingsort(arr),sep=" ")
