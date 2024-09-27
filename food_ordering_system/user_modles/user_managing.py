
class UserManager:
    __Users = []
      
    @classmethod 
    def add_users(cls,user):
        cls.__Users.append(user)
        print("You have been sucessfully Registered")

    @classmethod 
    def find_users(cls,email,psd):
        for user in cls.__Users:
             if user.email == email and user.password == psd:
                 return user
                 
