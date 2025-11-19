
# # def a():
# #     print("vamsi")

# # def dec(xyz):
# #     def abc():
# #         xyz() #vamsi
# #         print("returned function")
# #     return abc  
# #     # return 10  
# # mno=dec(a)
# # mno()




# def ageChecking():
#     age=int(input("enter yr age here :-- "))
#     if age>=18:
#         print("eligile to vote ....")
#     else:
#         print("no eleigility")    

# def dec(xyz):
#     print("abc")
#     print("vamsi")
#     def abc():
#         xyz()
#         gender =input("enter gender here :--   ")
#         if gender=="Male":
#             print("yes  you are male so go and vote")

#     return abc 
     
#     # return 10  
# m=dec(ageChecking)
# m()



def sal_logger(abc):
    def extraLogic(name,salary):
        print("before sal is 25000")
        abc(name,salary)
    return extraLogic    

def sal_incre(name,salary):
    sal=salary
    name=name
    increemntedSal=sal * 0.10
    print(increemntedSal,"after 10% of incrment and my name is ",name)
a=sal_logger(sal_incre)
a("vamsi",25000)
