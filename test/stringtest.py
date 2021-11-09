def clearNode(transicionCompleta):
    nodeA = ""
    nodeB = ""
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
                print("caracter: "+node)
                nodeA = nodeA+node               
                print("Nodo final: "+transicionCompleta)
        if numbernode == 1:
            if (node >= chr(65) and node <= chr(122)) or (node >= chr(48) and node <= chr(57)):
                print("caracter: "+node)
                nodeCamino = nodeCamino+node
                print("Nodo final: "+transicionCompleta)
        if numbernode == 2:
            if (node >= chr(65) and node <= chr(122)) or (node >= chr(48) and node <= chr(57)):
                print("caracter: "+node)
                nodeB = nodeB+node
                print("Nodo final: "+transicionCompleta)
    return nodeA, nodeB, nodeCamino
    
print("imprimiendo una coma, creo: "+chr(44))
transicion = input("Ingrese una transicion: ")
#print("primer nodo: "+ transicion[0])
nodeA, nodeB, camino = clearNode(transicion)

print("primer nodo: "+nodeA)
print("segundo nodo: "+nodeB)
print("camino: "+camino)
#print("nodo A: "+nodeA+" nodo B: "+nodeB)