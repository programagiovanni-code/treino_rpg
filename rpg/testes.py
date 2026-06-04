from utilidade.roll_dice import dados
from utilidade.modificador_atributos import tabela_modificadora_atributos as tabela_mod

atributos = {'Força' : 20,
                    'Destreza' : 10,
                    'Constituição' : 5,
                    'Inteligencia' : 11}

#---------------------------------------------------
modificadores = {'Modificador de Força' : 0, 
                        'Modificador de Destreza' : 0,
                        'Modificador de Constituição' : 0,
                        'Modificador de Inteligência' : 0}

def modificadores_atributos_efetora():
        for atributo1, valores in atributos.items():
            for atributo2, modificador in modificadores.items():
                atualizacao = tabela_mod(valores)
                print(atualizacao)
                if atributo1 == 'Força':
                    if atributo2 == 'Modificador de Força':
                        modificadores[atributo2] += atualizacao
                        print('Modificador atualizado - Força')
                elif atributo1 == 'Destreza':
                    if atributo2 == 'Modificador de Destreza':
                        modificadores[atributo2] += atualizacao
                        print('Modificador atualizado - Destreza')
                elif atributo1 == 'Constituição':
                    if atributo2 == 'Modificador de Constituição':
                        modificadores[atributo2] += atualizacao
                        print('Modificador atualizado - Constituição')
                elif atributo1 == 'Inteligência':
                    if atributo2 == 'Modificador de Inteligência':
                        modificadores[atributo2] += atualizacao
                        print('Modificador atualizado - Inteligência')

modificadores_atributos_efetora()
print(modificadores)
