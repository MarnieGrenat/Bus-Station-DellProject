# Author: Gabriela Dellamora Paim
# Version: 23.03.23


# IMPORTS
import numpy as np
from matplotlib import pyplot as plt
from dataclasses import dataclass
import time
import pandas as pd

##########################################################################################################################################################
#####################################################    GLOBAL VARIABLES    #############################################################################
df = pd.read_csv('../data/treated_data.csv', has_header=True, separator=';')
# Preço por KM
taxa_p= 4.87
taxa_m= 11.92
taxa_g= 27.44

##########################################################################################################################################################
##########################################################################################################################################################

#                    CLASSES
# Construtor
@dataclass
class Cliente():
    '''
    Construir um objeto com os seguintes atributos
        {
        cliente:str,
        info_viagem:list[
            {
                de:str
                itens:list
                para:str
                },
            {
                de:str
                itens:list
                para:str
                },
            ...
            ...
            ...
        ],
        peso:float.round(4),
        modalidade:int,                                # 0 = pequeno | 1 = medio | 2 = pesado 
        custo:float.round(2)
    }
'''
    _name:str
    _fr:str
    _to:list
    _itens:dict[str,int]
    _peso:float
    _mod:int                 #modalidade
    _custo:float

# Getters e Setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name:str):
        self._name=name
    
    @property
    def fr(self):
        return self._fr
    @fr.setter
    def fr(self, fr:str):
        self._fr=fr
        
    @property
    def to(self):
        return self._fr
    @to.setter
    def to(self, to:str):
        self._to=to
    
    @property
    def itens(self):
        return self._itens
    @itens.setter
    def itens(self, itens:dict):
        self._itens=itens
    
    @property
    def peso(self):
        return self._peso.round(4)
    @peso.setter
    def peso(self, peso:float):
        self._peso=peso
    
    @property
    def mod(self):
        return self._mod
    @mod.setter
    def mod(self, mod:int):
        if (mod < 0) or (mod > 2): 
            raise ValueError
        self._mod=mod
        
    @property
    def custo(self):
        return self._custo
    @custo.setter
    def custo(self, custo:float):
        self._custo=custo.round(2)
        
# FUNCTIONS
def check_trip(fr:str, to:str) -> int:  
    """Checa origem e destino

    Args:
        fr (str): _description_
        to (str): _description_

    Returns:
        _type_: int Quilometragem rodada
    """
    while fr == to:
        print('Rota inválida. Tente novamente.')
        fr=input('Origem: ')
        to=input('Destino: ')
    return df[to][fr] # quilometragem

def check_name(name:str):
    while True:
        retorno= input(f'O nome da sua empresa é {name}, certo? (S/N)')
        retorno=str(retorno.upper())
        if retorno == 'S':
            break
        if retorno == 'N':
            name= input('Qual o nome da sua empresa?    ')
        else:
            print('Não entendi sua resposta, vou refazer a pergunta, beleza?')
            time.sleep(0.7)
            
            
# 1. [Consultar trechos x modalidades]
def consult_trip():
    string=(f'\n Modalidades:\n        - Pequeno Porte:n\n            - Preço: {taxa_p}/km\n            - Peso Máximo: 1 Tonelada\n        - Médio Porte:\n            - Preço: {taxa_m}/km\n            - Peso Máximo: 4 Toneladas\n        - Grande Porte:\n            - Preço: {taxa_g}/km\n            - Peso Máximo: 11 Toneladas     \nORIGENS E DESTINOS:\n        {list(df.columns[1:])}')
    return string
# 2. [Cadastrar transporte]

# 3. [Dados estatísticos]

# 4. [Finalizar o programa]

# TESTES:
