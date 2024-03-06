trangle=[[0]*43 for _ in range(43)]
x,y=0,0
t=1
for i in range(40):
    if i % 2 == 0:
        x=i
        y=0
    else:
        x=0
        y=i
    for j in range(i+1):
        trangle[x][y]=t
        t+=1
        if i%2==0:
            x-=1
            y+=1
        else:
            x+=1
            y-=1
print(trangle[19][19])