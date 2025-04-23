import pygame #type: ignore
import sys #type:ignore
import time
import random
from krogla import Krogla
from strela import Strela
from borec import Borec
from mapa import MAP
from special import SPECIAL


pygame.init()
pygame.display.set_caption("StreetBros - Oskar Kopač, R2C")

length = 1280
width = 720
screen = pygame.display.set_mode((length, width))
clock = pygame.time.Clock()
center = screen.get_rect().center
Borba = True
Menu = False
frame_counter = 0 
game_over = False  # Novo stanje za konec igre
winner = None  

#Dodajanje Framov (za oba igralca): crouch, blokada, napad, strel ... --------------------------------------------------------------------------------

PD1 = pygame.transform.scale(pygame.image.load("StreetBros\player1\\attack\player1_hit_desno_1.png"),(350,350))
PD2 = pygame.transform.scale(pygame.image.load("StreetBros\player1\\attack\player1_hit_desno_2.png"), (350,350))
PD3 =pygame.transform.scale(pygame.image.load("StreetBros\player1\\attack\player1_hit_desno_3.png"), (350,350))

PL1 = pygame.transform.scale(pygame.image.load("StreetBros\player1\\attack\player1_hit_levo_1.png"), (350,350))
PL2 =pygame.transform.scale(pygame.image.load("StreetBros\player1\\attack\player1_hit_levo_2.png"), (350,350))
PL3 =pygame.transform.scale(pygame.image.load("StreetBros\player1\\attack\player1_hit_levo_3.png"), (350,350))


udar1 = pygame.transform.scale(pygame.image.load("StreetBros/efekti/udar1.png"), (100, 100)),
udar2 = pygame.transform.scale(pygame.image.load("StreetBros/efekti/udar1.png"), (100, 100)),
udar3 = pygame.transform.scale(pygame.image.load("StreetBros/efekti/udar1.png"), (100, 100))

game_over_bg = pygame.transform.scale(pygame.image.load("StreetBros/efekti/game_over.jpg"), (1280,720))
pritisni_enter = pygame.transform.scale(pygame.image.load("StreetBros/efekti/pritisni_enter.png"), (300,200))
game_over_icon = pygame.transform.scale(pygame.image.load("StreetBros/efekti/game_over_icon.png"),(500,500))
udar_effects = []

# Mapi
NightCity = MAP("StreetBros/wp5418813-anime-pixel-art-wallpapers.png", length, 0, width, 0, "StreetBros/music/Seek & Destroy (Remastered).mp3")
Forest_Map = MAP("StreetBros/8-bit-graphics-pixels-scene-with-forest (1).jpg", length, 0, width, 0, "StreetBros/music/Master of Puppets (Remastered).mp3")  

#Frami za Player1
player1_crouch_desno = pygame.transform.scale(pygame.image.load("StreetBros/player1/crouch/player1_crouch_desno.png"), (350, 350))
player1_crouch_levo = pygame.transform.scale(pygame.image.load("StreetBros/player1/crouch/player1_crough_levo.png"), (350, 350))
player1_stand_levo = pygame.transform.scale(pygame.image.load("StreetBros/player1/stand/player1_stand_levo.png"), (350, 350))
player1_stand_desno = pygame.transform.scale(pygame.image.load("StreetBros/player1/stand/player1_stand_desno.jpg"), (350, 350))
player1_walk_desno_2 = pygame.transform.scale(pygame.image.load("StreetBros/player1/walk-desno/player1_walk_desno_2.png"), (350, 350))
player1_walk_desno_3 = pygame.transform.scale(pygame.image.load("StreetBros/player1/walk-desno/player1_walk_desno_3.png"), (350, 350))
player1_blok_desno = pygame.transform.scale(pygame.image.load("StreetBros/player1/defend/player1_blok_desno.png"), (350, 350))
player1_blok_levo = pygame.transform.scale(pygame.image.load("StreetBros/player1/defend/player1_blok_levo.png"), (350, 350))
player1_walk_levo_2 = pygame.transform.scale(pygame.image.load("StreetBros/player1/walk-levo/player1_walk_levo_2.png"), (350, 350))
player1_walk_levo_3 = pygame.transform.scale(pygame.image.load("StreetBros/player1/walk-levo/player1_walk_levo_3.png"), (350, 350))
player1_fireball_desno = pygame.transform.scale(pygame.image.load("StreetBros/player1/special/player1_fireball_desno.png"), (350, 350))
player1_fireball_levo = pygame.transform.scale(pygame.image.load("StreetBros/player1/special/player1_fireball_levo.png"), (350, 350))

#Frami za Player2
player2_crouch_levo = pygame.transform.scale(pygame.image.load("StreetBros/player2/crouch/player2_crouch_levo.png"), (350, 350))
player2_crouch_desno = pygame.transform.scale(pygame.image.load("StreetBros/player2/crouch/player2_crouch_desno.png"), (350, 350))
player2_stand_levo = pygame.transform.scale(pygame.image.load("StreetBros/player2/stand/player2_stand_levo.png"), (350, 350))
player2_stand_desno = pygame.transform.scale(pygame.image.load("StreetBros/player2/stand/player2_stand_desno.png"), (350, 350))
Player2_walk_levo_2 = pygame.transform.scale(pygame.image.load("StreetBros/player2/walk-levo/player1_walk_levo_2.png"), (350, 350))
Player2_walk_levo_3 = pygame.transform.scale(pygame.image.load("StreetBros/player2/walk-levo/player1_walk_levo_3.png"), (350, 350))
Player2_walk_levo_1 = pygame.transform.scale(pygame.image.load("StreetBros/player2/walk-levo/player2_walk_levo_1.png"), (350, 350))
Player2_walk_desno_1 = pygame.transform.scale(pygame.image.load("StreetBros/player2/walk-desno/Player2_walk_desno_1.png"), (350, 350))
Player2_walk_desno_2 = pygame.transform.scale(pygame.image.load("StreetBros/player2/walk-desno/Player2_walk_desno_2.png"), (350, 350))
Player2_walk_desno_3 = pygame.transform.scale(pygame.image.load("StreetBros/player2/walk-desno/Player2_walk_desno_3.png"), (350, 350))
player2_blok_desno = pygame.transform.scale(pygame.image.load("StreetBros/player2/defend/player2_blok_desno.png"), (350, 350))
player2_blok_levo = pygame.transform.scale(pygame.image.load("StreetBros/player2/defend/player2_blok_levo.png"), (350, 350))
player2_strela_desno = pygame.transform.scale(pygame.image.load("StreetBros/player2/strela/player2_strela_desno.png"), (350, 350))
player2_strela_levo = pygame.transform.scale(pygame.image.load("StreetBros/player2/strela/player2_strela_levo.png"), (350, 350))

#slike za p2 attack na blizu
p2_cd_1=pygame.transform.scale(pygame.image.load("StreetBros/player2/cross/player2_attack_desno_1.png"), (350, 350))
p2_cd_2=pygame.transform.scale(pygame.image.load("StreetBros/player2/cross/player2_attack_desno_2.png"), (350, 350))
p2_cd_3=pygame.transform.scale(pygame.image.load("StreetBros/player2/cross/player2_attack_desno_3.png"), (350, 350))

p2_cl_1=pygame.transform.scale(pygame.image.load("StreetBros/player2/cross/player2_attack_levo_1.png"), (350, 350))
p2_cl_2=pygame.transform.scale(pygame.image.load("StreetBros/player2/cross/player2_attack_levo_2.png"), (350, 350))
p2_cl_3=pygame.transform.scale(pygame.image.load("StreetBros/player2/cross/player2_attack_levo_3.png"), (350, 350))

player2_attack_desno = [p2_cd_1,p2_cd_2,p2_cd_3]
player2_attack_levo = [p2_cl_1,p2_cl_2,p2_cl_3]

strela = pygame.transform.scale(pygame.image.load("StreetBros/player2/strela/strela_1.png"), (150, 150))

# Seznami za animacije hoje
Player1_hoja_desno = [player1_stand_desno, player1_walk_desno_2, player1_walk_desno_3]
Player1_hoja_levo = [player1_stand_levo, player1_walk_levo_2, player1_walk_levo_3]
Player2_hoja_levo = [Player2_walk_levo_2, Player2_walk_levo_1, Player2_walk_levo_3]
Player2_hoja_desno = [Player2_walk_desno_1, Player2_walk_desno_2, Player2_walk_desno_3]

Current_slika_1 = pygame.transform.scale(player1_stand_desno, (350,350))
Current_slika_2 = pygame.transform.scale(player2_stand_levo,(350,350))

krogla1 = pygame.transform.scale(pygame.image.load("StreetBros/player1/special/ogenj_1.png"), (150,150))
krogla2 = pygame.transform.scale(pygame.image.load("StreetBros/player1/special/ogenj_2.png"), (150,150))
fireball_slika = pygame.transform.scale(pygame.image.load("StreetBros/player1/special/ogenj_1.png"), (150,150))

odzadje = pygame.image.load("StreetBros/efekti/waitingPic.jpg")
logo = pygame.transform.scale(pygame.image.load("StreetBros/efekti/logo.png"),(600,600))


player1_attack_desno = [PD1,PD2,PD3]
player1_attack_levo = [PL1,PL2,PL3]

#------------------------------------------ konec dodajanja slik--------------------------------------------------------------------

class UdarEffect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.images = [udar1, udar2, udar3]


#ustvarim igralce s classom borec
Player1 = Borec("Bro Num 1", 100, None, 5, 50, "Stand", False, False, False, -30, 370, 1, False, False, 0, False)
Player2 = Borec("Bro Num 2", 100, None, 5, 50, "Stand", False, False, False, 850, 370, 0, False, False, 0, False)

#Začetne koordinate Playerjev (Y): za skos
Player1_y_start = Player1.y
Player2_y_start = Player2.y

krogle_frames = [krogla1, krogla2]

# Specialni efekti
fireball = SPECIAL(Player1.x, Player1.y)
Max_frames = 10
special_frames = 0

frames_krogle = []


#Funkcija ki naklučno izbere eno izmed dveh map

def izberi_mapo():
    global NightCity, Forest_Map
    pygame.mixer.music.load("StreetBros/music/lobby.mp3")  
    pygame.mixer.music.set_volume(0.5) 
    pygame.mixer.music.play()
    screen.blit(odzadje, (0,0))
    screen.blit(logo, logo.get_rect(center = screen.get_rect().center))
    screen.blit(pritisni_enter, (0, 500))
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
                izbrana = random.choice([NightCity, Forest_Map])
                pygame.mixer.music.load(izbrana.sound)
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
                return izbrana
                
        clock.tick(60)
            

pygame.mixer.music.stop()
izbrana_mapa_ = izberi_mapo()

if izbrana_mapa_ == NightCity:
    izbrana_mapa = NightCity.url

if izbrana_mapa_ == Forest_Map:
    izbrana_mapa = Forest_Map.url

# Glavna zanka igre
pygame.mixer.music.play(-1)


def konec_igre(): #Funkcija se kliče, ko je igra končana (Nekdo ima score 3)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("StreetBros/music/pixel-dreams-259187.mp3")
    pygame.mixer.music.play(-1)
    
    # Display winner information
   
    
    while True:
        screen.blit(odzadje, (0,0))
        screen.blit(game_over_icon, game_over_icon.get_rect(center = screen.get_rect().center))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Reset everything including scores
                Player1.health = Player1.max_health
                Player2.health = Player2.max_health
                Player1.x, Player1.y = -30, 370
                Player2.x, Player2.y = 850, 370
                Player1.blok = False
                Player2.blok = False
                Player1.special = False
                Player2.special = False
                Player1.krogle = []
                Player2.strele = []
                Player1.score = 0
                Player2.score = 0
                game_over = False
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load(izbrana_mapa_.sound)
                pygame.mixer.music.play(-1)
                return
                
        clock.tick(60)

#--------------------Main Loop -> event handlerji + klici ključnih funkcij------------------------------------

while Borba:
    starter_x_fireball = Player1.x
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT:
            Borba = False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_c:
                Player1.udarec_animacija = True
                Player1.udarec_frame = 0
                Player1.udarec_cooldown = 15


            if event.key == pygame.K_b and Player1.smer == 1 and Player1.blok == False and Player1.stamina >= 0: 
                Player1.special = True
                Current_slika_1 = player1_fireball_desno
                Player1.stamina -= 20
                Player1.ustvari_kroglo()
              
            if event.key == pygame.K_b and Player1.smer == 0 and Player1.blok == False and Player1.stamina >= 0: 
                Player1.special = True
                Current_slika_1 = player1_fireball_levo
                Player1.stamina -= 20
                Player1.ustvari_kroglo()
                

            Player1.posodobi_krogle(length, Player2)

            if event.key == pygame.K_p:
                Player2.udarec_animacija = True
                Player2.udarec_frame = 0
                Player2.udarec_cooldown = 15
                

            if event.key == pygame.K_w:
                Player1.skoci()

            if keys[pygame.K_v] and Player1.smer == 1:
                Current_slika_1 = player1_blok_desno
                Player1.blok = True
             
            if keys[pygame.K_v] and Player1.smer == 0:
                Current_slika_1 = player1_blok_levo
                Player1.blok = True
            
            if event.key == pygame.K_s and Player1.smer == 1:
                Player1.y += 20 
                Current_slika_1 = player1_crouch_desno
                
            if event.key == pygame.K_s and Player1.smer == 0:
                Player1.y += 20                
                Current_slika_1 = player1_crouch_levo
            
            if event.key == pygame.K_a:
                Player1.smer = 0
                Current_slika_1 = player1_stand_levo
                Player1.hoja()
                
            if event.key == pygame.K_d:
                Player1.smer = 1
                Current_slika_1 = player1_stand_desno
                Player1.hoja()

            # Igralec 2
            if event.key == pygame.K_u and Player2.smer == 1 and Player2.stamina >= 0: 
                Player2.special = True
                Current_slika_2 = player2_strela_desno
                Player2.stamina -= 20
                Player2.ustvari_strelo()

              
            if event.key == pygame.K_u and Player2.smer == 0 and Player2.stamina >= 0: 
                Player2.special = True
                Current_slika_2 = player2_strela_levo
                Player2.stamina -= 20
                Player2.ustvari_strelo()
                


            if event.key == pygame.K_i:
                Player2.skoci()

            if keys[pygame.K_o] and Player2.smer == 1:
                Current_slika_2 = player2_blok_desno
                Player2.blok = True
             
            if keys[pygame.K_o] and Player2.smer == 0:
                Current_slika_2 = player2_blok_levo
                Player2.blok = True

            if event.key == pygame.K_k and Player2.smer == 1:
                Player2.y += 15 
                Current_slika_2 = player2_crouch_desno
                Player2.crouch = True
                
            if event.key == pygame.K_k and Player2.smer == 0:
                Player2.y += 15                
                Current_slika_2 = player2_crouch_levo            
            if event.key == pygame.K_j:
                Player2.smer = 0
                Current_slika_2 = player2_stand_levo
                Player2.hoja()
                
            if event.key == pygame.K_l:
                Player2.smer = 1
                Current_slika_2 = player2_stand_desno
                Player2.hoja()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                Player2.udarec_animacija = False
                if Player2.smer == 1:
                    Current_slika_2 = player2_stand_desno
                else:
                    Current_slika_2 = player2_stand_levo

            if event.key == pygame.K_c:
                Player1.udarec_animacija = False
                if Player1.smer == 1:
                    Current_slika_1 = player1_stand_desno
                else:
                    Current_slika_1 = player1_stand_levo

            # Igralec 1
            if event.key == pygame.K_b and Player1.smer == 1: 
                Current_slika_1 = player1_stand_desno
                
            if event.key == pygame.K_b and Player1.smer == 0: 
                Current_slika_1 = player1_stand_levo

            if event.key == pygame.K_s and Player1.smer == 1:
                Player1.y -= 20
                Current_slika_1 = player1_stand_desno
                Player1.walk = False
                
            if event.key == pygame.K_s and Player1.smer == 0:
                Player1.y -= 20
                Current_slika_1 = player1_stand_levo
                Player1.walk = False
            
            if event.key == pygame.K_v and Player1.smer == 1:
                Current_slika_1 = player1_stand_desno
                Player1.blok = False

            if event.key == pygame.K_v and Player1.smer == 0:
                Current_slika_1 = player1_stand_levo
                Player1.blok = False

            if event.key == pygame.K_d and Player1.smer == 0:
                Current_slika_1 = player1_stand_levo
                Player1.walk = False
                
            if event.key == pygame.K_d and Player1.smer == 1:
                Current_slika_1 = player1_stand_desno
                Player1.walk = False
            
            if event.key == pygame.K_a:
                Current_slika_1 = player1_stand_levo
                Player1.walk = False

            # Igralec 2
            if event.key == pygame.K_u and Player2.smer == 1: 
                Current_slika_2 = player2_stand_desno
                
            if event.key == pygame.K_u and Player2.smer == 0: 
                Current_slika_2 = player2_stand_levo

            if event.key == pygame.K_o and Player2.smer == 0:
                Current_slika_2 = player2_stand_levo
                Player2.blok = False

            if event.key == pygame.K_o and Player2.smer == 1:
                Current_slika_2 = player2_stand_desno
                Player2.blok = False

            if event.key == pygame.K_k and Player2.smer == 1:
                Player2.y -= 15
                Current_slika_2 = player2_stand_desno
                Player2.walk = False
                Player2.crouch = False
                
            if event.key == pygame.K_k and Player2.smer == 0:
                Player2.y -= 15
                Current_slika_2 = player2_stand_levo
                Player2.walk = False
                Player2.crouch = False
            
            if event.key == pygame.K_l and Player2.smer == 0:
                Current_slika_2 = player2_stand_levo
                Player2.walk = False
                
            if event.key == pygame.K_l and Player2.smer == 1:
                Current_slika_2 = player2_stand_desno
                Player2.walk = False
            
            if event.key == pygame.K_j:
                Current_slika_2 = player2_stand_levo
                Player2.walk = False

    Player1.posodobi_krogle(1280, Player2)
    Player2.posodobi_strele(1280, Player1)

    # Premikanje igralcev
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        Player2.premik_desno()
        Player2.hoja()

    if keys[pygame.K_j]:
        Player2.premik_levo()
        Player2.hoja()

    if keys[pygame.K_d]:
        Player1.premik_desno()
        Player1.hoja()

    if keys[pygame.K_a]:
        Player1.premik_levo()
        Player1.hoja()

    # Risanje slike
    screen.fill("black")
    screen.blit(izbrana_mapa, (0,0))
    
    # Risanje health bare in imena
    pygame.draw.rect(screen, (255,0,0), (50, 45, 300, 30))
    pygame.draw.rect(screen, (0,255,0), (50, 45, 300 * (Player1.health/Player1.max_health), 30))
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"{Player1.ime}: {Player1.health}/{Player1.max_health}", True, (255,255,255))
    screen.blit(text, (50, 10))
    
    pygame.draw.rect(screen, (255,0,0), (length - 350, 45, 300, 30))
    pygame.draw.rect(screen, (0,255,0), (length - 350,45, 300 * (Player2.health/Player2.max_health), 30))
    text = font.render(f"{Player2.ime}: {Player2.health}/{Player2.max_health}", True, (255,255,255))
    screen.blit(text, (length - 350, 10))
    
    # Specialni udarci -> za kroglo / strelo v arraju jo nariše
    for krogla in Player1.krogle:
        screen.blit(krogla.slika, (krogla.x, krogla.y))
    
    for strela in Player2.strele:
        screen.blit(strela.slika, (strela.x, strela.y))
    
    # Animacija hoje za P1
    if Player1.walk:
        if frame_counter % 8 == 0:  
            if Player1.smer == 1:  
                Current_slika_1 = Player1_hoja_desno[(frame_counter // 8) % len(Player1_hoja_desno)]
            else:
                Current_slika_1 = Player1_hoja_levo[(frame_counter // 8) % len(Player1_hoja_levo)]
    
    # Animacija hoje za Bro2
    if Player2.walk:
        if frame_counter % 8 == 0:  
            if Player2.smer == 1:  
                Current_slika_2 = Player2_hoja_desno[(frame_counter // 8) % len(Player2_hoja_desno)]
            else:
                Current_slika_2 = Player2_hoja_levo[(frame_counter // 8) % len(Player2_hoja_levo)]

    #Udarci za Bro1 in Bro2
    if Player2.udarec_animacija:
        if Player2.udarec_cooldown > 0:
            Player2.udarec_cooldown -= 1
            
            x1, y1, x2, y2 = Player2.get_rezilo_pozicija()
            
            if Player2.udarec_frame in [1, 2] and Player2.zadnji_udarec_frame != Player2.udarec_frame:
                if (x1 < Player1.x + 200 and x2 > Player1.x and
                    y1 < Player1.y + 300 and y2 > Player1.y):
                    
                    if not Player1.blok or (Player1.blok and Player1.smer != Player2.smer):
                        Player1.zbij_health(15)
                        udar_effects.append(UdarEffect((x1+x2)//2, (y1+y2)//2))
                        Player2.zadnji_udarec_frame = Player2.udarec_frame
            
            if Player2.smer == 1:
                Current_slika_2 = player2_attack_desno[Player2.udarec_frame]
            else:
                Current_slika_2 = player2_attack_levo[Player2.udarec_frame]
            
            if frame_counter % 5 == 0:
                Player2.udarec_frame = (Player2.udarec_frame + 1) % len(player2_attack_desno)
        else:
            Player2.udarec_animacija = False
            Player2.zadnji_udarec_frame = -1
            if Player2.smer == 1:
                Current_slika_2 = player2_stand_desno
            else:
                Current_slika_2 = player2_stand_levo


    if Player1.udarec_animacija:
        if Player1.udarec_cooldown > 0:
            Player1.udarec_cooldown -= 1
            
            x1, y1, x2, y2 = Player1.get_rezilo_pozicija()
            
            if Player1.udarec_frame in [1, 2] and Player1.zadnji_udarec_frame != Player1.udarec_frame:
                if (x1 < Player2.x + 200 and x2 > Player2.x and
                    y1 < Player2.y + 300 and y2 > Player2.y):
                    
                    if not Player2.blok or (Player2.blok and Player2.smer != Player1.smer):
                        Player2.zbij_health(15)
                        udar_effects.append(UdarEffect((x1+x2)//2, (y1+y2)//2))
                        Player1.zadnji_udarec_frame = Player1.udarec_frame
            
            if Player1.smer == 1:
                Current_slika_1 = player1_attack_desno[Player1.udarec_frame]
            else:
                Current_slika_1 = player1_attack_levo[Player1.udarec_frame]
            
            if frame_counter % 5 == 0:
                Player1.udarec_frame = (Player1.udarec_frame + 1) % len(player1_attack_desno)
        else:
            Player1.udarec_animacija = False
            Player1.zadnji_udarec_frame = -1
            if Player1.smer == 1:
                Current_slika_1 = player1_stand_desno
            else:
                Current_slika_1 = player1_stand_levo

    # Nariši igralce
    screen.blit(Current_slika_1, (Player1.x, Player1.y))
    screen.blit(Current_slika_2, (Player2.x, Player2.y))

    # Skok igralcov
    if Player1.skok:
        Player1.y += Player1.hitrost_skoka
        Player1.hitrost_skoka += 1
        
        if Player1.y >= Player1_y_start:
            Player1.y = Player1_y_start
            Player1.skok = False
            Player1.hitrost_skoka = 0

    if Player2.skok:
        Player2.y += Player2.hitrost_skoka
        Player2.hitrost_skoka += 1
        
        if Player2.y >= Player2_y_start:
            Player2.y = Player2_y_start
            Player2.skok = False
            Player2.hitrost_skoka = 0

    #ko je score 3, se sproži game over in lastnosti se resetirajo
    if game_over:
        konec_igre()
        game_over = False
    
    #Prikaz healthbarov glede na health igralcov
    pygame.draw.rect(screen, (255,0,0), (50, 45, 300, 30))
    pygame.draw.rect(screen, (0,255,0), (50, 45, 300 * (Player1.health/Player1.max_health), 30))
    health_text = font.render(f"{Player1.ime}: {Player1.health}/{Player1.max_health}", True, (255,255,255))
    score_text = font.render(f"Score: {Player1.score}", True, (255, 255, 255))
    screen.blit(health_text, (50, 10))
    screen.blit(score_text, (50, 80))
    
    pygame.draw.rect(screen, (255,0,0), (length - 350, 45, 300, 30))
    pygame.draw.rect(screen, (0,255,0), (length - 350,45, 300 * (Player2.health/Player2.max_health), 30))
    health_text = font.render(f"{Player2.ime}: {Player2.health}/{Player2.max_health}", True, (255,255,255))
    score_text = font.render(f"Score: {Player2.score}", True, (255, 255, 255))
    screen.blit(health_text, (length - 350, 10))
    screen.blit(score_text, (length - 350, 80))
    
    #Prikaže score še gor
    score_display = font.render(f"{Player1.score} : {Player2.score}", True, (255, 255, 0))
    screen.blit(score_display, (length // 2 - 30, 10))



    #risanje stamine
    pygame.draw.rect(screen, (255,0,0), (50, 60, 300, 30))
    pygame.draw.rect(screen, (0,255,0), (50, 60, 300 * (Player1.stamina/Player1.max_stamina), 30))




    if Player1.health <= 0:
        Player2.score += 1
        Player1.health = Player1.max_health
        Player2.health = Player2.max_health
        Player1.x, Player1.y = -30, 370
        Player2.x, Player2.y = 850, 370
        if Player2.score >= 3:
            game_over = True
            winner = Player2
    
    if Player2.health <= 0:
        Player1.score += 1
        Player1.health = Player1.max_health
        Player2.health = Player2.max_health
        Player1.x, Player1.y = -30, 370
        Player2.x, Player2.y = 850, 370
        if Player1.score >= 3:
            game_over = True
            winner = Player1

    Player1.preveri_border()
    Player2.preveri_border()

    frame_counter += 1
    pygame.display.flip()
    clock.tick(60)

#konec igte
pygame.quit()