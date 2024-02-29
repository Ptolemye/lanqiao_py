n=int(input())
m=list(map(int,input().split()))
m.sort()
for i in range(n):
    print(m[i],end=' ')
