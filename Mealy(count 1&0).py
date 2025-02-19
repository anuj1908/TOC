#Mealy machine to count no of 1's and 0's

def A(S,i,a,b):
    print("A-->", end=" ")
    if len(S)==i:
        print("Accepted")
        print("Total no of 1's",b)
        print("Total no of 0's",a)
    else:
        if S[i]=='0':
            print("a")
            A(S,i+1,a+1,b)
        else:
            print("b")
            A(S,i+1,a,b+1)

#main
x=input("Enter the string:")
A(x,0,0,0)
