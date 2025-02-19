#DFA to accept decimal no divisible by 2

no=['0','2','4','6','8']
def A(S,i):
    print("A-->", end=" ")
    if len(S) ==i :
        print("Not divisible by 2")
        print("No")
    else:
        if S[i] in no:
            B(S,i+1)
        else:
            A(S,i+1)

def B(S,i):
    print("B-->", end=" ")
    if len(S) ==i :
        print("Divisible by 2")
    else:
        if S[i] in no:
            B(S,i+1)
        else:
            A(S,i+1)


#main
x=input("Enter the string")
A(x,0)
