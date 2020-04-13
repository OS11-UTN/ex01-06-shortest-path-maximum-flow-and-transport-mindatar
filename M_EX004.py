import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na, get_usage_string, get_min_cut, get_selected_arcs

# IMPORT THE DATA: ( 13 de Abril de 2020 )
# Marco Inda.
# Para este ejercicio , modificamos un arco : t-->s , que sería el que balancea las cargas.
# se considera como un flujo de capacidad infinita , para saber el flujo máximo sobre la red.
# este problema es de FMC Flujo de Minimo Costo.
NN = np.array([[0, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0]])

# DATA MANIPULATION:
Aeq, arc_idxs = nn2na(NN)
# Cambia el vector de Costos , 0 fluye excepto en t, 8 arcos , se suma uno más. 1x8
C = np.array([0,0,0,0, 0,0,0,-1])
# Vector B todo 0 , ojo con los vertices.
beq = np.array([0, 0, 0, 0, 0, 0 ])
# Los limites superiores son las capacidades máximas por cada arco.
# ojo con el orden , idem a la Matriz NA.

max_q = [7,1,2,3,2,1,2,None]
bounds = tuple([(0, 7),(0,1),(0,2),(0,3),(0,2),(0,1),(0,2),(0,None)])

print('## Optimizer inputs ## \n'
      'Cost vector: %s \n '
      'A_eq Node-Arc matrix:\n%s \n'
      'b_eq demand-supply vector: %s \n'
      'Bounds of each X arc variable: %s \n' % (C, Aeq, beq, bounds))

# OPTIMIZE:
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method='simplex' )

# GET THE SOLUTION:
usage = get_usage_string(arc_idxs, res.x.astype(int),max_q)
min_cut = get_min_cut(arc_idxs,res.x ,np.array(max_q))
max_flow = -1*res.fun
selarcs = get_selected_arcs(arc_idxs,res.x )

print('## REsultados ## \n'
      'Uso de cada arco : %s \n '
      'Los arcos que producen el minimo cortes: %s \n'
      'Maximo Flujo: %0.2f \n' % (usage,min_cut, max_flow))
