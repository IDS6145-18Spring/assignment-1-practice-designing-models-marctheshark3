from cactusmixsoil import cactusmixsoil
from gardenmixsoil import gardenmixsoil
from floridiasand import floridiasand
from compost import compost
from soil import soil

class decorative(container):
    ''' A general container class '''

    def __init__(self, n, w, s, v, m, c):
        material = m
        color = c
        container.__init__(self, n, w, s, v)