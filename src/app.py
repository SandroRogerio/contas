# -*- coding: utf-8 -*-
""" Modulo principal
"""
import os
import locale
from utilitarios import path

# Define a localização para correta leitura das datas
locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')


def main():
    """Função principal da aplicação.
    """

    print('DIRETORIO DE CONFIGURAÇÃO=[' +
          path.get_path('Config') +
          ']')
    # Identifica os arquivos a serem processados
    for Arquivo in os.listdir(path.get_path('Input')):
        if Arquivo.find('OUROCARD') != -1:
            print('Trata cartão de crédito')
            quit()
        else:
            print('Tratar conta corrente!!!')

    print('FINALIZADO COM SUCESSO!!!')


if __name__ == "__main__":
    main()
