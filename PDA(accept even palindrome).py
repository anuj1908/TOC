#PDA to accept even length palindrome strings that read same in forward and reverse direction
st=[]
def A(S,i):
    print("A-->", end="")
    if len(S)>0:
        st.append('z0')
        return B(S,i+1)
def B(S,i):
    print("B-->", end="")
    if len(S)==i:
        print("No")
    if S[i]=='a' or S[i] == 'b':
        st.append(S[i])
        return B(S,i+1)
    elif S[i] =='$':
        return C(S,i+1)
    else:
        return B(S,i+1)
def C(S,i):
    print("C-->", end="")
    if i < len(S):
        if S[i]=='a':
            if st[-1] == 'a':
                st.pop()
                return C(S,i+1)
            else:
                print('No')
                return False
        
        elif S[i]=='b':
            if st[-1] == 'b':
                st.pop()
                return C(S,i+1)
            else:
                print('No')
                return False
        elif st[-1]=='z0':
            st.pop()
            return D(S,i+1)
        else:
            return C(S,i+1)
def D(S,i):
    print("D-->", end="")
    if len(st)==0:
        print("Yes")
    else:
        print("No")

#main
S=input("Enter the string with $ in the middle part:")
A(S,0)
        
