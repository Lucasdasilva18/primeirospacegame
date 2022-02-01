import sys, pygame,math
from random import randint
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.display.set_caption('spacegamePC')
p=0
b1=0
b2=0
fonte=pygame.font.SysFont('arial',30,True)


x_tela=1000
y_tela=600
x_navejogador=460
y_navejogador=500
x_asteroidem=randint(0,950)
y_asteroidem=0
x_asteroideg=randint(0,900)
y_asteroideg=0
tela= pygame.display.set_mode((x_tela,y_tela))
explosão_jogador = pygame.mixer.Sound('sons/explosão jogador.ogg')
explosão=pygame.mixer.music.load('sons/explosão.ogg')
navejogador=pygame.image.load('sprites/nave.png')
asteroide_medio=pygame.image.load('sprites/asteroide medio.png')
asteroide_grande=pygame.image.load('sprites/asteroide grande.png')
img_de_explosão1=pygame.image.load('sprites/imagem explosão 3.png')
img_de_explosão2=pygame.image.load('sprites/imagem explosão 4.png')
img_de_explosão3=pygame.image.load('sprites/imagem explosão 5.png')
relogio=pygame.time.Clock()
pos_inicial_projetilx = x_navejogador + 26
pos_inicial_projetily = y_navejogador + 20
velocidade_do_projetil=0
voltarposicaox=pos_inicial_projetilx
voltarposicaoy=pos_inicial_projetily
projetil=pygame.draw.rect(tela, (255, 0, 0), (pos_inicial_projetilx, pos_inicial_projetily, 5, 10))
velocidade_do_asteroidemedio=3
velocidade_do_asteroide_grande=2
player=1
gameover = False
def game_over():
    global velocidade_do_asteroidemedio,velocidade_do_asteroide_grande,player,resultado,velocidade_do_tempo,jogardenovo,x_navejogador,y_navejogador,gameover
    x_navejogador = -200
    y_navejogador = -200
    velocidade_do_asteroidemedio=0
    velocidade_do_asteroide_grande=0
    player=0
    velocidade_do_tempo=0
    gameover = True
def reiniciar_jogo():
    global velocidade_do_asteroidemedio,velocidade_do_asteroide_grande,player,velocidade_do_tempo,t,p,x_navejogador,y_navejogador,gameover
    x_navejogador = 460
    y_navejogador = 500
    velocidade_do_asteroidemedio=3
    velocidade_do_asteroide_grande=2
    p=0
    t=0
    velocidade_do_tempo=0.03
    player=1
    gameover=False




t=0
velocidade_do_tempo=0.03
while True:
   reiniciar='aperte a tecla r para jogar de novo'
   fraseresultado=f'sua pontuação é {p} e seu tempo vivo foi de {math.ceil(t)} segundos'
   resultado=fonte.render(fraseresultado,True,(255,0,0))
   jogardenovo=fonte.render(reiniciar,True,(255,255,255))
   imagemdeexplosão=img_de_explosão1
   voltarposicaox=pos_inicial_projetilx
   pos_inicial_projetilx = x_navejogador + 26
   tela.fill((0,0,0))
   relogio.tick(30)

   t = t+velocidade_do_tempo

   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           exit()
       if event.type == KEYDOWN:
           if player== 1 and event.key == K_SPACE:
               velocidade_do_projetil =20
           if player== 0 and event.key == K_r:
               reiniciar_jogo()
   if velocidade_do_projetil==20:
       pos_inicial_projetilx=voltarposicaox

   projetil=pygame.draw.rect(tela, (255, 0, 0), (pos_inicial_projetilx, pos_inicial_projetily, 5, 10))
   if player==1 and pygame.key.get_pressed()[K_LEFT]:
       x_navejogador=x_navejogador-10
   if player==1 and pygame.key.get_pressed()[K_RIGHT]:
       x_navejogador=x_navejogador+10
   if pos_inicial_projetily <= 0:
       pos_inicial_projetily=voltarposicaoy
       velocidade_do_projetil=0
   if y_asteroidem>=600:
       y_asteroidem= 0
       x_asteroidem=randint(0,950)
   if y_asteroideg>=600:
       y_asteroideg=0
       x_asteroideg=randint(0,900)
   tela.blit(asteroide_medio,(x_asteroidem,y_asteroidem))
   tela.blit(navejogador,(x_navejogador,y_navejogador))
   tela.blit(asteroide_grande,(x_asteroideg,y_asteroideg))
   pos_inicial_projetily-=velocidade_do_projetil
   y_asteroidem+=velocidade_do_asteroidemedio
   y_asteroideg+=velocidade_do_asteroide_grande
   if pos_inicial_projetily > y_asteroideg+20 and pos_inicial_projetily<y_asteroideg+50 and pos_inicial_projetilx > x_asteroideg and pos_inicial_projetilx<x_asteroideg+56:
       pygame.mixer.music.play()
       p+=2
       b1=1
   if  pos_inicial_projetily > y_asteroidem+10 and pos_inicial_projetily < y_asteroidem+41 and  pos_inicial_projetilx > x_asteroidem and pos_inicial_projetilx < x_asteroidem + 43:
       pygame.mixer.music.play()
       b2=1
       p+=1
   if b1 == 1:
       posexplosão1x = x_asteroideg
       posexplosão1y = y_asteroideg
       b1+=1
       x_asteroideg=randint(0,900)
       y_asteroideg=-300
   if b1 > 1 and b1 <= 20:

       tela.blit(img_de_explosão1, (posexplosão1x, posexplosão1y))
       b1+=1
   if b1 > 20 and b1 <=40:
       tela.blit(img_de_explosão2, (posexplosão1x, posexplosão1y))
       b1+=1
   if b1 > 40 and b1 < 60:
       tela.blit(img_de_explosão3, (posexplosão1x, posexplosão1y))
       b1+=1
   if b1 == 60:
       b1=0

   if b2 == 1 :
      posexplosão2x = x_asteroidem
      posexplosão2y = y_asteroidem
      b2+=1
      x_asteroidem = randint(0,950)
      y_asteroidem = -300
   if b2 >= 1 and b2 <= 20:
       tela.blit(img_de_explosão1,(posexplosão2x,posexplosão2y))
       b2+=1
   if b2 > 20 and b2 <=40:
       tela.blit(img_de_explosão2,(posexplosão2x,posexplosão2y))
       b2+=1
   if b2 > 40 and b2 < 60:
       tela.blit(img_de_explosão3,(posexplosão2x,posexplosão2y))
       b2+=1
   if b2 == 60:
       b2=0
   if y_navejogador<y_asteroidem+40 and y_navejogador>y_asteroidem and x_navejogador+59>x_asteroidem and x_navejogador<x_asteroidem+43 or y_navejogador<y_asteroideg+50 and y_navejogador>y_asteroideg and x_navejogador+59>x_asteroideg and x_navejogador<x_asteroideg + 56:
       explosão_jogador.play()
       game_over()
   if gameover == True:
       tela.blit(resultado, (200, 300))
       tela.blit(jogardenovo, (250, 350))

   tempo=f'tempo:{math.ceil(t)}'
   pontuação=f'pontos: {p} '
   frase= fonte.render(pontuação,True,(255,255,255))
   segundos=fonte.render(tempo,True,(255,255,255))
   tela.blit(frase,(600,20))
   tela.blit(segundos,(750,20))
   pygame.display.update()
