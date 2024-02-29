F1, F2 = 1, 1
N=int(input())
for i in range(3, N + 1):
  F1, F2 = F2 % 10007, (F1 + F2) % 10007  # 先取余再递推防止超时
print(F2)
