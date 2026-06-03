import random

def dados(lados, numero_dados):
  ''' Simula uma jogada de dados onde você especifica 3 valores: 
      lados = Numero de lados | Valor máximo do intervalo, 
      numero_dados = Quantos dados foram jogados | Quantidade de resultados
      bonus = Modificador do personagem | Soma ao total calculado'''
  i = 1
  total = 0
  while i <= numero_dados:
      rolada = random.randint(1,lados)
      total += rolada
      i += 1
  else: 
    return total 
    
class Ataques:
    def __init__(self):
        self.ataque = 10
        self.defesa = 10
        self.vida_max = 25
        self.vida_atual = 25
        self.xp = 100
        self.funcao = 0

    @property
    def ataque_fraco(self):
        ataque_fraco = self.ataque/2
        return ataque_fraco
    
    @property
    def ataque_forte(self):
        ataque_forte = self.ataque*1.5
        return ataque_forte 
    
    @property
    def classe_armadura(self):
        ca = self.ataque*1.5
        return ca 

    def funcao_aleatoria(self):
       profi = ['Guerreiro', 'Mago', 'Ladino', 'Clérigo', 'Goblin', 'Orc', 'Dragao', 'Terrasque'] 
       i = random.randint(0, 8)
       self.funcao = profi[i]

    def funcao(self):
        if  self.funcao == 'Guerreiro': 
           self.ataque = random.randint(10,20)
           self.defesa = random.randint(10,20)
        elif self.funcao == 'Mago':
           self.ataque = random.randint(20,30)
           self.defesa = random.randint(3,7)
        elif self.funcao == 'Ladino':
           self.ataque = random.randint(15,25)
        elif self.funcao == 'Clérigo':
           self.ataque = random.randint(5,15)
           self.defesa = random.randint(15,30)
        elif self.funcao == 'Goblin':
           self.ataque = random.randint(5,20)
           self.defesa = random.randint(5,15)
        elif self.funcao == 'Orc':
           self.ataque = random.randint(20,30)
           self.defesa = random.randint(10,20)
        elif self.funcao == 'Dragao':
           self.ataque = random.randint(40,70)
           self.defesa = random.randint(20,30)
        elif self.funcao == 'Tarrasque':
           self.ataque = random.randint(100,200)
           self.defesa = random.randint(30,40)
    
    def dano(self, atacante, defensor):
       acao = [self.ataqueleve, self.ataqueforte]
       i = random.radint(0,2)
       if atacante.ataque >= defensor.defesa:
        self.vida_atual = self.vida_atual - acao[i]
        return self.vida_atual
         
