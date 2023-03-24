# Author: Gabriela Dellamora Paim
# Version: 23.03.23


# IMPORTS
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from dataclasses import dataclass


#GLOBAL VARIABLES
df = pd.read_csv('../data/treated_data.csv')

# CLASSES
# Construtor
@dataclass
class Cliente():
    '''
    Construir um objeto com os seguintes atributos
        {
        cliente:str,
        de:str,
        para:list:str,
        itens:list:str
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
    """_summary_

    Args:
        fr (str): _description_
        to (str): _description_

    Returns:
        _type_: _description_
    """
    if fr != to:
        return df[to][fr] # km
    else:
        print('Rota inválida. Tente novamente.')
        fr=input('Origem: ')
        to=input('Destino: ')
        return check_trip(fr=fr,to=to)
    
