from user_modles.users import users
from user_modles.user_managing import UserManager
from  file_control.mainmenu import Mainmenu

class Login_system:
    def login(self):
        email = input("Enter your Email Id :")
        password = input("Enter your password(it must contains 8 char) : ")

        user = UserManager.find_users(email,password)

        if user is not None:
            print("<<.....Login Sucessfully.....>>")
            menu = Mainmenu()
            menu.start()
        else:
            print("Invalid mailID /password")

 
    def register(self):
    
        name = input('Enter the Name : ')
        mobile = int(input("Enter the Mobile number : "))
        email = input("Enter your Email Id :")
        password = input("Enter your password(it must contains 8 char) : ")
        
        
        user1 = users(name,mobile,email,password)
        UserManager.add_users(user1)
       

    def guest(self):
        pass
    
    def Validate_option(self,choice):
        
        if choice==1:     #we can use this code using a getatt() also..
            self.login()
        elif choice==2:
            self.register()
        elif choice==3:
            self.guest()
        elif choice==4:
            print("<< Thank You >>")
            exit()
        else:
            print("Invalid Input.. please give give correct input...")    







class FoodApp:

    userOPtions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}

    @staticmethod
    def Init():
        print("<< Welcome to Food Ordering System >>")

        Login_users = Login_system()

        while True:

            for option in FoodApp.userOPtions:
                print(f"{option}. {FoodApp.userOPtions[option]}",end="  ")
                print()


        
            try:
                choice = int(input("Enter the any choice from the options :"))
                Login_users.Validate_option(choice)
            except:
                print("Invail input enter vaild choice..")    





FoodApp.Init()