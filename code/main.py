# Author: Gabriela Dellamora Paim
# Version: 23.03.23
from dataclasses import dataclass
import models as md
import time 

# BOAS VINDAS
print('Seja muito bem-vindo à Dely Transportadora!\n')


# DECIDINDO O NOME DA EMPRESA CLIENTE
name= input('Qual o nome da sua empresa?    ')
md.check_name(name=name)

# DECIDIR QUANTIDADE DE PRODUTOS (PESO)


    # DECIDIR ORIGEM E PARADA
        # É DESTINO FINAL? (LOOP)
            # SE SIM: QUANTIDADE_PRODUTOS=0 // FINALIZA LOOP
                # PRINT( VOCÊ VAI FAZER UMA ROTA COM ORIGEM EM ASDASD E PARADAS EM DASDSADAS, ASDSADSADAD PARA FINALIZAR EM DASDASDSADAD.)
            # SE NÃO: 
                # QUANTOS ITENS VOU DEIXAR AQUI?
                # (ORIGEM = DESTINO ANTERIOR)QUAL A PRÓXIMA PARADA?
                # QUANTIDADE_PRODUTOS = QUANTIDADE_PRODUTOS - PRODUTOS_DEIXADOS
                # É DESTINO FINAL? (LOOP)