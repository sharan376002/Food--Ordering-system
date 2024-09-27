from user_modles.Abstractitem import abstractitem
from user_modles.fooditem import fooditem

class foodmenu(abstractitem):

    def __init__(self,name):
        super().__init__(name)
        self.__fooditems = [] 

    @property
    def Foodmenu(self):
        return self.__fooditems

    @Foodmenu.setter
    def Fooditems(self,items):
        for item in items:
            if not isinstance(item,fooditem):
                print("Invlid Food Item..")
                return
        self.__fooditems = items     

