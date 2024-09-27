from user_modles.fooditem import fooditem
from user_modles.foodmenu import foodmenu
from user_modles.restuarante import retaurant


class foodmanager:

    def __init__(self):
        self.Resturants = self.__PrepareRestaurants()

    def __PrepareFoodItems(self):
        item1 = fooditem("Dosa", 4.3,50,"the dosa was really nice")
        item2 = fooditem("Veg-Briyani", 4.9,150,"the briyani was really nice")    
        item3 = fooditem("Noodles", 4.6,90,"the noodles was really nice")    
        item4 = fooditem("Fired-Rice", 4.4,90,"the rice was really nice")    
        item5 = fooditem("Parrata", 4.8,50,"the parrata was really nice")    
        return item1,item2,item3,item4,item5

    def __PrepareFoodMenus(self):
        fooditems = self.__PrepareFoodItems()
        menu1 = foodmenu("VEG")
        menu1.Fooditems = [fooditems[0],fooditems[1]]
        menu2 = foodmenu("NON-VEG")
        menu2.Fooditems = [fooditems[3],fooditems[4]]
        menu3 = foodmenu("Chinese")
        menu3.Fooditems = [fooditems[3]]
        return[menu1, menu2,menu3]

    
    def __PrepareRestaurants(self):

        foodmenu = self.__PrepareFoodMenus()
        res1 = retaurant("A2b",5,"puducherry",20)
        res1.foodmenu = [foodmenu[0]]
        res2 = retaurant("ethu-oru-kada",5,"puducherry",30)
        res2.foodmenu = [foodmenu[0], foodmenu[1]]
        res3 = retaurant("nee poi sapudu..",5,"puducherry",20)
        res3.foodmenu = [foodmenu[0], foodmenu[1],foodmenu[2]]
        return [res1,res2,res3]
