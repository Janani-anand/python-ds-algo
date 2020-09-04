def knapsack(profit,wt,weight):
    n=len(profit)
    k=[[0]*(weight+1) for x in range(n+1)]
    for i in range(n+1):
        for w in range(weight+1):
            if(i==0 or w==0):
                k[i][w]=0
            elif(wt[i-1]<=w):
                k[i][w]=max(k[i-1][w],k[i-1][w-wt[i-1]]+profit[i-1])
            else:
                k[i][w]=k[i-1][w]
    return k[n][weight]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(val,wt,W))
