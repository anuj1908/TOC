#DFA to accept decimal no divisible by 3

a=['0','3','6','9']
b=['1','4','7']
c=['2','5','8']
def A(S,i):
    print("A-->", end=" ")
    if len(S) == i:
        print("Final State")
    else:
        if S[i] in a:
            A(S,i+1)
        elif S[i] in b:
            C(S,i+1)
        else:
            B(S,i+1)

def B(S,i):
    print("B-->", end=" ")
    if len(S) == i:
        print("No")
    else:
        if S[i] in a:
            B(S,i+1)
        elif S[i] in b:
            A(S,i+1)
        else:
            C(S,i+1)

def C(S,i):
    print("C-->", end=" ")
    if len(S) == i:
        print("No")
    else:
        if S[i] in a:
            C(S,i+1)
        elif S[i] in b:
            B(S,i+1)
        else:
            A(S,i+1)

#main
x=input("Enter the string:")
A(x,0)
