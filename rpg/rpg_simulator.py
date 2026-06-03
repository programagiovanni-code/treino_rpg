import random
import time
import roll_dice as dado


class Personagens:
    def __init__(self):
      '''Classe de seres vivos e suas habilidades como, ataque, defesa, vida_max, vida_atual, xp, função'''
      self.ataque = 10
      self.defesa = 10
      self.vida_atual = 35
      self.vida_max = 35
      self.funcao_aleatoria()


    def funcao_aleatoria(self):
      profi = ['Guerreiro', 'Mago', 'Ladino', 'Clérigo', 'Goblin', 'Orc']
      funcao_velha = random.choice(profi)
      self.funcao = funcao_velha
      if self.funcao == 'Guerreiro':
        self.ataque = random.randint(10,20) + dado.dados(6,1)
        self.defesa = random.randint(10,20) + dado.dados(6,1)
      elif self.funcao == 'Mago':
        self.ataque = random.randint(20,30) + dado.dados(12,1)
        self.defesa = random.randint(3,7) + dado.dados(4,1)
      elif self.funcao == 'Ladino':
        self.ataque = random.randint(15,25) + dado.dados(20,1)
      elif self.funcao == 'Clérigo':
        self.ataque = random.randint(5,15)
        self.defesa = random.randint(15,30) + dado.dados(20,1)
      elif self.funcao == 'Goblin':
        self.ataque = random.randint(5,20)
        self.defesa = random.randint(5,15)
      elif self.funcao == 'Orc':
        self.ataque = random.randint(20,30)
        self.defesa = random.randint(10,20) + dado.dados(6,1)
      return funcao_velha

#===================================================================
#- Ataque x CA -----------------------------------------------------
    def ataque_total (self, defensor):
      ataque = (self.ataque + dado.dados(20,1)) - defensor.defesa
      return ataque

    def defesa_total (self, defensor):
      defesa = (defensor.defesa + dado.dados(20,1)) - self.defesa
      return defesa
    
#- Dano ------------------------------------------------------------
    @property
    def dano_ataque(self):
      ataque_fraco = int(self.ataque * random.random())
      ataque_forte = int(self.ataque*random.randint(1,2))
      ataque = [ataque_forte, ataque_fraco]
      return random.choice(ataque)
    
#- Ajuste de vida --------------------------------------------------
    def loss_hp(self, ataque):
      self.vida_atual = self.vida_atual - ataque
      return self.vida_atual

#===================================================================
# --- Mecanica de combate ------------------------------------------
    def round(self):
      print(40*'=')
      print(f'Seu atacante surge, ele é um {self.funcao}')
      print(f'Ataque {self.ataque} | Defesa {self.defesa}  |  Vida {self.vida_atual}')    
      print(40*'='); time.sleep(2) 

      while self.vida_atual > 0:
        defensor = Personagens()
        print(f'Um novo defensor surge, ele é um {defensor.funcao}')
        print(f'Ataque {defensor.ataque} | Defesa {defensor.defesa}  |  Vida {defensor.vida_atual}')
        print(40*'='); time.sleep(2)

        while defensor.vida_atual > 0:
          ataque_atack = self.dano_ataque
          ataque_def = defensor.dano_ataque

          if self.vida_atual <= 0: break

          elif self.ataque_total(defensor) >= 0 and self.defesa_total(defensor) >= 0:
            print('----------=== Nova rodada ===-----------')
            print(40*'-')
            print(f'Vida do Atacante: {self.vida_atual}     |     Vida do Defensor: {defensor.vida_atual}')
            print(40*'-'); time.sleep(2)

            self.loss_hp(ataque_def)       
            defensor.loss_hp(ataque_atack) 

            print('Os guerreiros cruzam a espada violentamente e ambos se ferem!'); time.sleep(1)
            print(f'O Defensor {defensor.funcao} tomou {ataque_atack:.0f} de dano e está com {defensor.vida_atual:.0f} pontos de vida!')
            print(f'O Atacante {self.funcao} tomou {ataque_def:.0f} de dano e está com {self.vida_atual:.0f} pontos de vida')
            print(40*'-'); time.sleep(4)

          elif self.ataque_total(defensor) >= 0:
            print('----------=== Nova rodada ===-----------')
            print(40*'-')
            print(f'Vida do Atacante: {self.vida_atual}     |     Vida do Defensor: {defensor.vida_atual}')
            print(40*'-'); time.sleep(2)

            defensor.loss_hp(ataque_atack) 

            print('O Atacante se esquiva e desfere um golpe certeiro'); time.sleep(1)
            print(f'O Atacante {self.funcao} causou {ataque_atack:.0f} de dano ao Defensor {defensor.funcao} deixando ele com {defensor.vida_atual:.0f} pontos de vida!')
            print(40*'-'); time.sleep(3)

          elif self.defesa_total (defensor) >= 0:
            print('----------=== Nova rodada ===-----------')
            print(40*'-')
            print(f'Vida do Atacante: {self.vida_atual}     |     Vida do Defensor: {defensor.vida_atual}')
            print(40*'-'); time.sleep(2)

            self.loss_hp(ataque_def) 

            print('O defensor se esquiva e desfere um golpe certeiro'); time.sleep(1)
            print(f'O Defensor {defensor.funcao} causou {ataque_def:.0f} de dano ao Atacante {self.funcao} deixando ele com {self.vida_atual:.0f} pontos de vida!') 
            print(40*'-'); time.sleep(3)

          elif (self.ataque_total(defensor) < 0) and (self.defesa_total(defensor) < 0):
            print('----------=== Nova rodada ===-----------')
            print(40*'-')
            print(f'Vida do Atacante: {self.vida_atual}     |     Vida do Defensor: {defensor.vida_atual}')
            print(40*'-'); time.sleep(2)
            print('Os guerreiros cruzam a espada mas ninguem se fere.')
            print(40*'-'); time.sleep(1)

          else:
            defensor = Personagens()
                
        else: 
          print(40*'=')
          print(f'O Defensor {defensor.funcao} morreu')
          print(40*'='); time.sleep(1)

#===================================================================
# --- Loop de combate ----------------------------------------------

    def loop(self):
      print('  ===xx    INICIO DE JOGO!!    xx===')
      print('=====xx -------------------- xx=====')
      i = 0
      while True:
        self.vida_atual = self.vida_max
        nova_funcao = self.funcao_aleatoria()
        self.funcao = nova_funcao
        continuar = ['S','s','sim','Sim', 'SIM', 'Quero']
        again = input('Deseja iniciar o jogo? (S / N): ')
        if again in continuar:
          while self.vida_atual > 0:
            self.round()
          else: 
            print(40*'x')
            print('===xx    O ATACANTE MORREU!!    xx===')
            print(40*'-')
        else: break
      else:
          print(40*'-')
          print(' ===xx        FIM DE JOGO       xx===')
          print(40*'x')

pedro = Personagens()
pedro.loop()