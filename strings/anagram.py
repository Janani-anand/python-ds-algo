def anagram(s1,s2):
    h1=dict()
    for i in s1:
        h1[i]=h1.get(i,0)+1
    for i in s2:
        if(i in h1):
            h1[i]=h1[i]-1
        else:
            h1[i]=1
    for i in h1:
        if(h1[i]!=0):
            return False
    return True

if __name__=='__main__':
    s1=input()
    s2=input()
    print(anagram(s1,s2))
