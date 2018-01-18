from cactusmixsoil import cactusmixsoil
from gardenmixsoil import gardenmixsoil
from floridiasand import floridiasand
from compost import compost
from soil import soil

class container:
    ''' A general container class '''

    def __init__(self, n, w, s, v):
        self.nutrientReserve = n
        self.waterReserve = w
        self.soil = s
        self.vegtables = v