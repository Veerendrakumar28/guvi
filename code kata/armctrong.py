q=int(input())
a=q
s=0
while(q>0):
  k=q%10
  q=q//10
  c=k**3
  s=s+c
if(a==s):
  print('yes')
else:
  print('no')
