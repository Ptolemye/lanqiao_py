from datetime import *
start=date(2000,1,1)
end=date(2020,10,2)
gap=timedelta(days=1)
ans=0
while start!=end:
    if start.weekday()==0 or start.day==1:
        ans+=2
    else:
        ans+=1
    start+=gap
print(ans)