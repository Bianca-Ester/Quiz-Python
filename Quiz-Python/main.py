import os

from q_biblico import quiz_biblico
from q_rita_lee import quiz_rita_lee
from q_versace import quiz_versace

def menu_inicial():
    controlador = True

    while controlador:
        limpar_terminal() 
        print("========================================")
        print("|     SEJA BEM-VINDO AO MULTI QUIZ     |")
        print("========================================")

        print("\nMe diz, qual quiz você quer jogar?\n")
        
        print("================ OPÇÕES ================")
        print("1) QUIZ SOBRE A RITA LEE")
        print("2) QUIZ BÍBLICO")
        print("3) QUIZ SOBRE A VERSACE")
        print("________________________________________")
        print("|PARA SAIR, DIGITE QUALQUER OUTRA TECLA|")
        print("========================================")
    
        quiz = input("Digite uma opção: ")

        if quiz == "1":
            limpar_terminal()
            quiz_rita_lee()
        elif quiz == "2":
            limpar_terminal()
            quiz_biblico()
        elif quiz == "3":
            limpar_terminal()
            quiz_versace()
        elif quiz != "1" or quiz != "2" or quiz != "3":
            print("Isso é um adeus? 🤧")
            controlador = False

def limpar_terminal():
    os.system('cls')

menu_inicial()
