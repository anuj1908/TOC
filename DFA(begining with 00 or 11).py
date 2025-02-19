#DFA that accept string begging with 00 or 11
def A(S,i):
    print("A-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='0':
            B(S,i+1)
        else:
            C(S,i+1)

def B(S,i):
    print("B-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='0':
            D(S,i+1)
        else:
            E(S,i+1)
            
def C(S,i):
    print("C-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='1':
            D(S,i+1)
        else:
            E(S,i+1)

def D(S,i):
    print("D-->", end=" ")
    if len(S)==i:
        print("Accepted")
    else:
        if S[i]=='0' or S[i]=='1':
            D(S,i+1)
        
def E(S,i):
    print("E-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i]=='0' or S[i]=='1':
            E(S,i+1)

#main
x=input("Enter the string:")
A(x,0)
