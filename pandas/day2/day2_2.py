import pandas as pd

data = {
    "name": [
        "vamsi", "ravi", "sathwik", "roja", "priya",
        "kiran", "bharath", "sneha", "teja", "anil",
        "ram", "nikhil", "samatha", "bindu", "varun",
        "sravani", "suresh", "madhu", "rajitha", "swetha"
    ],
    "age": [
        20, 19, 22, 21, 18,
        23, 17, 20, 22, 19,
        18, 24, 21, 22, 23,
        20, 19, 25, 18, 21
    ],
    "marks": [
        450, 389, 410, 500, 430,
        390, 250, 470, 480, 300,
        410, 445, 350, 365, 495,
        425, 385, 470, 390, 355
    ],
    "department": [
        "CSE", "ECE", "MECH", "EEE", "CIVIL",
        "CSE", "ECE", "EEE", "MECH", "IT",
        "CSE", "MECH", "IT", "EEE", "CIVIL",
        "ECE", "IT", "CSE", "EEE", "MECH"
    ],
    "phone": [
        "98765", "9876", "987654", "98a7654", "987 654", 
        "987650", "965432", "abc987", "98-7654", "987065",
        "987651", "999999", "987600", "123987", "908765",
        "98700", "98--765", "000000", "9876x4", "965 432"
    ],
    "city": [
        "hyd", "hydreabad", "banglre", "cheni", "mumbaii",
        "hydrebad", "bengluru", "chen", "hyd", "banglor",
        "kadap", "vizag", "vijyawada", "hyd", "tirupathi",
        "cheanni", "hyd", "mumbai", "benglore", "hydrabad"
    ],
    "scholarship": [
        "true", 1, "t", "y", "YES",
        False, True, False, True, 0,
        True, False, "No", "no", "n",
        "f", "False", "True", False, "0"
    ]
}
# 0 :-- "0" :--- 0
df = pd.DataFrame(data)
# df["city"]=df["city"].str.contains("hyd",case=False)
df["city"]=df["city"].str.replace(r"^hyd.*","Hyderabad",case=False,regex=True)
df["city"]=df["city"].str.replace(r"^che.*","Chennai",case=False,regex=True)
df["city"]=df["city"].str.replace(r"^ban.*","Bangolore",case=False,regex=True)
df["city"]=df["city"].str.replace(r"^ben.*","Bangolore",case=False,regex=True)
df["city"]=df["city"].str.replace(r"^mum.*","Mumbai",case=False,regex=True)


# df["scholarship"]=df["scholarship"].astype(int)
# df["scholarship"]=df["scholarship"].map({True:1,False:0})
def clean_bool(x):
    c=str(x).strip().lower()
    if c in ["true", "1", "t", "y", "yes"]:
        return "1"
    if c in ["no", "no", "n",
        "f", "false","0"]  :
        return "0"      
df["scholarship"]=df["scholarship"].apply(clean_bool)

print(df.info())
