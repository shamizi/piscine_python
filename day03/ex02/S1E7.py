from S1E9 import Character

class Baratheon(Character):
    """Representating the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        """constructor for baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def die(self):
        """ un baratheon qui meurt"""
        self.is_alive = False
    
    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return self.__str__()



class Lannister(Character):
    """Un lannister ta peeeeur"""
    def __init__(self, first_name, is_alive=True):
        """constructor for baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self):
        """ un baratheon qui meurt"""
        self.is_alive = False
    
    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return self.__str__()
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        ret = cls(first_name)
        ret.is_alive = is_alive
        return(ret)


