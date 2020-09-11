
# 1
# 11
# 21
# 1211
# 111221

def lookandsay(s):
    st=''
    pos1=0
    pos2=0
    s=s+'0'
    for i in range(1,len(s)):
        pos2=i
        if(s[pos1]!=s[pos2]):
            st+=str(pos2-pos1)+s[pos1]
            pos1=pos2
    return st

if __name__=='__main__':
    s=input()
    n=int(input())
    print(s)
    for _ in range(n-1):
        s=lookandsay(s)
        print(s)
