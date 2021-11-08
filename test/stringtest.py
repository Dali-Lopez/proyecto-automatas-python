def clearNode(nodeComplete):
    nodeA = ""
    nodeB = ""
    for node in nodeComplete:
        #print("Imprimiendo al caracter del nodo completo: "+node)
        if node >= chr(65) and node <= chr(122):
            print("caracter: "+node)
            nodeA = nodeA+node
    #nodeA = "a"       
    nodeB = "b"
    #nodeA = node[0]
    #nodeB = node[1]
    return nodeA, nodeB
    
print("imprimiendo una coma, creo: "+chr(44))
transicion = input("Ingrese una transicion: ")
print("primer nodo: "+ transicion[0])
nodeA, nodeB = clearNode(transicion)
print("primer nodo chido jejejej XD: "+nodeA)
#print("nodo A: "+nodeA+" nodo B: "+nodeB)