y = "*"
K = "="
for x in range(1,13):
    for F in range(1,13):
        Z = x*F
        T = str(Z)
        A = str(x) 
        J = str(F)
        B = A+y+J+K
        V = B+T
        print(V)
    print()

# for x in range(1,13):
#     for y in range(1,13):
#         print(x,"*",y,"=",x*y)
#     print()