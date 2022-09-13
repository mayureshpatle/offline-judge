from random import randrange as rr
tl,tr=map(int,input().split())
l,r=map(int,input().split())

t=rr(tl,tr+1)
print(t)
for _ in range(t):
    print(rr(l,r+1))