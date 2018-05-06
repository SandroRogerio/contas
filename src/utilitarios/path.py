# -*- coding: utf-8 -*-
""" Modulo para gerenciar os caminhos (paths) comuns
"""


def get_path(id_path):
    return _Paths_[id_path]


# Define Path's / caminhos
_Paths_ = {}
_Paths_['Raiz'] = '/home/sandro/Dropbox/python/app_contas/'
_Paths_['Export'] = _Paths_['Raiz'] + 'export/'
_Paths_['Input'] = _Paths_['Raiz'] + 'input/'
_Paths_['Output'] = _Paths_['Raiz'] + 'output/'
_Paths_['Config'] = _Paths_['Raiz'] + 'config/'
