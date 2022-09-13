from random import randrange as rr

def instruct():
    print("="*80)
    print("Input Format:")
    print("Enter lower and upper constraint for length of string")
    print("="*80)
    print("Generation Format:\nSingle line containing a string with length in given range")
    print("="*80)

lower='qwertyuiopasdfghjklzxcvbnm'
upper=lower.upper()

instruct()
nl,nr=map(int,input().split())
n=rr(nl,nr+1)
s=[lower[rr(26)] if rr(2) else upper[rr(26)] for _ in range(n)]
print(''.join(s))