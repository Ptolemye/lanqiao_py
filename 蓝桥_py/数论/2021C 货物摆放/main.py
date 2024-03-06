n=2021041820210418
i=1
ans=0
docker=set()
while i*i<=n:
    if n%i==0:
        docker.add(i)
        if n//i!=i:
            docker.add(n//i)
    i+=1
for ii in docker:
    for j in docker:
        if n%(ii*j)==0:
            ans+=1
print(ans)

#因数求解