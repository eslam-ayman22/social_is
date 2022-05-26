#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[2]:



def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'asleep'
    return state


# In[3]:


initial_state(G)


# In[15]:


import random

P_AWAKEN = 0.2
def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'asleep':
            if random.random() < P_AWAKEN:
                next_state[node] = 'awake'
    return next_state


# In[16]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[ ]:


from simulation import Simulation

sim = Simulation(G, initial_state, state_transition, name='Simple Sim')


# In[20]:


sim.state()


# In[21]:


sim.draw()


# In[22]:


sim.run()


# In[23]:


sim.steps


# In[24]:


sim.draw(with_labels=True)


# In[25]:


sim.state()


# In[26]:


sim.run(10)


# In[27]:


sim.steps


# In[28]:


sim.draw(with_labels=True)


# In[29]:


sim.plot()


# In[30]:


sim.draw(4, with_labels=True)


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[32]:


import random
import string

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = random.choice('ABCD')
    return state


# In[34]:


initial_state(G)


# In[35]:


def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        # Caveat: what if the node has no neighbors?
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[36]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[37]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[39]:


sim.draw()


# In[40]:


sim.run(40)


# In[41]:


sim.draw()


# In[42]:


import random

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[43]:


def state_transition_async(G, current_state):
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[44]:


def state_transition_async(G, current_state):
    # Randomizing the update order prevents bias
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[45]:


sim = Simulation(G, initial_state, state_transition_async, name='Async Voter Model')
sim.run(40)
sim.plot()


# In[47]:


def stop_condition(G, current_state):
    unique_state_values = set(current_state.values())
    is_stopped = len(unique_state_values) <= 1
    return is_stopped


# In[48]:


sim = Simulation(G, initial_state, state_transition, stop_condition, name='Voter model')
sim.run(100)


# In[49]:


sim.steps


# In[50]:


def state_transition_async_rewiring(G, current_state):
    # Randomizing the update order prevents bias
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            # This is the same as before
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
            # This is the new part
            neighbor = random.choice(list(G.neighbors(node)))
            if current_state[node] != current_state[neighbor]:
                G.remove_edge(node, neighbor)
            
    return current_state


# In[51]:


sim = Simulation(G, initial_state, state_transition_async_rewiring, stop_condition,
                 name='Voter Model with rewiring')
sim.draw()


# In[52]:


sim.run(40)
sim.draw()


# In[53]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[54]:


import random

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'S'
    
    patient_zero = random.choice(list(G.nodes))
    state[patient_zero] = 'I'
    return state


# In[55]:


initial_state(G)


# In[56]:


MU = 0.1
BETA = 0.1

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'I':
            if random.random() < MU:
                next_state[node] = 'S'
        else: # current_state[node] == 'S'
            for neighbor in G.neighbors(node):
                if current_state[neighbor] == 'I':
                    if random.random() < BETA:
                        next_state[node] = 'I'

    return next_state


# In[57]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[58]:


sim = Simulation(G, initial_state, state_transition, name='SIS model')


# In[59]:


sim.draw()


# In[60]:


sim.run(25)


# In[61]:


sim.draw()


# In[62]:


sim.plot()


# In[ ]:




