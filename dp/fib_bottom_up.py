def fib(n):
    f={}
    for i in range(1,n+1):
        if i<=2:
            f[i]=1
        else:
            f[i]=f[i-1]+f[i-2]
    return f[n]
print('Enter the number:')
num=int(input())
print(fib(num))
