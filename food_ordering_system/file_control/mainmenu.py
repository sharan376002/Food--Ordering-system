from foodmanager import Foodmanager


class Mainmenu:
    __Options = {1: "show restutants", 2: "Show FoodItems", 3: "Search Reasturants", 4: "Search Fooditems",
                 5: '"LogOut'}

    def __init__(self):
        self.__foodmanager = Foodmanager()

    def ShowRestaurants(self):
        for res in self.__foodmanager.Resturants:
            print(f"{res.name} = rating : {res.rating}")

    def ShowFooditem(self):
        pass
    def searchrestuarats(self):
        pass
    def searchfooditem(self):
        pass


    def start(self):

        while True:

            for option in Mainmenu.__Options:
                print(f"{option}.{Mainmenu.__Options[option]}")
            print()

            try:
                choice = int(input("please Enter Your Choice : "))
                value = Mainmenu.__Options[choice].replace(" ","")
                getattr(self,value)
            except(ValueError,KeyError):
                print("Invalid Input..please Enter the valid choice")
