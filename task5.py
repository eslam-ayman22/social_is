#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[2]:


p = 0.75

# Do this 7 times
for _ in range(7):
    r = random.random()
    if r < p:
        print('Heads')
    else:
        print('Tails')


# In[3]:


names = ['Alice', 'Bob', 'Cathy', 'Dan']
random.choice(names)#choose one random element from list


# In[4]:


G = nx.cycle_graph(5)
random.sample(G.nodes, 2)#return list from random 3 elements


# In[5]:


names = ['Alice', 'Bob', 'Carol']
tickets = [1, 3, 4]

for _ in range(10):
    print(random.choices(names, tickets))


# In[6]:


random.choices(names, tickets, k=10)


# In[7]:


elements = [0, 1, 2, 3, 4]
list(itertools.combinations(elements, 2))


# In[8]:


G = nx.Graph()
G.add_nodes_from(elements)

list(itertools.combinations(G.nodes, 2))


# In[9]:


def gnp_random_graph(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    for i, j in itertools.combinations(G.nodes, 2):
        r = random.random()
        if r < p:
            G.add_edge(i, j)
        # Do nothing if r >= p
        
    return G


# In[10]:


G = gnp_random_graph(16, 0.15)
nx.draw(G)
print('Graph has', G.number_of_edges(), 'edges.') # each time number of edges will be diffrent


# In[11]:


def gnm_random_graph(N, M):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    possible_edges = itertools.combinations(G.nodes, 2)
    edges_to_add = random.sample(list(possible_edges), M)
    G.add_edges_from(edges_to_add)
    
    return G


# In[12]:


G = gnm_random_graph(16, 18)
nx.draw(G)


# In[13]:


N = 10
G = nx.cycle_graph(N)
nx.draw_circular(G, with_labels=True)


# In[14]:


k = 4

for n in G.nodes:
    for i in range(1, k // 2 + 1):
        left  = (n-i) % N
        right = (n+i) % N 
        G.add_edge(n, left)
        G.add_edge(n, right)

nx.draw_circular(G, with_labels=True)


# In[15]:


p = 0.1

for u, v in list(G.edges):
    if random.random() < p:
        not_neighbors = set(G.nodes) - set(G.neighbors(u))
        w = random.choice(list(not_neighbors))
        G.remove_edge(u, v)
        G.add_edge(u, w)

nx.draw_circular(G, with_labels=True)


# In[16]:


def watts_strogatz_graph(N, k, p):
    # 1. Create a ring of N nodes
    G = nx.cycle_graph(N)

    # 2. Connect each node n to k nearest neighbors
    #    [n-(k//2), ... , n-1, n+1, ... , n+(k//2)]
    for n in G.nodes:
        for i in range(1, k // 2 + 1):
            left  = (n-i) % N
            right = (n+i) % N 
            G.add_edge(n, left)
            G.add_edge(n, right)
    
    # 3. Rewire edges with probability p
    for u, v in list(G.edges):
        if random.random() < p:
            not_neighbors = set(G.nodes) - set(G.neighbors(u)) - {u}
            w = random.choice(list(not_neighbors))
            G.remove_edge(u, v)
            G.add_edge(u, w)

    return G


# In[17]:


G = watts_strogatz_graph(16, 4, 0.2)
nx.draw_circular(G, with_labels=True)


# In[18]:


G = watts_strogatz_graph(16, 4, 0.2)
nx.draw_circular(G, with_labels=True)


# In[19]:


def barabasi_albert_graph(N, m):
    # 1. Start with a clique of m+1 nodes
    G = nx.complete_graph(m + 1)
    for i in range(G.number_of_nodes(), N):
        # 2. Select m different nodes at random, weighted by their degree.
        new_neighbors = []
        possible_neighbors = list(G.nodes)
        for _ in range(m):
            degrees = [G.degree(n) for n in possible_neighbors]
            j = random.choices(possible_neighbors, degrees)[0]
            new_neighbors.append(j)
            possible_neighbors.remove(j)
        
        # 3. Add a new node i and link it with the m nodes from the previous step.
        for j in new_neighbors:
            G.add_edge(i, j)

    return G


# In[20]:


G = barabasi_albert_graph(30, 1)
nx.draw(G)


# In[ ]:




