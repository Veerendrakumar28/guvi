k,l=map(int,input().split())
if(k<l):
  for i in range(k+1,l,1):
     if i%2!=0:
        print(i,end=' ')
