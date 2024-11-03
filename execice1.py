A=[]
B=[]
C=[]
S=0
N=int(input("donner la nombre des case des trois tableau:"))
for i in range(N):
    x=int(input("donner un nombre:"))
    A.append(x)
    y=int(input("donner un nombre du tableau B:"))
    B.append(y)
    S=x+y
    C.append(S)
print(A)
print(B)
print(C)
