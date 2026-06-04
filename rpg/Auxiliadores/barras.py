def linha(texto, tipo):
    '''Imprime barras para o terminal com ou sem texto, possue dois parametros:
        texto - introduza o texto para o titulo
       ----> Se 0 ou False é por não ter texto, se não coloque o texto
        tipo - 'arrow', 'triangle','maori', else
       ----> Define o desenho da barra.'''

    
    if texto == 0:
        if tipo == 'arrow':
            print('»»'+ 61*'—'+'⇌••⇋'+ 61*'—'+'««')
        elif tipo == 'triangle':
            print(65*'◈━')
        elif tipo == 'maori':
            print(65*'₪₪')
        else:
            print(65*'▄▀')

    else:
        if tipo == 'arrow':
            print(f'»»{56*'—'}⇌•| {texto} |•⇋{56*'—'}««')
        elif tipo == 'triangle':
            print(f'{30*'◈━'}| {texto} |{30*'◈━'}')
        elif tipo == 'maori':
            print(f'{30*'₪₪'}| {texto} |{30*'₪₪'}')
        else:
            print(f'{30*'▄▀'}| {texto} |{30*'▄▀'}')       

def charge(valor):
    '''Imprime uma barra de carregamento possuindo apenas um parametro:
        valor - 0 a 100'''
    try:
        valor = int(valor)

        if valor < 0 or valor > 100:
            print('Erro: Insira um valor de 0 a 100')
            return
        
        blocos_cheios = valor // 5
        blocos_vazios = 20 - blocos_cheios

        barra = ('■' * blocos_cheios) + ('□' * blocos_vazios)
        
        print(f'[{barra}] {valor}%')

    except ValueError:
        print('Erro: Você precisa digitar um número válido!')

def box(texto):
    '''Imprime um texto dentro de uma caixa, possum parametro
        texto - Insira seu texto'''
    tamanho = len(texto) + 2
    print('╔' + ('═' * tamanho) + '╗')
    print(f'║ {texto} ║')
    print('╚' + ('═' * tamanho) + '╝')

######   TESTES    #######################################################  
# Testes sem texto
#linha('arrow',0); linha('triangle',0); linha('maori',0); linha('chegada',0)

#Testes com texto
#linha('arrow','Teste'); linha('triangle','Teste'): linha('maori','Teste'); linha('chegada','Teste')

#Testes Carregamento
#charge(79)

#Teste Box
#box('Teste')
