def pattern(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end=" ")
        print("\r")
n=5
pattern(n)
