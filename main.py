# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from graph import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        #print(numeros)
        c = 0
        for _id in range(g.n):
            i = numeros[_id]
            g.M[l][c] = int(i)
            if(g.M[l][c] > 0):
                g.L[l].append(c)
            
            c += 1
        l += 1
    return g

gr = load_from("pcv177.txt")
print(gr.M)
print(gr.L)
gr.dfs()
print("Numero de Componentes Conexas: " + str(gr.num_componentes_conexas()))


