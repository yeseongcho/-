import math
sqrt = math.sqrt

N = int(input())
ballon = []
parents = {}
for i in range(N) :
    n, k = [int(x) for x in input().split()]
    ballon.append((n, k))

parents[(ballon[0][0], ballon[0][1])] = None
print("%.3f" % ballon[0][1])
if sqrt((ballon[1][1] - ballon[0][1])**2 + (ballon[1][0] - ballon[0][0])**2) <= ballon[0][1] + ballon[1][1] :
    A = (ballon[1][0] - ballon[0][0])**2
    B = 4*(ballon[0][1])
    ballon[1][1] = A/B
    parents[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    print("%.3f" % ballon[1][1])
else :
    parents[(ballon[1][0], ballon[1][1])] = (ballon[0][0], ballon[0][1])
    print("%.3f" % ballon[1][1])

# 아니 바보 같이 다 서칭을 하는 데 이게 효율적일까?
def is_joint(present, previous, parents, bal) :
    print(sqrt((present[0] - previous[0])**2 + (present[1] - previous[1])**2))
    print(present[1] + previous[1])
    while previous == None :
        if sqrt((presents[0] - previous[0])**2 + (present[1]- previous[1])**2) <= present[1] + previous[1] :
            C = (presents[0] - previous[0])**2
            D = 4 * (previous[1])
            present[1] = C/D
            return True, present[1]
        else :
            previous = parent[previous]

    return False, present[1]

for bal in range(2, len(ballon)) :
    parents[(ballon[bal][0], ballon[bal][1])] = (ballon[bal-1][0], ballon[bal-1][1])
    if is_joint((ballon[bal][0], ballon[bal][1]), (ballon[bal-1][0], ballon[bal-1][1]), parents, bal)[0] :
        print("%.3f" % is_joint[1])
    else :
        print("%.3f" % ballon[bal][1])

        
        
