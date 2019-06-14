q,r=map(int,input().split())
for v in range(q+1,r):
  if v>1:
    for l in range(2,v):
      if(v%l==0):
        break
    else:
      print(v,end=' ')
