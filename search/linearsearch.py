def linearsearch(arr,key):
    for i in arr:
        if(i==key):
            return arr.index(i)
    return None

if __name__=='__main__':
    print('Enter the sorted array:')
    arr=list(map(int,input().split()))
    print('Enter the key:')
    key=int(input())
    print(linearsearch(arr,key))
