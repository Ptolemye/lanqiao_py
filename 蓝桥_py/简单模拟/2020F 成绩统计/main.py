n=int(input())
grade=[]
for _ in range(n):
    grade.append(int(input()))
good_number=0
ok_number=0
for i in grade:
    if i>=60:
        ok_number+=1
    if i>=85:
        good_number+=1
good_rate=int((good_number/n+0.005)*100)
ok_rate=int((ok_number/n+0.005)*100)
print(str(ok_rate)+'%')
print(str(good_rate)+'%')