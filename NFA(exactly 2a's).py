#NFA that contains exactly 2a's

def A(S,i):
    print("A-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='a':
            B(S,i+1)
        else:
            A(S,i+1)


def B(S,i):
    print("B-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='a':
            C(S,i+1)
        else:
            B(S,i+1)


def C(S,i):
    print("C-->", end=" ")
    if len(S)==i:
        print("Accepted")
    else:
        if S[i]=='a':
            D(S,i+1)
        else:
            C(S,i+1)


def D(S,i):
    print("D-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='a' or S[i]=='b':
            D(S,i+1)

#main
x=input("Enter the string:")
A(x,0)
