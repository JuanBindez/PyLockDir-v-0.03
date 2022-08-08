'''
Copyright (c) 2022 Juan Carlos Bindez

This project is licensed under the MIT License.
'''

'''
Author: www.github.com/JuanBindez
Description: change file and directory permissions
Python Version: 3.10
Local: Brazil
OS: Linux
'''


class Color():
    VERDE = '\033[92m'
    VERDE_CLARO = '\033[1;92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    NEGRITO = '\033[;1m'
    CYANO = '\033[1;36m'
    CYANO_CLARO = '\033[1;96m'
    CINZA_CLARO = '\033[1;37m'
    CINZA_ESCURO = '\033[1;90m'
    PRETO = '\033[1;30m'
    BRANCO = '\033[1;97m'
    INVERTE = '\033[;7m'
    RESET = '\033[0m'

        
def header_menu():
    print(Color.VERMELHO +
        '''
                             ____        _               _    ____  _      
                            |  _   _   _| |    ___   ___| | _|  _  (_)_ __ 
                            | |_) | | | | |   / _ \ / __| |/ / | | | | '__|
                            |  __/| |_| | |__| (_) | (__|   <| |_| | | |   
                            |_|     __, |_____ ___/  ___|_| _ ____/|_|_|    v 0.03
                                   |___/ Copyright (c) 2022 Juan Carlos Bindez                     
        
                               [ Ctrl + C ]  Para Encerrar o Programa

        '''
    + Color.RESET)


def header_choices():
    print(Color.BRANCO +

        '''

                            [1]  ---------  000        [6]  rw-rw-rw-  666
                            [2]  r--------  400        [7]  rwx------  700
                            [3]  r--r--r--  444        [8]  rwxr-x---  750
                            [4]  rw-------  600        [9]  rwxr-xr-x  755
                            [5]  rw-r--r--  644        [10] rwxrwxrwx  777
                            
                                            [11] Pendrive
        
        
        '''
    + Color.RESET)
