#Mealy Machine for 1's complement

def A(S,i):
    print("A-->",end=" ")
    if len(S)==i:
        print("Accepted")
    else:
        if S[i]=='0':
            print('1')
            A(S,i+1)
        else:
            print('0')
            A(S,i+1)

#main
x=input("Enter the string")
A(x,0)
