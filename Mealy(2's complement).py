#Mealy machine for 2's complement

def A(S,i):
    print("A-->", end=" ")
    if len(S) == i:
        print("Not Accepted")
    else:
        if S[i]=='1':
            print('1')
            B(S,i+1)
        else:
            print('0')
            A(S,i+1)


def B(S,i):
    print("B-->", end=" ")
    if len(S) == i:
        print("Accepted")
    else:
        if S[i]=='1':
            print('0')
            B(S,i+1)
        else:
            print('1')
            B(S,i+1)

#main
x=input("Enter the String:")
A(x,0)
                        
