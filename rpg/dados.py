import random

def dados(lados, numero_dados, bonus):
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
    total += bonus 
    return total 
    