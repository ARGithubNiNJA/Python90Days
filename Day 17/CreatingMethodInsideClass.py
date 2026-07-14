class User:
    def __init__(self, id, username):
        self.user_Id=id
        self.username=username
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following+=1
        self.followers+=1

user_1=User(id=1,username='user1')
user_2=User(id=2,username='user2')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)