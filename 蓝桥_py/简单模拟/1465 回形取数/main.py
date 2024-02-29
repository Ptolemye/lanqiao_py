m,n=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(m)]
flag=[[0]*n for _ in range(m)]
i,j=0,0
ans=[]
dir=1#1表示向下，2表示向右，3表示向上，4表示向左
for _ in range(m*n):
    ans.append(matrix[i][j])
    flag[i][j]=1
    if dir==1:
        if i+1>m-1 or flag[i+1][j]==1:
            dir=2
            j+=1
        else:
            i+=1
    elif dir==2:
        if j+1>n-1 or flag[i][j+1]==1:
            dir=3
            i-=1
        else:
            j+=1
    elif dir==3:
        if i-1<0 or flag[i-1][j]==1:
            dir=4
            j-=1
        else:
            i-=1
    elif dir==4:
        if j-1<0 or flag[i][j-1]==1:
            dir=1
            i+=1
        else:
            j-=1
for c in ans:
    print(c,end=' ')