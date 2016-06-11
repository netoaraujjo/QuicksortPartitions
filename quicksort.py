#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
from copy import copy
import time
import matplotlib.pyplot as pyplot

class Quicksort(object):
    """docstring for Quicksort"""
    def __init__(self, num_repeticoes, tamanhos):
        super(Quicksort, self).__init__()
        self.num_repeticoes = num_repeticoes
        self.tamanhos = tamanhos

        self.LOMUTO = 'lomuto'
        self.HOARE  = 'hoare'

        self.tempos_de_execucao = {}
        self.tempos_de_execucao[self.LOMUTO] = []
        self.tempos_de_execucao[self.HOARE]  = []

        self.tempos_medios = {}
        self.tempos_medios[self.LOMUTO] = []
        self.tempos_medios[self.HOARE]  = []


    def gera_arranjo(self, tamanho):
        """Inicializa os arranjos a serem ordenados."""

        # Configura o valor maximo do intervalo para o maior inteiro suportado
        # pela arquitetura do computador onde executa
        # maximo = sys.maxsize
        maximo = tamanho

        # Cria  arranjo de numeros aleatorios na quantidade especificada
        arranjo = random.sample(range(maximo), tamanho)

        return arranjo


    def executa(self):
        """"""
        for tamanho in self.tamanhos:
            print('\n#########################################################')
            print('Executando testes para arranjos de tamanho:', tamanho)
            print('#########################################################\n')
            for n in range(self.num_repeticoes):
                # Gera um novo arranjo
                arranjo_original = self.gera_arranjo(tamanho)

                # Faz uma copia do arranjo original
                arranjo = copy(arranjo_original)

                self.executa_ordenacao(copy(arranjo_original), self.LOMUTO, tamanho)

                self.executa_ordenacao(copy(arranjo_original), self.HOARE, tamanho)

            self.calcula_tempo_medio()
            print('\n\n')

        self.plotar_grafico()


    def executa_ordenacao(self, arranjo, metodo_particao, tamanho):
        """"""
        print('Ordenacao por ', metodo_particao)
        # print(arranjo)

        # Define os parametros iniciais para a execucao da ordenacao
        inicio = 0
        fim = tamanho - 1

        if metodo_particao == self.LOMUTO:
            # Obtem o tempo inicial
            tempo_inicial = time.time()

            self.quicksortLomuto(arranjo, inicio, fim)

            # Obtem o tempo final
            tempo_final = time.time()
        else:
            # Obtem o tempo inicial
            tempo_inicial = time.time()

            self.quicksortHoare(arranjo, inicio, fim)

            # Obtem o tempo final
            tempo_final = time.time()

        # Calcula o tempo de execucao
        tempo_de_execucao = (tempo_final - tempo_inicial) * 1000

        self.tempos_de_execucao[metodo_particao].append(tempo_de_execucao)

        # print(arranjo)
        print('Tempo de execucao:', tempo_de_execucao, 'milissegundos')
        print()


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


    def calcula_tempo_medio(self):
        """"""
        media = sum(self.tempos_de_execucao[self.LOMUTO]) / self.num_repeticoes
        self.tempos_medios[self.LOMUTO].append(media)

        media = sum(self.tempos_de_execucao[self.HOARE]) / self.num_repeticoes
        self.tempos_medios[self.HOARE].append(media)

        print('Tempo medio lomuto:', self.tempos_medios[self.LOMUTO])
        print('Tempo medio hoare:', self.tempos_medios[self.HOARE])


    def plotar_grafico(self):
        """"""
        eixo_x = self.tamanhos
        eixo_lomuto = self.tempos_medios[self.LOMUTO]
        eixo_hoare = self.tempos_medios[self.HOARE]

        pyplot.xlabel('Tamanho do arranjo (Nº de elementos)')
        pyplot.ylabel('Tempo de execução (ms)')

        pyplot.xlim(min(self.tamanhos), max(self.tamanhos) + 100)

        # pyplot.xticks = 10000

        pyplot.title('Ordenação com as partições de Hoare e Lomuto')

        plot1 = pyplot.plot(eixo_x, eixo_lomuto, 'ro-', label = 'Lomuto', linewidth = 2)
        plot2 = pyplot.plot(eixo_x, eixo_hoare, 'bs-', label = 'Hoare', linewidth = 2)

        pyplot.legend(loc='upper left')


        pyplot.show()

        # pyplot.savefig('grafico.png', bbox_inches = 'tight')
