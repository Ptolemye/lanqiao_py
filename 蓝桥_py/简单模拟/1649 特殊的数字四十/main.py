for i in range(1000,10000):
    s=str(i)
    Sum=0
    for c in s:
        Sum+=int(c)
    if Sum==10:
        print(i)