#linear time to solve O(n)
#f1=f2=1
#fn=fn-1 +fn-2
def fib(n):
    memo={}
    if n in memo:
        return memo[n]
    if n<=2:
        f=1
    else:
        f=fib(n-1)+fib(n-2)
    memo[n]=f
    return f
print('Enter the number:')
num=int(input())
print(fib(num))
