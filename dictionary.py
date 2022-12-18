# myDictionary = {
#     "name":"Rajat",
#     "age":"18",
#     "Roll no":"03",
#     "percentage":"80.3%"

# }

# myDictionary.pop("name")
# print(myDictionary)

# myDictionary.update["age"] = 20

# print(myDictionary.items())
# print(myDictionary.values())
# print(myDictionary.keys())
# a = myDictionary.get("name")
# print(a)
# print(len(myDictionary))


#Dictionary are ordered
#Duplicates arwe not allowed
 


myDictionary = {
    "class":{
        "student":{
            "name" : "abc",
            "marks" : {
                "python" : 90,
                "web" : 95
            }
        }
    }
}


print(myDictionary['class']['student']['marks']['web'])