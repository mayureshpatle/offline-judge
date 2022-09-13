from random import randrange as rr
from random import uniform 
tl,tr=map(int,input().split())
l,r=map(float,input().split())

t=rr(tl,tr+1)
print(t)
for _ in range(t):
    print("%.10f"%uniform(l,r))