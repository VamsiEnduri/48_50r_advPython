# class bank:
#     def __init__(self):
#         self.bal=5000


#     def get_bal(self): # getter
#         return self.bal

#     def set_bal(self,reAmount): # setter
#         if reAmount<0:
#             print("pls enter +ve values")
#         else:
#             self.bal+=reAmount
#             print(self.bal)    

# obj=bank()        
# # get_value=obj.get_bal()
# # print(get_value)


# obj.set_bal(2000)

class bank:
    def __init__(self):
        self.balance=5000

    @property #getter
    def bal(self): # getter
        return self.balance

    @bal.setter
    def bal(self,*reAmount): # setter
        if reAmount<0:
            print("pls enter +ve values")
        else:
            self.balance+=reAmount
            self.balance+=r2
            print(self.balance)    

obj=bank()
print(obj.bal) # getter
# obj.bal=10000# setter

