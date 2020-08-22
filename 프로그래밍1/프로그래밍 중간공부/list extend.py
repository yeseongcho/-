
list1 = [1, 2, 3]
lt = ["a", "b"]
tp = ("a", "b")
st = "ab"

list1.extend(lt)
#[1, 2, 3, 'a, 'b']
list1.extend(tp)
# 문제는 얘도 [1, 2, 3, 'a', 'b']
list1.extend(st)
# 얘도 [1, 2, 3, 'a', 'b']
print(list1)
#라는 것이다!

#append의 정의를 살펴보자!

# "Append all elements in a sequence K to list!
# 저 seq는 tuple, string list를 의미하는데 거기 있는 모드 요소들을 다 리스트에 넣은 단 소리!
# 그게 tuple이든 list든 뭐든 그 모든 sequence를 넣는다는 의미다!!

"""
list1 = ['a', 'b', 'c']

print(min(list1))
print(max(list1))
print(sum(list1))
"""
