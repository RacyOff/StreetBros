import pygame
from krogla import Krogla
from strela import Strela  # Add this import at the top
from krogla import Krogla  # You'll likely need this too

length = 1280
width = 720
screen = pygame.display.set_mode((length, width))
class Borec:
    def __init__(self, ime, health, avatar, Tocka_na_udarec, hitrost, pozicija, blok, udarec, tek, x, y, smer, walk, skok, hitrost_skoka, special):
        self.tek = tek
        self.ime = ime
        self.health = health
        self.max_health = health  
        self.avatar = avatar
        self.Tocka_na_udarec = Tocka_na_udarec
        self.hitrost = hitrost
        self.pozicija = pozicija
        self.blok = blok
        self.udarec = udarec
        self.smer = smer
        self.walk = walk
        self.skok = skok
        self.hitrost_skoka = 0
        self.special = special
        self.x = x
        self.y = y
        self.krogle = []  
        self.cooldown = 0  
        self.krogle = []  
        self.cooldown_krogle = 0
        self.strele = []
        self.cooldown_strela = 0
        self.hitbox = (self.x - 200, self.y-200)
        self.crouch = False
        self.udarec_animacija = False
        self.udarec_frame = 0
        self.udarec_cooldown = 0
        self.zadnji_udarec_frame = -1 
        self.score = 0
        self.stamina = 100
        self.max_stamina = 100
    
    def zbij_health(self, vrednost):
        self.health -= vrednost

    def ustvari_strelo(self):
        if self.cooldown_strela <= 0:
            zacetni_x = self.x + 150 if self.smer == 1 else self.x - 50
            nova_strela = Strela(zacetni_x, self.y + 100, self.smer)
            self.strele.append(nova_strela)
            self.cooldown_strela = 30
            return True
        return False

    def ustvari_kroglo(self):
        if self.cooldown_krogle <= 0:
            zacetni_x = self.x + 150 if self.smer == 1 else self.x - 50
            nova_krogla = Krogla(zacetni_x, self.y + 100, self.smer)
            self.krogle.append(nova_krogla)
            self.cooldown_krogle = 30  
            return True
        return False

    def posodobi_krogle(self, sirina_zaslona, opponent):
        if self.cooldown_krogle > 0:
            self.cooldown_krogle -= 1
        
        for krogla in self.krogle[:]:
            krogla.posodobi()
            
            if krogla.je_izven_zaslona(sirina_zaslona):
                self.krogle.remove(krogla)
                continue
                
            if krogla.trk_z_igralcem(opponent):
                self.special = False
                if opponent.blok == False or (opponent.blok == True and opponent.smer == self.smer):
                    opponent.zbij_health(10)
                else:
                    pass
                    
                self.krogle.remove(krogla)

    def posodobi_strele(self, sirina_zaslona, opponent):
        if self.cooldown_strela > 0:
            self.cooldown_strela -= 1
        
        for strela in self.strele[:]:
            strela.posodobi()
            
            if strela.je_izven_zaslona(sirina_zaslona):
                self.strele.remove(strela)
                continue
                
            if strela.trk_z_igralcem(opponent):
                self.special = False
                if opponent.blok == False or (opponent.blok == True and opponent.smer == self.smer):
                    opponent.zbij_health(10)
                else:
                    pass
                self.strele.remove(strela)

    def get_rezilo_pozicija(self):
        if self.smer == 1:  # Desno
            return (self.x + 200, self.y + 100, self.x + 300, self.y + 250)
        else:  # Levo
            return (self.x, self.y + 100, self.x + 100, self.y + 250)

    def premik_levo(self):
        self.x -= 20
        
    def premik_desno(self):
        self.x += 20
    
    def poklekni(self):
        self.y += 10
        
    def blok(self):
        self.blok = True
        
    def konec_bloka(self):
        self.blok = False
        
    def hoja(self):
        self.walk = True
        
    def skoci(self):
        if not self.skok:
            self.skok = True
            self.hitrost_skoka = -15

    def udari(self, other):
        if (other.x > self.x and 30 < (other.x - self.x) < 60) or (other.x < self.x and  30 < (self.x - other.x) < 60):
            if other.blok == False or(self. smer == other.smer and other.blok == True):
                other.zbij_health()

    def preveri_border(self):
        if self.x <= -50:
            self.x = -50
        elif self.x >= length-300:
            self.x = length-300

    def preveri_health(self):
        if self.health <= 0:
                screen.blit()