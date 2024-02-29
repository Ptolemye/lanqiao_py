str_1=input()
str_2=input()
ans=1
if len(str_1)!=len(str_2):
    ans=1
elif str_1==str_2:
    ans=2
elif len(str_1)==len(str_2) and str_1.upper()==str_2.upper():
    ans=3
elif len(str_1)==len(str_2) and str_1.upper()!=str_2.upper():
    ans=4
print(ans)