from random import randrange as rr

def instruct():
    print("="*80)
    print("Input Format:")
    print("Enter lower and upper constraint for total number of strings")
    print("Enter upper and lower constraint for length of strings in 2nd line")
    print("="*80)
    print("Generation Format:\nNumber of strings T on first line\nNext T will contain strings with length in given range")
    print("="*80)

alphabets='qwertyuiopasdfghjklzxcvbnm'
def make(nl,nr):
    n=rr(nl,nr+1)
    s=[alphabets[rr(26)] for _ in range(n)]
    print(''.join(s))

instruct()
tl,tr=map(int,input().split())
t=rr(tl,tr+1)
nl,nr=map(int,input().split())
print(t)
for _ in range(t):
    make(nl,nr)