import pandas as p 


abc=p.read_excel("../../../Downloads/PizzaSales_100.xlsx",engine="openpyxl")
abc2=p.read_csv("./d.csv")
abc3=p.read_json("./d.json")
query="select * from employees"
abc4=p.read_sql(query)
print(abc3)
print(p)

data=p.Series(10)
data2=p.Series("vamsi")
data3=p.Series(True)
data4=p.Series(None)
data5=p.Series([1,2,3,{"id":1}])
print(data5)

students={
    "names":["vamsi","ravi","sathwik","ramesh"],
    "age":[20,12,13,25]
    }
data=p.DataFrame(students)


data.to_excel("data.xlsx",index=False)
data.to_csv("data.csv",index=False)
data.to_json("data.json",index=False)
data.to_html("data.html",index=False)

