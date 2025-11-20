# a=10
# b=0
# c=a/b # 10/0
# print(c)
# print("program ended")
# print("program started")
# try:
#     a=10
#     b=10
#     c=a/b
#     print(c)
# except  ZeroDivisionError:
#     print("we can divide any num with 0")
# print("program ended")    

# ValueError :-- 
# TypeError :-- 
# NameError :-- 
# ZeroDivisionError :-- 
# print("pr started")
# try:
#     a=[1,2,3]
#     b={"id":1}
#     marks1=int(input("entre your marks :--- "))
#     marks2=int(input("enter marks 2 here :-- "))
#     totlaMarks=marks1+marks2
#     print(totlaMarks)
#     b.append(10)
#     print(a[5])
# except AttributeError:
#     print("try to use proper methods for proper datatypes")    
# except ValueError:
#     print("enter proper values")    
# except TypeError:
#     print("give proper datatypes to do proper opeartion")    
# except NameError:
#     print("try to access the name is which is defined")
# except    ZeroDivisionError:
#     print("can t divide with zero")
# except IndexError :
#     print("try to acess the item which is in range of list")    
# print("pr ended")         
    

# try:
#     num = int(input("Enter a number: "))
#     print("Square is:", num * num)
# except ValueError:
#     print("Please enter a valid number.")
# else:
#     print("Good job! You entered a number.")
# else:
#     print("hhhiiii")    
    
class lowAmountEnterNeeded(Exception):
    pass
try:
    bal=4000
    withD=int(input("enter amount to withdraw :--   ")) # 9000
    if withD>bal: # 9000 > 4000
        raise lowAmountEnterNeeded("you are trying to drwa more amount than yr bal amount")
except lowAmountEnterNeeded as l:
    print(l)        
