import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na, get_usage_string, get_min_cut, get_selected_arcs

# IMPORT THE DATA:
# Marco Inda
# Usando algoritmo ShortPath , resolver problema de Transportes
NN = np.array([[0, 0, 0, 1, 1],
               [0, 0, 0, 1, 1],
               [0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])

# DATA MANIPULATION:
Aeq, arc_idxs = nn2na(NN)
# Vector de Costos , son los valores de los arcos.
# En este caso los Xij son cantidades a transportar por cada unidad tiene un Costo Cij
C = np.array([10, 20, 10, 10,10, 30])
# El vector Bi , son las restricciones tanto de Generación como de Demanda con su propio signo.
beq = np.array([10, 20, 15, -25, -20])
# limites por low seria cero , y por upper , sería NOne , ya que queremos ver cuales son la cantidades que hacen
# cumplir la Demanda a un costo mínimo.
bounds = tuple([(0, None),(0, None),(0, None),(0, None),(0, None),(0, None) ])

print('## Optimizer inputs ## \n'
      'Cost vector: %s \n '
      'A_eq Node-Arc matrix:\n%s \n'
      'b_eq demand-supply vector: %s \n'
      'Bounds of each X arc variable: %s \n' % (C, Aeq, beq, bounds))

# OPTIMIZE:
name_method_01 = 'simplex'
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method = name_method_01 )

# GET THE SOLUTION:
selarcs = get_selected_arcs(arc_idxs,res.x )

print('\n ## Results %s ## ' % name_method_01 )
print ('The row solution  will be : %s ' % res.x)
print ('The arcs that make the shortest path will be (from , to ) : %s ' % selarcs)
print ('The maximum cost will be : %0.2f ' % res.fun )

# Por último no tiene un Arco de paso más corto , por que no tiene un origen comun y un destino
#el problema es de Asignación./ Transporte.
# Osea los arcos que uso son : 1-->4 con costo 10
# Arco de 2-->5 costo 10( 20 u. ) , arco de 3-->4 costo 10 ( 15 unidades ).
