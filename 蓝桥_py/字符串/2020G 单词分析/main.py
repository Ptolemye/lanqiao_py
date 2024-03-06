str=input()
start=ord('a')
end=ord('z')+1
ans='a'
number=0
while start!=end:
    ch=chr(start)
    if number<str.count(ch):
        ans=ch
        number = str.count(ch)
    start+=1
print(ans)
print(number)
