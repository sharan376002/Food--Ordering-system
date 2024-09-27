from user_modles.Abstractitem import abstractitem



class fooditem(abstractitem):

    def __init__(self,name,rating,price,description):
        super().__init__(name,rating)
        self.price = price
        self.description = description

            