# Creating a Class (blueprint for our objects)

# class User: # PascalCase((Class names are all one word with the first letter of each word capitalized e.g FullName, StudentScores)
#     pass # allows to make empty class/ functions

# user_1 = User()
# user_1.id = "001"
# user_1.username  = "akila"

# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jack"

# Constructor

class User:

    def __init__(self, user_id,username):
        self.id = user_id # everytime we create a new object with this class we need to provie a id_number and username for each user
        self.username = username ## e.g. user_num = User((id_number),(username))
        self.followers = 0 # i.e. if we were coding up the instagram website we would have a users id, username and a follower count. 
        ##Since everyones follower count will start off the same (0) and maybe increase from there, 
        ###it doesnt make sense for us to provide a follower count of zero every time we create an object
        #### Instead we can set our attribute, followers, to a default value zero and we can add a method to find the follwer count for each user(object)
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = User("001", "akila")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(f"user_1 followers: {user_1.followers}")
print(f"user_1 followers: {user_1.following}")

print(f"user_2 followers: {user_2.followers} ")
print(f"user_2 followingL {user_2.following} ")


