# -*- coding: utf-8 -*-
""" Gerencia os caminhos (paths) comuns, com base na localização da aplicação
    Trabalha com os seguintes 'id':
        Raiz
        Export
        Input
        Output
        Config
"""

import os


def get_path(id_path):
    """ Retorna o path referente ao 'id' informado
    """
    return _Paths_[id_path]


# Define Path's / caminhos a partir da localização atual
_Paths_ = {}
_Paths_['Raiz'] = os.getcwd().replace('/src', '/')
_Paths_['Export'] = _Paths_['Raiz'] + 'export/'
_Paths_['Input'] = _Paths_['Raiz'] + 'input/'
_Paths_['Output'] = _Paths_['Raiz'] + 'output/'
_Paths_['Config'] = _Paths_['Raiz'] + 'config/'
