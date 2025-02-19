#NFA that ends with 1

def A(S,i):
    print("A-->", end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i] == '1':
            B(S,i+1)
        else:
            A(S,i+1)

def B(S,i):
    print("B-->", end=" ")
    if len(S)==i:
        print("Accepted")
    else:
        if S[i] == '1':
            B(S,i+1)
        else:
            A(S,i+1)

#main

x=input("Enter the string:")
A(x,0)
            
