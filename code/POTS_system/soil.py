class soil:
    ''' A general vegtable class '''

    def __init__(self, n, w, wet, c):
        '''Set the name and vertices of the shape'''
        self.name = n
        self.weight = w
        self.water = wet
        self.nutrients = c


    def __str__(self):
        '''Definition for the print statement'''
        return "soil: '{}' of type ({}) weighs {} grams.".format(
            self.name,str(self.__class__.__name__),
            str(self.weight))


    def ProvideNutrients(self):
        '''Every vegtable grows differently'''
        raise NotImplementedError("Please Implement the Grow method!")
        #This containts a check to make sure subclasses implement this.
        return None

