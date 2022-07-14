'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: www.github.com/JuanBindez
License: https://github.com/JuanBindez/PyLockDir/blob/main/LICENSE
Description: change file and directory permissions
Python Version: 3.10
year: 2022
Local: Brazil
OS: Linux

'''

from files import header
import os
import time


try:
    def chmod_a(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_b(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_c(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_d(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_e(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_f(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_g(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_h(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_i(caminho):
        os.system("sudo chmod 000 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def chmod_j(caminho):
        os.system("sudo chmod 777 -v {}".format(caminho))
        time.sleep(3)
        menu()


    def menu():
        header.header_menu()
        header.header_choices()

        escolha = int(input("{} >>".format(name_file)))

        match escolha:
            case 1:
                chmod_a(name_file)

            case 2:
                chmod_b(name_file)

            case 3:
                chmod_c(name_file)

            case 4:
                chmod_d(name_file)

            case 5:
                chmod_e(name_file)

            case 6:
                chmod_f(name_file)

            case 7:
                chmod_g(name_file)

            case 8:
                chmod_h(name_file)

            case 9:
                chmod_i(name_file)

            case 10:
                chmod_j(name_file)

            case _:
                print("                             Digite Apenas os Números Listados!")
                menu()
        

    header.header_menu()
    name_file = str(input("                           Digite o Nome Do Arquivo ou o Caminho Do Diretório\n>"))
    os.system("clear")
    menu()



except KeyboardInterrupt:
    os.system("clear")
    header.header_menu()
    print("Obrigado Por Usar o PyLockDir!")
