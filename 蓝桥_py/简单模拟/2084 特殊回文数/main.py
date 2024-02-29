n=int(input())
for i in range(10000,1000000):
    s=str(i)
    Sum=0
    if s==s[::-1]:
        for c in s:
            Sum+=int(c)
        if Sum==n:
            print(i)

