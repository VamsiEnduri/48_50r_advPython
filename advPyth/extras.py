# abc=lambda a,b,c:print(a+b+c)
# abc(10,20,30)

# abc=lambda a:[print(i) for i in a]
# abc([10,20,30])
# nums=[10000,20000,30000]
# # nums={"id":1,"name":"vamsi"}
# def add5(xyz):
#     # print(xyz+5000)
#     return xyz+5000
#     # print("v")

# a=list(map(add5,nums))
# print(a)

# print(list(map(lambda x:x+5,[1,2,3,4,5])))


# a=[1,2,3,4,5]

# print(list(filter(lambda x: x%2 == 0 and x>=4,a)))
# print(list(filter(lambda x : x% 3 ==0 or x %  5==0,a)))

from functools import reduce

a=reduce(lambda x,y:x+y,[1,2,3]) # x=1 y:1+0 =y=1
                               #x=2  y:2+1  y=3
                               #x=3  y:3+3 y=6

print(a)