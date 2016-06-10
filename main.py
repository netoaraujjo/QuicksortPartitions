#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MODO DE EXECUCAO
# python3 main.py tamanho_do_arranjo

from quicksort import *
import sys

def main(tamanho):
    qs = Quicksort(tamanho)


if __name__ == '__main__':
    tamanho = int(sys.argv[1])
    main(tamanho)
