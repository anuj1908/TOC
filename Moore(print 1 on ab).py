#Moore machine to print 1 whenever it encounter 'ab'

def A(S,i):
    print("A-->", end=" ")
    print('0')
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='a':
            B(S,i+1)
        else:
            A(S,i+1)


def B(S,i):
    print("B-->", end=" ")
    print('0')
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='b':
            C(S,i+1)
        else:
            B(S,i+1)

def C(S,i):
    print("C-->", end=" ")
    print('1')
    if len(S)==i:
        print("End of the string")
    else:
        if S[i]=='a' or S[i]=='b':
            C(S,i+1)

#main
x=input("Enter the string:")
A(x,0)

                        
