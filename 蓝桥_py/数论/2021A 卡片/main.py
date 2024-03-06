def ins_count(k):
    return ((k+1)/2)*k
n=int(input())
i=1
while True:
    if ins_count(i)>=n:
        print(i)
        break
    else:
        i+=1