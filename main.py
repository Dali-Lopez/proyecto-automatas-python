import graphviz
#Generando el diagrama
f = graphviz.Digraph('finite_state_machine', filename='diagrama.png')
f.attr(rankdir='LR',size='800')

nodo_inicial = {'a'}
a='Nodo inicial'
#dibujar nodo inicial
f.node( name='', shape='point')
f.node(a,shape='circle')
f.edge( '',nodo_inicial,'',shape='point')

vector = {'a':2,'v':1}
print(vector.get('a'))
print(type(vector))
#Generar el diagrama
f.render()
