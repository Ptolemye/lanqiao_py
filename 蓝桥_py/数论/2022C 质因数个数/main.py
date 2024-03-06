n=int(input())
ans=0
i=2
while i*i<=n:
    if n%i==0:
        ans+=1
        while n%i==0:
            n=n//i
    if n==1:
        break
    i+=1
if n>1:
    ans+=1
print(ans)
#质因数求解