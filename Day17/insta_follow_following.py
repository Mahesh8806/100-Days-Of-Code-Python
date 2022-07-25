class User:
    def __init__(self,user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1

user1 = User("001", "Mahesh")
user2 = User("002", "Rahul")

user1.follow(user2);

print(f"User1 Followers:{user1.followers}")
print(f"User1 Followings:{user1.following}")
print(f"User2 Followers:{user2.followers}")
print(f"User2 Followers:{user2.following}")

