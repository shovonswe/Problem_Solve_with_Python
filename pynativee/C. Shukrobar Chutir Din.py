t = int(input())
for i in range(t):
  k,m,n = map(int,input().split())
  ans = (k*m*n)-(k*m*(n//7))
  print(ans)
    