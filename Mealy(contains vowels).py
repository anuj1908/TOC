#Mealy machine to check if given input string contains a vowels

vowels=['a','e','i','o','u']
def A(S,i):
    print("A-->",end=" ")
    if len(S)==i:
        print("Not Accepted")
    else:
        if S[i] in vowels:
            print("1")
            B(S,i+1)
        else:
            print("0")
            A(S,i+1)

def B(S,i):
    print("B-->",end=" ")
    if len(S)==i:
        print("Accepted")
    else:
        if S[i] in vowels:
            print("1")
            B(S,i+1)
        else:
            print("0")
            B(S,i+1)

#main
x=input("Enter the string:")
A(x,0)
        
        
