#Dictionaries{key, value}
programming_language={
    "name": "Arsh",
    "age": 17,
    "course": "Python",
    "city": "Delhi",
}
#printing dictionaray
print(programming_language)
#printing a specific value using key
print(programming_language["name"])


#inserting a value
programming_language["job"] = "Software Engineer"
print(programming_language)

#Looping over the dictionary
for key in programming_language:
    print(key)
    print(programming_language[key])

#emptying a dictionary
programming_language={}
print(programming_language)
#Assiginng the value