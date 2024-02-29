a_loc=list(map(float,input().split()))
b_loc=list(map(float,input().split()))
#确定最小的右上角x
x1=min(max(a_loc[0],a_loc[2]),max(b_loc[0],b_loc[2]))
x2=max(min(a_loc[0],a_loc[2]),min(b_loc[0],b_loc[2]))
y1=min(max(a_loc[1],a_loc[3]),max(b_loc[1],b_loc[3]))
y2=max(min(a_loc[1],a_loc[3]),min(b_loc[1],b_loc[3]))
a=x1-x2
b=y1-y2
if a<=0 or b<=0:
    print("0.00")
else:
    print("%.2f"%(a*b))#格式化输出语句的语法