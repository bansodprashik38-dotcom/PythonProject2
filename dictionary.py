dict = {"company":"dell",
"ram" : "8gb",
"cpu" : "i7",
"rom" : "128gb",
"year" : "2019"}
dict.update({"processor" :"Ryzen"})
dict["ram"] = "16gb"
dict.pop("year")
dict.popitem()
del dict["rom"]
print(dict)
dict.clear()
print(dict)
dict1=_dict
print(dict1)