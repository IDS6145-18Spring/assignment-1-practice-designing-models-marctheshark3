import math
from vegtable import vegtable

class stringbean(vegtable):
    '''This is a string bean'''

    def __init__(self, n, s, w, wet, c, a, b):
        '''Intializes the vegtable'''
        self.length = 1.0  # start as baby string bean
        self.radius = 0.1
        vegtable.__init__(self,n, s, w, wet, c, a, b)


    def Volume(self):
        '''The volume of a string bean is like a cylinder'''
        return math.pi * self.radius ** 2 * self.length


    def Grow(self):
        '''This is how a stringbean grows'''
        rate =  self.sun*self.water / 1000
        self.radius += 0.1 * rate
        self.length += 0.3 * rate
        self.weight += 0.2 * rate

        volume = self.Volume()
        self.water -= (volume* self.weight) / 2.0
        self.sun = 0.0
        return None