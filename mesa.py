# -*- coding: utf8 -*-
from FGAme import *
from random import uniform, randint

import taco, buraco


gravity=0
friction=0.5
restitution=0.95
num_balls=15
speed=200
radius=10


# Inicializa a mesa com as bolas

class Mesa(World):

    def __init__(self):
        super(Mesa, self).__init__(gravity=gravity, dfriction=friction,
                                  restitution=restitution, background = (0,146,64))

        
        # Buracos da mesa
        pos_buracos = [(30, 495), (770, 495), (400, 495), (400, 100),(30, 100), (770, 100)]
        self.listaBuracos = []

        for pos in pos_buracos:
            buraco = Circle(radius=25, vel=Vec2(0, 0), pos=Vec2(pos), mass='inf',color=(30,30,30), col_layer=2)
            self.add(buraco)
            
            centroBuraco = Circle(radius=10, pos=pos, mass='inf', color='blue')
            self.listaBuracos.append(centroBuraco)
            self.add(centroBuraco)
            centroBuraco.listen('collision', self.bola_no_buraco)
        
        # Limites da mesa (740 x 395)
        #   xi, xf, yi, yf 
        AABB(0, 800, 495, 800, world=self, mass='inf')  # Cima
        AABB(0, 30, 30, 800, world=self, mass='inf')   # Esquerda
        AABB(770, 800, 30, 800, world=self, mass='inf') # Direita
        AABB(0, 800, 0, 100, world=self, mass='inf')     # Baixo

        # Inicia bolas
      
        # Vetor de posição das bolas        
        posX = 200
        posY = 297.5
        pos_bolas = [(posX,posY), (posX-20,posY-10), (posX-20,posY+10), (posX-40, posY-20), 
                    (posX-40, posY), (posX-40, posY+20), (posX-60, posY-30), (posX-60, posY-10),
                    (posX-60,posY+10), (posX-60, posY+30), (posX-80, posY-40), (posX-80, posY-20),
                    (posX-80, posY), (posX-80, posY+20), (posX-80, posY+40)]
    
        # Vetor de cores das bolas
        cor_bolas = [(255,255,0), (0,0,255), (255,0,0), (128,0,128), (255,20,147), (0,128,0), (244,164,96), (0,0,0),
                        (255,215,0), (0,0,205), (139,0,0), (34,139,34), (255,105,180), (138,43,226), (188,143,143)]
        # Na ordem: amarela, azul, vermelha, violeta, rosa, verde, bege, preta, 
        #           amarela, azul, vermelha, verde, rosa, violeta, bege
        
        #Cria as bolas e as associa com as posições e as cores:

        for x in range (num_balls):
            bola = Circle(radius=radius, mass=1)
            bola.pos = pos_bolas[x]
            bola.color = cor_bolas[x]
            bola.numero = x
            self.add(bola)

        # Define bola branca
        pos = (600, 100 + 395/2)
        self.bolao = Circle(radius=1.5*radius, vel=(-300, 0), pos=pos, mass=2)
        self.bolao.color = (255,255,255)
        self.add(self.bolao)

    @listen("frame-enter")
    def aplica_colisoes(self):
        pass
    
    @listen('key-down', 'return')
    def toggle_pause(self):
        super(Mesa, self).toggle_pause()

    # Teste de tacada
    @listen('key-down', 'up', 200 )
    def tacadau(self, impulso):
        direcao = Vec2(0,1)
        self.bolao.boost(direcao*impulso)

    @listen('key-down', 'down', 200 )
    def tacadad(self, impulso):
        direcao = Vec2(0,-1)
        self.bolao.boost(direcao*impulso)

    @listen('key-down', 'left', 200 )
    def tacadal(self, impulso):
        direcao = Vec2(-1,0)
        self.bolao.boost(direcao*impulso)

    @listen('key-down', 'right', 200 )
    def tacadar(self, impulso):
        direcao = Vec2(1,0)
        self.bolao.boost(direcao*impulso)

    #@listen('collision')
    def bola_no_buraco(self, col):
        self.remove(col.objects[1])
        print(col.objects)

        # Inicia o jogo
if __name__ == '__main__':
    game = Mesa()
    game.run()
