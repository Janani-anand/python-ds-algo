def spreadsheet(s):
    dic={}
    alpha='A'
    ans=0
    l=len(s)-1
    dic[alpha]=1
    for i in range(1,26):
        dic[chr(ord(alpha)+i)]=i+1
    for i in range(l+1):
        ans+=dic[s[i]]*(26**(l-i))
    return ans

if __name__=='__main__':
    s=input()
    print(spreadsheet(s))
