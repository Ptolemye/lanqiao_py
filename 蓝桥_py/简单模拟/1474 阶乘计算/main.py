t=int(input())#输入数字
n=list(map(int,list(str(t))))
n=n[::-1]
for i in range(1,t):
    for ii in range(len(n)):
        n[ii]=n[ii]*i
    for ii in range(len(n)-1):
        n[ii+1]+=int(n[ii]/10)
        n[ii]=n[ii]%10
    while n[len(n)-1]>=10:
        n.append(int(n[len(n) - 1]/10))
        n[len(n) - 2] %= 10
for i in n[::-1]:
    print(i,end='')