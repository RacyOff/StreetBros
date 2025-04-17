import pygame

class Krogla:
    def __init__(self, x, y, smer):
        self.x = x
        self.y = y
        self.smer = smer  # 1 za desno, 0 za levo
        self.hitrost = 15
        self.slika = pygame.transform.scale(pygame.image.load("StreetBros/player1/special/ogenj_1.png"), (150, 150))
        
    def premik_desno(self):
        self.x += 10
    
    def premik_levo(self):
        self.x-= 10

    def posodobi(self):
        if self.smer == 1:
            self.premik_desno()
        else:
            self.premik_levo()
        
    def je_izven_zaslona(self, sirina_zaslona):
        if self.x < -100 or self.x > sirina_zaslona + 100:
            return True
        return False
        
    def trk_z_igralcem(self, igralec):
        if igralec.x - 50 < self.x < igralec.x + 350 and igralec.y - 50 < self.y < igralec.y + 350:
            return True
        else:
            return False