#class
#we use pass to avoid any exception

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user_1=User('Arsh',21)

print(user_1.name)
print(user_1.age)