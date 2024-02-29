n=int(input())
for i in range(n):
    s=input()
    res_1=int(s,16)
    res_2=oct(res_1)
    print(res_2[2:])
