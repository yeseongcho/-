X = [1, -1, 2, -4, 51, -6, 2, -45, 25, 31, -21]
n = len(X)
MaxSoFar = 0

for L in range(n) :
    for U in range(L+1, n+1) :
        sum = 0
        for i in range(L, U) :
            sum = sum + X[i]
            if MaxSoFar < sum :
                MaxL, MaxU, MaxSoFar = L, U, sum


for i in range(MaxL, MaxU+1) :
    print(X[i], end = " ")


"""
for L in range(n) :
    for U in range(L+1, n+1) :
        sum = 0
        for i in range(L, U) :
            sum = sum + X[i]
            if MaxSoFar < sum :
                MaxL, MaxU, MaxSoFar = L, U, sum


for i in range(MaxL, MaxU+1) :
    print(X[i], end = " ")
"""
print(" ")
print(MaxSoFar)


