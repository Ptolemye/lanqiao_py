n=int(input())
box=[[0]*n for i in range(n)]
for i in range(n):
    input_list=list(map(int,input().split()))
    for j in range(n):
        box[i][j]=input_list[j]
good=[]
standard=int((n+1)/2)
for i in range(n):
    Sum=0
    for j in range(n):
        Sum+=box[j][i]
    if Sum>=standard:
        good.append(i+1)
for i in good:
    print(i,end=' ')
