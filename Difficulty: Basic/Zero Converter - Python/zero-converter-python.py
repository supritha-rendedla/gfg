def pos(n):
    ## Write the code
    if n==0:
        print("already Zero")
    elif n>0:
        for i in range(n-1,-1,-1):
            print(i,end=" ")
def neg(n):
    if n==0:
        print("already Zero")
    elif n<0:
        for i in range(n,1):
            print(i,end=" ")