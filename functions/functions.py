import graphviz
class count_entry_position:
    x = 0
    y = 0
    def __init__(self, px, py):
        self.x = px
        self.y = py
        print("x: ",self.x," y: ",self.y)    
    def newValues(self):
        print("x: ",self.x," y: ",self.y)
        if self.y == 640:
            self.y = 190
            self.x = self.x + 100
        else:
            self.x = self.x + 0
            self.y = self.y + 30
def getValues_function(self,list_values):
    for value in list_values:
            print("valores para las entradas: ", value.get())
class automata:
    def __init__(self,estados, alfabeto, transiciones_list, estado_inicial, estados_finales):
        transiciones_list_prueba = ['q0,1=q0','q0,0=q1','q1,0=q1','q1,1=q2','q2,0=q2','q2,1=q2']
        print("Valores del automata")
        print("Estadps: ",estados," Alfabeto: ",alfabeto," Transiciones: ", transiciones_list[0].get()," Estados iniciales: ", estado_inicial,"Estados finales: ", estados_finales)
        # Preparar el automata
        
        f = graphviz.Digraph('finite_state_machine', filename='diagrama_automata', format='png')
        f.attr(rankdir='LR', size='100')
        #### Nodo inicial
        print(type(estado_inicial))
        f.node( name='', shape='point')
        f.node(estado_inicial,shape='circle')
        f.edge( '',estado_inicial,'',shape='point')
        #### Nodo Inicial
        
        #### Nodos terminales
        f.attr('node', shape='doublecircle')
        list_nodos_finales = self.list_values_nodes(estados_finales)
        for item in list_nodos_finales:
            f.node(item)
        #f.node(c)
        #### Nodos terminales
        
        #### Transiciones
        f.attr('node', shape='circle')
        for transicion in transiciones_list_prueba:
            nodo_inicio, nodo_final, camino = self.clearNode(transicion)
            f.edge(nodo_inicio, nodo_final, camino)
        #### Transiciones
        
        #### Render diagram
        f.render()
    def nodos_finales(self,nodos):
        print (nodos)
    def list_values_nodes(self, list_values):
        nodos_list = list()
        count_list = 0
        newAppend = 0
        for node in list_values:
            #print("Imprimiendo al caracter del nodo completo: "+node)
            if newAppend == 0:
                nodos_list.append("")
                newAppend = 1
            if (node >= chr(65) and node <= chr(122)) or (node >= chr(48) and node <= chr(57)):
                    print("caracter: "+node)
                    nodos_list[count_list] = nodos_list[count_list]+node               
                    #print("Nodo final: "+transicionCompleta)
            if node == chr(44):
                newAppend = 0
                count_list = count_list + 1
        print("NODOS FINALES: ",nodos_list)
        return nodos_list    
    def clearNode(self,transicionCompleta):
        nodeInicio = ""
        nodeFinal = ""
        nodeCamino = ""
        numbernode = 0
        for node in transicionCompleta:
            #print("Imprimiendo al caracter del nodo completo: "+node)
            if node == chr(44):
                numbernode = 1
            if node == chr(61):
                numbernode = 2
            if numbernode == 0:
                if (node >= chr(65) and node <= chr(122)) or (node >= chr(48) and node <= chr(57)):
                    nodeInicio = nodeInicio+node               
            if numbernode == 1:
                if (node >= chr(65) and node <= chr(122)) or (node >= chr(48) and node <= chr(57)):
                    nodeCamino = nodeCamino+node
            if numbernode == 2:
                if (node >= chr(65) and node <= chr(122)) or (node >= chr(48) and node <= chr(57)):
                    nodeFinal = nodeFinal+node
        print("transicion: ",nodeInicio, nodeFinal, nodeCamino)
        return nodeInicio, nodeFinal, nodeCamino
        