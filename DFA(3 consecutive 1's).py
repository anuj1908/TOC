#DFA to accept 3 consecutive 1's

def A(S,i):
    print('A-->', end=" ")
    if len(S)==i:
        print("Not accepted")
    else:
        if S[i] == '1':
            B(S,i+1)
        else:
            A(S,i+1)

def B(S,i):
    print('B-->', end=" ")
    if len(S)==i:
        print("Not accepted")
    else:
        if S[i] == '1':
            C(S,i+1)
        else:
            A(S,i+1)

def C(S,i):
    print('C-->', end=" ")
    if len(S)==i:
        print("Not accepted")
    else:
        if S[i] == '1':
            D(S,i+1)
        else:
            A(S,i+1)

def D(S,i):
    print('D-->', end=" ")
    if len(S)==i:
        print("Accepted")
    else:
        if S[i] == '1' or S[i] == '0':
            D(S,i+1)

#main
x=input("Enter the value")
A(x,0)
