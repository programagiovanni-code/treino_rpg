def tabela_modificadora_atributos(atributo): # Interno
    '''Tabela que converte valores de atributos em modificadores de habilidades estilo D&D'''
    valor_atributo = range(1,31)
    mod_inicial = -5
    dict_mod = {}
    for valor in valor_atributo:
        if valor % 2 == 0:
            mod_inicial += 1
        dict_mod[valor] = mod_inicial
    if atributo <= 30:
        return dict_mod[atributo]


#tabela_modificadora_atributos(30)

