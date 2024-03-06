martrix=[list(input()) for _ in range(300)]
ans=0
#同一行
for i in range(300):
    for j in range(297):
        if martrix[i][j]=='2'and martrix[i][j+1]=='0' and martrix[i][j+2]=='2' and martrix[i][j+3]=='0':
            ans+=1
#同一列
for i in range(300):
    for j in range(297):
        if martrix[j][i]=='2'and martrix[j+1][i]=='0' and martrix[j+2][i]=='2' and martrix[j+3][i]=='0':
            ans+=1
#对角线
for i in range(297):
    for j in range(297):
        if martrix[i][j]=='2'and martrix[i+1][j+1]=='0' and martrix[i+2][j+2]=='2' and martrix[i+3][j+3]=='0':
            ans+=1
print(ans)