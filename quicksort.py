#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
from copy import copy

class Quicksort(object):
    """docstring for Quicksort"""
    def __init__(self, tamanho):
        super(Quicksort, self).__init__()

        self.inicializar_arranjo(tamanho)



    def inicializar_arranjo(self, tamanho):
        """Inicializa os arranjos a serem ordenados."""

        print("Criando arranjo de tamanho %s." % tamanho)

        # Configura o valor maximo do intervalo para o maior inteiro suportado
        # pela arquitetura do computador onde executa
        # maximo = sys.maxsize
        maximo = 10

        # Cria  arranjo de numeros aleatorios na quantidade especificada
        self.arranjo = random.sample(range(maximo), tamanho)

        print("Arranjo criado.")

        print(self.arranjo)

        self.executa()


    def executa(self):
        # Faz uma copia do arranjo para preservar o original
        arranjo = copy(self.arranjo)
        inicio = 0
        fim = len(arranjo) - 1
        self.quicksortLomuto(arranjo, inicio, fim)
        print(arranjo)


    def quicksortHoare(self, arranjo, inicio, fim):
        """Executa a ordenacao utilizando o particionamento de Hoare."""
        j = 0
        if inicio < fim:
            j = self.particionamentoHoare(arranjo, inicio, fim)
            self.quicksortHoare(arranjo, inicio, j - 1)
            self.quicksortHoare(arranjo, j + 1, fim)


    def quicksortLomuto(self, arranjo, inicio, fim):
        """Executa a ordenacao utilizando o particionamento de Lomuto."""
        j = 0
        if inicio < fim:
            j = self.particionamentoLomuto(arranjo, inicio, fim)
            self.quicksortLomuto(arranjo, inicio, j - 1)
            self.quicksortLomuto(arranjo, j + 1, fim)


    def particionamentoHoare(self, arranjo, inicio, fim):
        """Particiona o arranjo utilizando o metodo de Hoare."""
        pivo = arranjo[inicio]
        i = inicio + 1
        j = fim
        while True:
            while i <= fim and arranjo[i] <= pivo:
                i += 1
            while pivo < arranjo[j]:
                j -= 1
            if i >= j:
                break
            temp = arranjo[i]
            arranjo[i] = arranjo[j]
            arranjo[j] = temp

        arranjo[inicio] = arranjo[j]
        arranjo[j] = pivo
        return j


    def particionamentoLomuto(self, arranjo, inicio, fim):
        """Particiona o arranjo utilizando o metodo de Lomuto."""
        pivo = arranjo[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            if arranjo[j] <= pivo:
                i += 1
                temp = arranjo[i]
                arranjo[i] = arranjo[j]
                arranjo[j] = temp
        temp = arranjo[i + 1]
        arranjo[i + 1] = arranjo[fim]
        arranjo[fim] = temp
        return i + 1
