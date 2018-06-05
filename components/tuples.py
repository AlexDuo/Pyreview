list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# change list 1 into set

list_1 = set(list_1)

print(list_1, type(list_1))

# to format the sytanx you just wrote, could use control+alt+L
list_2 = set([2,4,6,5,8,3,7,8,])

duplicate = list_1.intersection(list_2)

union = list_1.union(list_2)

difference = list_1.difference(list_2)

difference2 = list_2.difference(list_1)

yesorno = list_2.issubset(list_1)

yesorno2 = list_1.issuperset(list_2)

# print(duplicate)
#
#
# print(union)
#
#
# print(difference)

# 对称差集概念：取出两个集合中互相没有的元素
# isdisjoint means 两个集合有没有交集
# &交集  |并集  - 差集  a^b 对称差集(在a中或者在b中但是同时存在a或者b中)
print(difference2)

print(yesorno)

print(yesorno2)