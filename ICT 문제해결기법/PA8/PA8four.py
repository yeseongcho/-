mountain = {}
N = int(input())
Max = 0
maxs = 0
max_dic = {}

for floor in range(N) :
    mountain[floor] = [int(x) for x in input().split()]
    maxs = max(mountain[floor])
    #print(mountain[floor].index(maxs))
    #print("why?")
    max_dic[floor] = (maxs, mountain[floor].index(maxs))


index = 0
leaf = {}


def Find(node, leaf) :
    if node not in leaf :
        leaf[node] = node
        return node
    
    elif node == leaf[node] :
        return node
    
    else : 
        node = leaf[node]
        return Find(node, leaf)
    

def compare(row, val, leaf, result1, result2, result3, result4) :
    index = mountain[row].index(val)
    if row == 0 :
        if index == 0 :
            if val < mountain[row][index+1] :
                leaf[(row, index+1)] = (row, index)
                result1 = Find((row,index), leaf)
                #leaf[(val, index+1)] = result
            if val < mountain[row+1][index] :
                leaf[(row+1, index)] = (row, index)
                result2 = Find((row, index), leaf)
                #print(result2)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val)
                    
            
        if index == N-1 :
            if val < mountain[row][index-1] :
                leaf[(row, index-1)] = (row, index)
                result1 = Find((row, index), leaf)

            if val < mountain[row+1][index] :
                leaf[(row+1, index)] = (row, index)
                result2 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])
            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val)
                
                

        else :
            if val < mountain[row][index+1] :
                leaf[(row, index+1)] = (row, index)
                result1 = Find((row, index), leaf)

            if val < mountain[row][index-1] :
                leaf[(row, index-1)] = (row, index)
                result2 = Find((row, index), leaf)

            if val < mountain[row+1][index] :
                leaf[(row+1, index)] = (row, index)
                result3 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])

            return  min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val)
            
    elif row == N-1 :
        if index == 0 :
            if val < mountain[row-1][index] :
                leaf[(row-1, index)] = (row, index)
                result = Find((row, index), leaf)
            if val < mountain[row][index+1] :
                leaf[(row, index+1)] = (row, index)
                result2 = Find((row, index), leaf)
            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val)
        
                       
        elif index == N-1 :
            if val < mountain[row-1][index] :
                leaf[(row-1, index)] = (row, index)
                result1 = Find((row, index), leaf)
            if val < mountain[row][index-1] :
                leaf[(row, index-1)] = (row, index)
                result2 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])


            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], val)
            
            
        else :
            if val < mountain[row-1][index] :
                leaf[(row-1, index)] = (row, index)
                result1 = Find((row, index), leaf)

            if val < mountain[row][index-1] :
                leaf[(row, index-1)] = (row, index)
                result2 = Find((row, index), leaf)

            if val < mountain[row][index+1] :
                leaf[(row, index+1)] = (row, index)
                result3 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])

            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val)          

    else :
        if index == 0 :
            if val < mountain[row][index+1] :
                leaf[(row, index+1)] = (row, index)
                result1 = Find((row, index), leaf)

            if val < mountain[row+1][index] :
                leaf[(row+1, index)] = (row, index)
                result2 = Find((row, index), leaf)

            if val < mountain[row-1][index] :
                rleaf[(row-1, index)] = (row, index)
                result3 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])
                #print("###")

            if result2 == () :
                result2 = (row, max_dic[row][1])
                #print("###")

            if result3 == () :
                result3 = (row, max_dic[row][1])
                #print("###")
            #print(result1)
            #print(result2)
            #print(result3)

            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val)
        
                
            
        elif index == 3 :
            if val < mountain[row][index-1] :
                leaf[(row, index-1)] = (row, index)
                result = Find((row, index), leaf)

            if val < mountain[row+1][index] :
                leaf[(row+1, index)] = (row, index)
                result2 = Find((row, index), leaf)

            if val < mountain[row-1][index] :
                leaf[(row-1, index)] = (row, index)
                result3 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])


            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], val)
            


        else :
            if val < mountain[row][index-1] :
                leaf[(row, index-1)] = (row, index)
                result1 = Find((row, index), leaf)

            if val < mountain[row][index+1] :
                leaf[(row, index+1)] = (row, index)
                result2 = Find((row, index), leaf)

            if val < mountain[row+1][index] :
                leaf[(row+1, index)] = (row, index)
                result3 = Find((row, index), leaf)
            
            if val < mountain[row-1][index] :
                leaf[(row-1, index)] = (row, index)
                result4 = Find((row, index), leaf)

            if result1 == () :
                result1 = (row, max_dic[row][1])

            if result2 == () :
                result2 = (row, max_dic[row][1])

            if result3 == () :
                result3 = (row, max_dic[row][1])

            if result4 == () :
                result4 = (row, max_dic[row][1])

            return min(mountain[result1[0]][result1[1]], mountain[result2[0]][result2[1]], mountain[result3[0]][result3[1]], mountain[result4[0]][result4[1]], val)
                
              
for row in mountain :
    for val in mountain[row] :
        result1 = ()
        result2 = ()
        result3 = ()
        result4 = ()
        leafs = compare(row, val, leaf, result1, result2, result3, result4)
        print(leafs)
        print("#")
        print(val)
        print("############")
        Max = max(Max, val - leafs)

print(Max)
        
