from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    
    @abstractmethod
    def __init__(self, first_name, family_name, is_alive=True):
        """constructor for character class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
    

    def die(self):
        pass

    def __str__(self):
        pass    
    def __repr__(self):
        pass
    
class Stark(Character):
    """creating a new stark"""
    def __init__(self, first_name, is_alive=True):
        """constructor for stark class"""
        self.first_name = first_name
        self.is_alive = is_alive
    
    def die(self):
        """set is_alive to false"""
        self.is_alive = False