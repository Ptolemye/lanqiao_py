now_ch=ord('A')#记录现在最新字母的ASCLL码
str='A'
n=int(input())
for i in range(n-1):
    ans=str+chr(now_ch+1)+str
    str=ans
    now_ch+=1
print(ans)
#很简单，基本的字符串操作