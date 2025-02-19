#Moore machine to print 1 whenever it encounter string 'baa'

def A(S,i):
    print("A-->", end=" ")
    print("0")
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='b':
            B(S,i+1)
        else:
            A(S,i+1)


def B(S,i):
    print("B-->", end=" ")
    print("0")
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='a':
            C(S,i+1)
        else:
            B(S,i+1)

def C(S,i):
    print("A-->", end=" ")
    print("0")
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='a':
            D(S,i+1)
        else:
            B(S,i+1)

def D(S,i):
    print("D-->", end=" ")
    print("1")
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='b':
            B(S,i+1)
        else:
            A(S,i+1)

#main
x=input("Enter the string:")
A(x,0)
                                                
