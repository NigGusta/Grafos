# -*- coding: utf-8 -*-
import queue

BRANCO = 0
CINZA = 1
PRETO = 2

class Graph:
    def __init__(self, n):
        self.n = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [[] for _ in range(n)]
        
        self.pai = [None for _ in range(n)]
        self.d = [-1 for _ in range(n)]
        self.cor = [BRANCO for _ in range(self.n)]

    def num_componentes_conexas(self):
        n_comp = 0
        for p in self.pai:
            if p == None:
                n_comp += 1
        return n_comp

    

    def bfs(self, source):
        self.cor[source] = CINZA
        self.d[source] = 0
        Q = queue.Queue()
        Q.put(source)
        
        while (Q.empty() == False) :
            u = Q.get()
            for v in self.L[u]:
                if self.cor[v] == BRANCO :
                    self.cor[v] = CINZA
                    self.d[v] = self.d[u] + 1
                    self.pai[v]  = u
                    Q.put(v)
            self.cor[u] = PRETO
        
        print(self.d)
        print(self.pai)
        
        def imprimir_caminho_bfs(self, s, t):
            if s == t:
                print(s)
                return
    
            self.bfs(s)
    
            if self.pai[t] is None:
             print("Não há caminho entre os vértices")
             return
    
            caminho = []
            atual = t
            while atual != s:
                caminho.append(atual)
                atual = self.pai[atual]
                caminho.append(s)
    
            caminho.reverse()
            print("Caminho:", caminho)
        
        
    def dfs(self):
        for u in range(self.n):
            if self.cor[u] == BRANCO:
                self.dfs_visit(u)                

    def dfs_iterative(self, origem):
        self.cor[origem] = CINZA
        self.pai[origem] = None
    
        pilha = [origem]
    
        while pilha:
            u = pilha[-1]
            tem_vizinho_nao_visitado = False
        
        for v in self.L[u]:
            if self.cor[v] == BRANCO:
                self.cor[v] = CINZA
                self.pai[v] = u
                pilha.append(v)
                tem_vizinho_nao_visitado = True
                break
        
        if not tem_vizinho_nao_visitado:
            pilha.pop()
            self.cor[u] = PRETO
                
