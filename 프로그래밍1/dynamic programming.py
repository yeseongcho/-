def max_sub(X) :
    MaxTail = 0
    MaxSoFar = 0
    for i in range(len(X)) :
        MaxTail = max(0, MaxTail+X[i])
        MaxSoFar = max(MaxSoFar, MaxTail)
    return MaxSoFar

X =  [1, -1, 2, -4, 51, -6, 2, -45, 25, 31, -21]

print(max_sub(X))
