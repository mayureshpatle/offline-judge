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
    total=10**6

    #Line 1
    line=input().strip().split()
    if(len(line)==2):
        minl,maxl=line

        if minl.isdigit():
            minl=int(minl)
            if(minl<1):
                minl=1
                stderr.write("Min_Len cannot be less than 1, set Min_Len = 1\n")
        else:
            minl=1
            stderr.write("Min_Len not given properly, set Min_Len = 1\n")
        
        if maxl.isdigit():
            maxl=int(maxl)
        else:
            maxl=2*(10**5)
            stderr.write("Max_Len not given properly, set Max_Len = 200000\n")
    
    else:
        minl,maxl=1,200000
        stderr.write("Problem in Line 1, set Min_Len = 1 & Max_Len = 200000\n")

    if minl>maxl:
        minl=1
        stderr.write("Min_Len > Max_Len, set Min_Len = 1\n")

    stderr.write("Processed Line 1\n")
    ok()

    #Line 2
    line=input().strip().split()
    try:
        minv,maxv=map(int,line)
    except:
        stderr.write("Problem in Line 2, set Min_Val=1 & Max_Val=Max_Len\n")
        minv,maxv=1,maxl

    if(minv>maxv):
        stderr.write("Max_Val < Min_Val, set Max_Val = Min _Val\n")
        maxv=minv

    if maxv>10**9 or minv<-10**9:
        total=200000
        if maxl>2*(10**5):
            stderr.write("Values are large, decreasing Length Constraints\n")
            stderr.write("Set Max_Len = 200000\n")
            maxl=int(2e5)
            if minl>maxl: 
                stderr.write("Set Min_Len = 1\n")
                minl=1
    elif maxl>10**6:
        stderr.write("Decreasing Length Constraints\n")
        stderr.write("Set Max_Len = 1000000\n")
        maxl=int(1e6)
        if minl>maxl: 
            stderr.write("Set Min_Len = 1\n")
            minl=1
    stderr.write("Processed Line 2\n")
    ok()

    #Line 3
    order=input().strip()
    try:
        order=int(line)
        if order==1:
            stderr.write("Increasing Order Selected\n")
        elif order==2:
            stderr.write("Decreasing Order Selected\n")
        else:
            order=0
            stderr.write("Random Order Selected\n")
    except:
        order=0
        stderr.write("Random Order Selected\n")
    stderr.write("Processed Line 3\n")
    ok()

    #Line 4
    line=input().strip()
    try:
        diff=int(line)
        if diff!=1:
            diff=0
            stderr.write("Distinct_Flag is NOT SET\n")
        else:
            stderr.write("Distinct_Flag is SET\n")
    except:
        diff=0
        stderr.write("Distinct_Flag is NOT SET\n")
    if diff:
        if minl>maxv-minv+1:
            stderr.write("Invalid length to ensure distinct elements.\n")
            stderr.write("Decreasing Array Length, Min_Len=1, Max_Len=Length of Interval of values")
            minl,maxl=1,maxv-minv+1
            

    stderr.write("Processed Line 4\n")
    ok()

    #Line 5
    line=input()
    try:
        perm=int(line)
        if perm!=1:
            perm=0
            stderr.write("Permutation_Flag is NOT SET\n")
        else:
            diff=1
            stderr.write("Permutation_Flag is SET, Distince_Flag is also SET\n")
    except:
        perm=0
        stderr.write("Permutation_Flag is NOT SET\n")
    if perm:
        if minl>maxv-minv+1:
            stderr.write("Invalid length to ensure permutation.\n")
            stderr.write("Decreasing Array Length, Min_Len=1, Max_Len=Length of Interval of values\n")
            minl,maxl=1,maxv-minv+1
            minv,maxv=1,maxl
    stderr.write("Processed Line 5\n")
    ok()

    #Line 6
    line=input().strip()
    if line=="":
        delim=" "
        delim_vis=" "
        stderr.write("Using ' ' as delimiter\n")
    elif line=="ENTER":
        delim="\n"
        delim_vis="\\n"
        stderr.write("Using '\\n' as delimiter\n")
    elif line=="TAB":
        delim="\t"
        delim_vis="\\t"
        stderr.write("Using '\\t' as delimiter\n")
    else:
        delim=line
        delim_vis=line
        stderr.write("Using"+line+"as delimiter\n")
    stderr.write("Processed Line 6\n")
    ok()

    #Line 7
    line=input()
    try:
        tests=int(line)
        if tests!=1:
            tests=0
            stderr.write("Multiple_Testcases_Flag is NOT SET\n")
        else:
            stderr.write("Multiple_Testcases_Flag is SET\n")
    except:
        tests=0
        stderr.write("Multiple_Testcases_Flag is NOT SET\n")
    stderr.write("Processed Line 7\n")
    ok()

    #Line 8
    line=input().strip()
    if not tests:
        stderr.write("Ignored Line 8\n")
    else:
        try:
            maxt=int(line)
        except:
            maxt=total
            stderr.write("Set Max_T =",maxt)
    stderr.write("Processed Line 8\n")
    ok()
    
    if not tests:
        maxt=1

    ok()
    out("CONSIDERED VALUES")
    out("Line 1:",minl,maxl)
    out("Line 2:",minv,maxv)
    out("Line 3:",order)
    out("Line 4:",diff)
    out("Line 5:",perm)
    out("Line 6:",delim_vis)
    out("Line 7:",tests)
    out("Line 8:",maxt)
    out("Sum of Array Lengths over all Testcases:",total)
    ok()
    out("Test File Generation Initialized ...............")
    ok()

    lens=[]
    full=0
    while maxt and total>=minl:
        if not full and maxt*maxl <= total:
            full=1
        if full:
            l=min(maxl,total)
            lens.append(l)
            total-=l
        else:
            l=rr(minl,min(total,maxl)+1)
            lens.append(l)
            total-=l
        maxt-=1

    if tests:
        print(len(lens))

    for l in lens:
        print(l)
        arr=[]
        if not diff and rr(2) and rr(2) and rr(2):
            ele=rr(minv,maxv+1)
            arr=[ele]*l
        elif not diff and rr(2) and rr(2):
            req=l
            while req:
                curr=rr(1,req+1)
                ele=rr(minv,maxv+1)
                arr+=[ele]*curr
                req-=curr
        elif not diff:
            arr=[rr(minv,maxv+1) for _ in range(l)]
        elif perm:
            arr=list(range(1,l+1))
        else:
            arr=set()
            rng = maxl-minl+1
            blc = min(rng//l,1000)
            arr=set()
            if blc<2:
                arr=list(range(1,l+1))
            else:
                ix=0
                while(len(arr)<l):
                    last=min(ix+blc,rng)
                    arr.add(random.choice(range(ix+minv,last+minv)))
                    ix=(ix+blc)%rng
            arr=list(arr)

        if order:
            arr.sort()
            if order==2:
                arr=arr[::-1]
        else:
            random.shuffle(arr)

        print(*arr,sep=delim)
    
    return True


def main():
    if create():
        ok()
        stderr.write("\nTEST FILE CREATED SUCCESSFULLY!")
    
main()