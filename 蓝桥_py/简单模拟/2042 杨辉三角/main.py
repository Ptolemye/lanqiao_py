n=[[0]*1000 for i in range(1000)]
for i in range(1000):
    for j in range (1000):
        if j==0:
            n[i][j]=1
        else:
            n[i][j]=n[i-1][j]+n[i-1][j-1]
t=list(map(int,input().split()))

print(n[t[0]-1][t[1]-1])