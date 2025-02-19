#PDA to accept same no of a's and b's

stack=[]
def A(S,i):
    print("A-->", end=" ")
    if len(S)>0:
        stack.append("z0")
        B(S,i)
def B(S,i):
    print("B-->",end=" ")
    if S[i]=='a' and S[i+1]=='a':
        stack.append('a')
        B(S,i+1)
    else:
        C(S,i+1)
def C(S,i):
    print("C-->", end=" ")
    if S[i]=='b' and i<len(S)-1:
        stack.pop()
        C(S,i+1)
    else:
        D(S,i+1)
def D(S,i):
    print("D-->", end=" ")
    if len(stack)==1:
        stack.pop(0)
        print("Accepted")
    else:
        print("Reject")

#main
S='aaabbb'
A(S,0)
