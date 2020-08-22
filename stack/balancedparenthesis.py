
def balanced(par):
    arr=[i for i in par]
    dic={'(':')',
    '[':']',
    '{':'}'}
    stack=[]
    i=0
    while arr:
        if arr[i] in dic:
            stack.append(arr[i])
        else:
            if(arr[i]==dic[stack[-1]]):
                stack.pop()
        arr.pop(0)

    if(not stack):
        return 'Valid'
    return 'Invalid'

if __name__=='__main__':
    inp=input()
    print(balanced(inp))
