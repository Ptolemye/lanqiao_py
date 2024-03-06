a=[(x,y) for x in range(20) for y in range(21)]
d=set()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i][0]-a[j][0]!=0:
            k=(a[i][1]-a[j][1])/(a[i][0]-a[j][0])
print(len(d)+20)
