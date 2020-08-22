def merge(left,right):
    result=[]
    while left and right:
        result.append((left if left[0]<right[0] else right).pop(0))
    return result + left + right

def mergesort(arr):
    if(len(arr)<=1):
        return arr
    mid=len(arr)//2
    return merge(mergesort(arr[:mid]),mergesort(arr[mid:]))

if __name__ == "__main__":
    arr=list(map(int,input().split()))
    print(*mergesort(arr),sep=" ")
