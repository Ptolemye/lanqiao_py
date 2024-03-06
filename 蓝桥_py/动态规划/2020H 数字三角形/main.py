N=int(input())
trangle=[list(map(int,input().split())) for _ in range(N)]
dp=[[0]*i for i in range(1,N+1)]
dp[0][0]=trangle[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i-1][0]+trangle[i][j]
        elif i==j:
            dp[i][j]=dp[i-1][j-1]+trangle[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+trangle[i][j]
if N%2==1:
    print(dp[N-1][(N-1)//2])
else:
    print(max(dp[N-1][N//2-1],dp[N-1][N//2]))