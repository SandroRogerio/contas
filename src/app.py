# -*- coding: utf-8 -*-
""" Modulo principal
"""
import os
import locale

# Define a localização para correta leitura das datas
locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')


def main():
    """Função principal da aplicação.
    """

    # Identifica os arquivos a serem processados
    for Arquivo in os.listdir('dados/extrato/Input/arquivo01'):
        if Arquivo.find('OUROCARD') != -1:
            print('Trata cartão de crédito')
            quit()
        else:
            print('Tratar conta corrente!!!')

    print('FINALIZADO COM SUCESSO!!!')


if __name__ == "__main__":
    main()

