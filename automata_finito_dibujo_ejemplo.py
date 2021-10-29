import graphviz
#Comentario desde visual
f = graphviz.Digraph('finite_state_machine', filename='fsm.png')
f.attr(rankdir='LR', size='100')
a='a'
b='b'
c='c'
lenguaje = ['0','1']
# Nodo inicial recibir algo. y hacer cosas muy de jakers
f.node( name='', shape='point')
f.node(a,shape='circle')
f.edge( '',a,'',shape='point')

#   Nodos terminales
f.attr('node', shape='doublecircle')
f.node(c)

#   Nodos simpleas
f.attr('node', shape='circle')
f.edge(b, c, label=lenguaje[0])
f.edge(b, b, label=lenguaje[0])
f.edge(a, b, label=lenguaje[0])
f.edge(c, a, label=lenguaje[1])

f.render()
#ultima modificacion 29 de cotubre 18:37