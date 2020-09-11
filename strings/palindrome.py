
def check_palindrome(st):
    s="".join([i.lower() for i in st if(i.isalnum())]).replace(" ","")
    return s==s[::-1]
#preffered solution solves in linear time doesnt take up extra space
def palindrome(st):
    i=0
    j=len(s)-1
    while i<j:
        while not st[i].isalnum() and i<j:
            i+=1
        while not st[j].isalnum() and i<j:
            j-=1
        if(st[i].lower()!=st[j].lower()):
            return False
        i+=1
        j-=1
    return True
if __name__=='__main__':
    s=input()
    print(check_palindrome(s))
    print(palindrome(s))
