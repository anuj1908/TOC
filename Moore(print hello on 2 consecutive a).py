#Moore machine to print 'hello' when the input starts with 2 consecative a

def A(S,i):
    print("A-->", end=" ")
    print("0")
    if len(S)==i:
        print("End of the String")
    else:
        if S[i]=='a':
            B(S,i+1)
        else:
            D(S,i+1)

def B(S,i):
    print("B-->", end=" ")
    print("0")
    if len(S)==i:
        print("End of the String")
    else:
        if S[i]=='a':
            C(S,i+1)
            print("Hello")
        else:
            D(S,i+1)

def C(S,i):
    print("C-->", end=" ")
    print("1")
    if len(S)==i:
        print("End of the String")
    else:
        if S[i]=='a' or S[i]=='b':
            C(S,i+1)

def D(S,i):
    print("D-->", end=" ")
    print("0")
    if len(S)==i:
        print("End of the String")
    else:
        if S[i]=='a' or S[i]=='b':
            D(S,i+1)
       

#main
x=input("Enter the string:")
A(x,0)
        
