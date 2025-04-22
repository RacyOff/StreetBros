# strela.py
import pygame

class Strela:
    def __init__(self, x, y, smer):
        self.x = x
        self.y = y
        self.smer = smer  # 1 for right, 0 for left
        self.hitrost = 20
        self.slika = pygame.transform.scale(pygame.image.load("StreetBros/player2/strela/strela_1.png"), (150, 150))
        
    def premik_desno(self):
        self.x += 15
    
    def premik_levo(self):
        self.x -= 15

    def posodobi(self):
        if self.smer == 1:
            self.premik_desno()
        else:
            self.premik_levo()
        
    def je_izven_zaslona(self, sirina_zaslona):
        if self.x < -200 or self.x > sirina_zaslona + 200:
            return True
        return False
        
    def trk_z_igralcem(self, igralec):
        if igralec.x - 50 < self.x < igralec.x + 350 and igralec.y - 50 < self.y < igralec.y + 350 and igralec.crouch != True:
            return True
        return False