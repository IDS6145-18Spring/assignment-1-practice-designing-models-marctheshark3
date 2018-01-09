import math
from soil import soil

class floridiasand(soil):
    '''This is a string bean'''

    def __init__(self, n, w, wet, c):
        '''Set the name and vertices of the shape'''
        soil.__init__(self,n, w, wet, c)


    def ProvideNutrients(self):
        '''Every vegtable grows differently'''    
        if self.nutrients >= 1.0:
            self.nutrients -= 1.0
            return 1.0
        else:
            return None