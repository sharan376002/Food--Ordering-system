from abc import ABC,abstractmethod

@abstractmethod
class abstractitem(ABC):
    def __init__(self, name,rating= None):
        self.name = name
        self.rating = rating