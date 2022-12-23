class Song():
    favs = [] #class

    #constructor
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    # def is_short(self):
    #     if self.pages < 100:
    #         return True

    #str method
    def __str__(self):
        return f"{self.title}, by {self.artist}"

    #equals method
    def __eq__(self, other):
        if(self.title == other.title and self.artist == other.artist):
            return True
    
    #It's appropriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    # hash code
    __hash__ = None

    # complete str representation, str is for visibility
    def __repr__(self): #added to make list of items invoke str
        return self.__str__()