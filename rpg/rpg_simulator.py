class Personagens:
    def __init__(self):
      '''Classe de seres vivos e suas habilidades como, ataque, defesa, vida_max, vida_atual, xp, função'''
      self.ataque = 10
      self.defesa = 10
      self.vida_atual = 25
      self.funcao_aleatoria()

    def funcao_aleatoria(self):
      profi = ['Guerreiro', 'Mago', 'Ladino', 'Clérigo', 'Goblin', 'Orc']
      self.funcao = random.choice(profi)
      if self.funcao == 'Guerreiro':
        self.ataque = random.randint(10,20) + dados(6,1)
        self.defesa = random.randint(10,20) + dados(6,1)
      elif self.funcao == 'Mago':
        self.ataque = random.randint(20,30) + dados(12,1)
        self.defesa = random.randint(3,7) + dados(4,1)
      elif self.funcao == 'Ladino':
        self.ataque = random.randint(15,25) + dados(20,1)
      elif self.funcao == 'Clérigo':
        self.ataque = random.randint(5,15)
        self.defesa = random.randint(15,30) + dados(20,1)
      elif self.funcao == 'Goblin':
        self.ataque = random.randint(5,20)
        self.defesa = random.randint(5,15)
      elif self.funcao == 'Orc':
        self.ataque = random.randint(20,30)
        self.defesa = random.randint(10,20) + dados(6,1)

#===================================================================
#- Ataque x CA -----------------------------------------------------
    def ataque_total (self, defensor):
      ataque = (self.ataque + dados(20,1)) - defensor.defesa
      return ataque

    def defesa_total (self, defensor):
      defesa = (defensor.defesa + dados(20,1)) - self.defesa
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
      while self.vida_atual > 0:
        defensor = Personagens()
        print(40*'=')
        print(f'Um novo atacante surge, ele é um {defensor.funcao}')
        print(f'Ataque {defensor.ataque} | Defesa {defensor.defesa}  |  Vida {defensor.vida_atual}')
        print(40*'=')

        while defensor.vida_atual > 0:
          ataque_atack = self.dano_ataque
          ataque_def = defensor.dano_ataque
          print('---=== Nova rodada ===---')

          if self.vida_atual <= 0: break
          
          elif self.ataque_total(defensor) >= 0 and self.defesa_total(defensor) >= 0:
            print('Os guerreiros cruzam a espada violentamente e ambos se ferem!')
            self.loss_hp(ataque_def)
            defensor.loss_hp(ataque_atack)
            print(f'O Defensor tomou {ataque_atack:.0f} de dano e está com {defensor.vida_atual:.0f} pontos de vida!')
            print(f'O Atacante tomou {ataque_def:.0f} de dano e está com {self.vida_atual:.0f} pontos de vida')
            print(40*'-')

          elif self.ataque_total(defensor) >= 0:
            defensor.loss_hp(self.dano_ataque)
            print('O Atacante se esquiva')
            print(f'Um golpe certeiro do Atacante {self.funcao} causando {ataque_atack:.0f} de dano, agora o Defensor {defensor.funcao} esta com {defensor.vida_atual:.0f} pontos de vida!')
            print(40*'-')

          elif self.defesa_total (defensor) >= 0:
            self.loss_hp(defensor.dano_ataque)
            print('O defensor se esquiva')
            print(f'Um golpe certeiro do Defensor {defensor.funcao} causando {ataque_def:.0f} de dano, agora o Atacante {self.funcao} esta com {self.vida_atual:.0f} pontos de vida!')
            print(40*'-')

          elif (self.ataque_total(defensor) < 0) and (self.defesa_total(defensor) < 0):
            print('Os guerreiros cruzam a espada mas ninguem se fere.')
            print(40*'-')

          else:
            defensor = Personagens()

#===================================================================
# --- Loop de combate ----------------------------------------------
    def loop(self):
      print('===xx    INICIO DE JOGO!!    xx===')
      print(' ===xx -------------------- xx===')
      while self.vida_atual > 0:
        self.round()
      else:
        print('===xx    O Atacante morreu!!    xx===')
        print(' ===xx        FIM DE JOGO      xx===')
