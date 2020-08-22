def quicksort(arr):
    if(len(arr)<=1):
        return arr
    pivot=arr.pop()
    #pivot to be the last element
    lesser,greater=[],[]
    for i in arr:
        if(i<pivot):
            lesser.append(i)
        else:
            greater.append(i)
    return quicksort(lesser)+[pivot]+ quicksort(greater)

if __name__ == "__main__":
    arr=list(map(int,input().split()))
    print(*quicksort(arr),sep=" ")
