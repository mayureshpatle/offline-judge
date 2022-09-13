from random import randrange as rr
import random
from sys import stderr
import sys

def ok():
    stderr.write("="*50+"\n")

def dbg():
    stderr.write("Alright till here\n")

def out(*l):
    stderr.write(" ".join(map(str,l)))
    stderr.write("\n")

def create():
    #Line 1
    minn,maxn=map(int,input().strip().split())

    #Line 2
    mine,maxe=map(int,input().strip().split())

    #Line 3
    try:
        direct=int(input().strip())
    except:
        direct=0
    if direct!=1: direct=0

    #Line 4
    try:
        nd_wt=int(input().strip())
    except:
        nd_wt=0
    if nd_wt!=1:nd_wt=0

    #Line 5
    if nd_wt:
        minnw,maxnw=map(int,input().split())
    else:
        minnw,maxnw=0,0

    #Line 6
    try:
        e_wt=int(input().strip())
    except:
        e_wt=0
    if e_wt!=1: e_wt=0


    #Line 7
    if e_wt:
        minew,maxew=map(int,input().split())
    else:
        minew,maxew=0,0

    #Line 8
    try:
        conn=int(input().strip())
    except:
        conn=0
    if conn!=1: conn=0

    #Line 9
    try:
        cycle=int(input().strip())
    except:
        cycle=1
    if cycle!=1: cycle=0

    #Line 10
    try:
        base=int(input().strip())
    except:
        base=1
    if base!=1: base=0

    #Line 11
    try:
        tests=int(input().strip())
    except:
        tests=1
    if tests!=1: tests=0

    #Line 12
    if tests:
        maxt=int(input().strip())
    else:
        maxt=1

    #Line 13
    try:
        tree=int(input().strip())
    except:
        tree=0
    if tree!=1: tree=0
    else: conn,cycle=1,0

    #Line 14
    try:
        rooted=int(input().strip())
    except:
        rooted=0
    if rooted!=1: rooted=0


    ok()
    out("Processed All Lines")
    out("CONSIDERED VALUES")
    out("Line 1:",minn,maxn)
    out("Line 2:",mine,maxe)
    out("Line 3:",direct)
    out("Line 4:",nd_wt)
    out("Line 5:",minnw,maxnw)
    out("Line 6:",e_wt)
    out("Line 7:",minew,maxew)
    out("Line 8",conn)
    out("Line 9:",cycle)
    out("Line 10:",base)
    out("Line 11:",tests)
    out("Line 12:",maxt)
    out("Line 13:",tree)
    out("Line 14:",rooted)

    ok()
    out("Test File Generation Initialized ...............")
    ok()

    t=rr(1,maxt+1)
    if tests:
        print(t)

    for _ in range(t):
        n=rr(minn,maxn+1)
        if nd_wt:
            wts=[rr(minnw,maxnw) for _ in range(n)]
            print(*wts)
        
        if n<1415 and (cycle or n==1 or (n==2 and not direct)) and rr(2) and rr(2):
            e=(n*(n-1))//2
            if direct:
                e<<=1
            print(e)
            edges=[]
            for i in range(base,base+n):
                for j in range(i+1,base+n):
                    w1,w2=[rr(minew,maxew+1) for _ in range(2)]
                    if e_wt:
                        e1=(i,j,w1)
                        e2=(j,i,w2)
                    else:
                        e1=(i,j)
                        e2=(j,i)
                    if direct:
                        edges.append(e1)
                        edges.append(e2)
                    else:
                        edges.append([e1,e2][rr(2)])
                    
        else:
            e=rr(mine,min((n*(n-1))//2,maxe))
            print(e)
            done={}
            edges=[]
            for _ in range(e):
                while True:
                    u,v=[rr(base,base+n) for _ in range(2)]
                    w=rr(minew,maxew+2)
                    if not done[(u,v)]:
                        break
                done[(u,v)]=1
                done[(v,u)]=1
                if e_wt:
                    e1=(u,v,w)
                    e2=(v,u,w)
                else:
                    e1=(u,v)
                    e2=(v,u)
                edges.append([e1,e2][rr(2)])
            
        for ed in edges:
            print(*ed)

    return True




def main():
    if create():
        ok()
        stderr.write("\nTEST FILE CREATED SUCCESSFULLY!")
    
main()
