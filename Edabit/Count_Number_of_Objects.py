#Count Number of Instances
#Create a class named User and create a way to check the number of users (number of instances) were created, so that the value can be accessed as a class attribute.
class User:
    user_count=0
    def __init__(self,t):
        self.t=t
        self.username=t
        User.user_count+=1
u1 = User("johnsmith10")
print(User.user_count)
# 1
u2 = User("marysue1989")
print(User.user_count)
# 2
u3 = User("milan_rodrick")
print(User.user_count)
#Make sure that the usernames are accessible via the instance attribute username.
# 3
print(u1.username)
#"johnsmith10"
print(u2.username)
#"marysue1989"
print(u3.username)
#"milan_rodrick"
