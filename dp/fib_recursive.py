#exponential time to solve 2^n
def fib(n):
    if n<=2:
        f=1
    else:
        f=fib(n-1)+fib(n-2)
    return f
print('Enter the number:')
num=int(input())
print(fib(num))
