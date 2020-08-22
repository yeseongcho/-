from random import randint

def fitted(m, posit):
    j, k = posit
    return randint(0,3) == 0

def put_plm(plm, posit):
    j, k = posit
    # put the polyomino into output

def undo_plm(plm, posit):
    j, k = posit
    # Undo the polyomino in the output

def find_and_try(plm_lst, success = False, level = 0):
    if success: return success, level-1 
    for i in plm_lst:
        plm, remLst = plm_lst[0], plm_lst[1:]
        for j in range(square):
            for k in range(square):
                if fitted(plm,(j,k)):
                    put_plm(plm,(j,k))
                    print("\t" * level, plm)
                    success, level = find_and_try(remLst,   \
                                len(remLst) == 0,level+1)
                    if success: return success, level - 1
                    else: undo_plm(plm, (j,k))
                else: print("\t" * level, plm, "Retry")
        return success, level-1  
    
data = ["A","B","C","D"]
square = randint(2, 2)
print((square, square))
output = [[0] * square for i in range(square)]
print(output)
if find_and_try(data)[0]:
    print("\n Success")
else:
    print("\n Failue")



