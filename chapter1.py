#!/usr/bin/env python
# coding: utf-8

# In[6]:


####################################
#EXERCISE 1
import networkx as nx
G=nx.Graph()
nodes_to_add=['b','c','d','a','f']
#G.add_nodes_from(nodes_to_add)
G.add_edge('a','c')
edges_to_add = [('a', 'c'),('c', 'd'), ('b', 'd'),('f', 'd')]
G.add_edges_from(edges_to_add)
nx.draw(G,with_labels=True,node_color='red',node_size=1200,font_color='blue',font_size=12)
li=[]
def get_leaves(g):
    for node in g.nodes:
        if g.degree(node)==1:
            li.append(node)
    return li            
print(get_leaves(G))

  


# In[7]:


############################
#EXERCISE 2

import networkx as nx
G=nx.Graph()
nodes_to_add=['b','c','d']
#G.add_nodes_from(nodes_to_add)
G.add_edge('a','b')
edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_edges_from(edges_to_add)
nx.draw(G,with_labels=True,node_color='yellow',node_size=1600,font_color='red',font_size=16)
l=[]
def max_degree(g):
    x=0
    y=''
    for node in g.nodes:
        if x < g.degree(node):
            x=g.degree(node)
            y=node
    l.append(('name',y))
    l.append(('degree',x))
    return l            
print(max_degree(G))


# In[10]:


############################
#EXERCISE 3
import networkx as nx
G=nx.Graph()
nodes_to_add=['b','c','d','a','f']
G.add_edge('a','c')
edges_to_add = [('a', 'c'),('c', 'd'), ('b', 'd'),('f', 'd'),('c','b')]
G.add_edges_from(edges_to_add)
nx.draw(G,with_labels=True,node_color='yellow',node_size=1600,font_color='red',font_size=16)
l=[]
def mutual_friends(g, node_1, node_2):
    x1=list(g.neighbors(node_1))
    y2=list(g.neighbors(node_2))
    for node1 in x1:
        for node2 in y2:
            if node1==node2:
                l.append(node1)
    return l
mutual_friends(G,'c','d')


# In[ ]:




