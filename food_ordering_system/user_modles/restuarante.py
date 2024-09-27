from user_modles.Abstractitem import abstractitem
from user_modles.foodmenu import foodmenu

class retaurant(abstractitem):

    def __init__(self,name,rating,location,offers):
        super(). __init__(name,rating)
        self.location = location
        self.offers = offers
        self.__foodmenu = []
         
    @property
    def foodmenu(self):
        return self.__foodmenu

    @foodmenu.setter
    def fooditems(self,items):
        for item in items:
            if not isinstance(item,foodmenu):
                print("Invlid Food Item..")
                return
        self.__foodmenu = items 