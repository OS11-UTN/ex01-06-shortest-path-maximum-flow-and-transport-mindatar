class Grafo:

    ''' Para armar el algoritmo de FordFulkerson nos basamos en recibir como parámetros
     una Matriz de Adyacencia , con los "pesos" en los lugares donde va 1
     ej. si el Nodo 1 tiene un Arco al Noto 2 , A[1,2] = 1 , pero nosotros vamos a colocar en vez de 1
        el peso del arco. osea A[1,2] = 5 ej. 5 seria el peso/distancia/ capacidad máxima entre nodo 1 y 2.'''

    def __init__(self,grafo):
        self.grafo = grafo # Grafo residual
        self.fila =len(grafo)

    ''' La funcion encontrarCamino , no es nada más que el algorito de DSF Depth First Search
    que nos dice que encontro un camino desde "s" a "t" , y nos devulve un Vector Padre
        que tiene el cámino recorrido '''

    def encontrarCamino(self,s,t,padre):

        # Visitado es un vector para llevar la cuenta de todos los nodos procesados.
        visitado = [False]*(self.fila)
        #print ( "visitado :", visitado)
        #print ( "grafo ", grafo)
        cola =[]

        cola.append(s)
        visitado[s] = True
        #Cola es para encontrar el camino hasta t. se procesa mientra tenga valores.
        while cola:
            u = cola.pop(0)

         #   print("u...:", u)
         #   print("padre : ", padre)
            for ind,val in enumerate(self.grafo[u]):
             #   print ( "grafo val : ",val)
             #   print ( "visitados :", visitado)
                if visitado[ind]==False and val > 0 :
                    cola.append(ind)
                    visitado[ind] = True
                    padre[ind]= u
                    print("cola modificada :",cola)
             #       print("Pdre : ", padre )


        return True if visitado[t] else False

    def FordFulkerson(self,salida,llegada):

        padre =[-1]*(self.fila)
        # Contador de Maximo flujo , por default nace en 0
        max_flujo = 0
        # aumento el flujo mientras haya camino
        while self.encontrarCamino(salida,llegada , padre):
            # Establece la veriable infinito para comparación
            camino_flujo = float("inf")
            s=llegada
            while (s != salida):
                print ("salida s ",s)
                camino_flujo = min(camino_flujo, self.grafo[padre[s]][s])
                s=padre[s]
            #Añade el flujo obtenido al flujo total
            max_flujo += camino_flujo
            #Actualiza la capacidad residual de las aristas y las aristas inversas
            v = llegada
            while ( v != salida ):
                u = padre[v]
                self.grafo[u][v] -= camino_flujo
                self.grafo[v][u] += camino_flujo
                v = padre[v]
        # Este último print es importante , ya que el grafo ( adyacencia con pesos ) , nos queda
        # si la graficacamos , con los principales arcos de corte que en este caso son 3
        t->4 , t->2 , 3->S , con la nomenclatura del ej. osea salida es : "S" , y sumidero "t"
        print("grafo final ", self.grafo)
        return max_flujo


grafo = [[0,7,1,0,0,0],
         [0,0,0,2,0,3],
         [0,0,0,0,2,0],
         [0,0,0,0,0,1],
         [0,0,0,0,0,2],
         [0,0,0,0,0,0]]

salida = 0
llegada = 5
g= Grafo(grafo)
print ( "El Maximo flujo es %d " % g.FordFulkerson(salida,llegada))