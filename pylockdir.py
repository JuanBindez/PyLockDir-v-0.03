

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