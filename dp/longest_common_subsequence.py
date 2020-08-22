def lcs(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


if __name__=='__main__':
    s1=input()
    s2=input()
    print('The longest Common Subsequence is:')
    print(lcs(s1,s2))
