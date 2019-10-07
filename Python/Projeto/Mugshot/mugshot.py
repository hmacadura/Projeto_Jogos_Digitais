import pygame
import sys

sys.path.insert(1, '..\Selecao')

import selecaoEmFuncao

opcaoPersonagem = selecaoEmFuncao.seleciona.selecaoPersonagem()
if opcaoPersonagem == 1:
    print("HERÓI")
elif opcaoPersonagem == 2:
    print("Cavaleiro")
elif opcaoPersonagem == 3:
    print("Feiticeira")
elif opcaoPersonagem == 4:
    print("Mago")
elif opcaoPersonagem == 5:
    print("Princesa")
    
