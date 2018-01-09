class vegtable:
    ''' A general vegtable class '''

    def __init__(self, n, s, w, wet, c, a, b):
        '''Intializes the vegtable'''
        self.name = n
        self.sun = s
        self.weight = w
        self.water = wet
        self.vitaminC = c
        self.vitaminA = a
        self.vitaminB = b
        self.alive = True


    def __str__(self):
        '''Definition for the print statement'''
        return "vegtable: '{}' of type ({}) weighs {} grams.".format(
            self.name,str(self.__class__.__name__),
            str(self.weight))


    def Grow(self):
        '''Every vegtable grows differently'''
        raise NotImplementedError("Please Implement the Grow method!")
        #This containts a check to make sure subclasses implement this.
        return None


    def Volume(self):
        '''Every vegtable grows differently'''
        raise NotImplementedError("Please Implement the Volume method!")
        #This containts a check to make sure subclasses implement this.
        return None


    def Sun(self, s):
        '''Every vegtable needs light'''
        self.sun = s
        return None


    def Water(self, wet):
        self.water += wet
        return None


    def Die(self):
        self.alive = False