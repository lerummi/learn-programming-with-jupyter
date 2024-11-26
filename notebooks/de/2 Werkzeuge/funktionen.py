import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from variablen import (
    lebenspunkte, 
    veraendere_lebenspunkte,
    lebenspunkte_als_variablen
)

lebenspunkte = veraendere_lebenspunkte(lebenspunkte)
from variablen import lebenspunkte_als_variablen
globals().update(lebenspunkte_als_variablen(lebenspunkte))

Start_c = c_Start = Start_a + a_b + b_c
c_Zwerg = Zwerg_c = c_d + d_i + i_j + j_k + k_l + l_Zwerg
c_Riese = Riese_c = c_Zwerg - l_Zwerg + l_Riese
c_Magier = Magier_c = c_f + f_m + m_Magier
Magier_Hexe = Hexe_Magier = m_Magier + f_m + f_o + e_g + e_g + g_Hexe
c_Hexe = Hexe_c = c_e + e_g + g_Hexe
Hexe_y = y_Hexe = g_Hexe + g_r + r_v + v_y
Magier_y = y_Magier = m_Magier + f_m + f_o + o_p + p_q + q_r + r_v + v_y
c_y = y_c = c_d + d_n + n_s + s_v + v_y
Zwerg_y = y_Zwerg = Zwerg_s + s_v + v_y
Riese_y = y_Riese = Riese_u + u_y
y_Schatz = Schatz_y = y_z + z_Schatz

nodes = ["Start", "c", "Zwerg", "Riese", "Magier", "Hexe", "y", "Schatz"]
edges = [
    ("Start", "c", Start_c),
    ("c", "Zwerg", c_Zwerg),
    ("c", "Riese", c_Riese),
    ("c", "Magier", c_Magier),
    ("Magier", "Hexe", Magier_Hexe),
    ("c", "Hexe", c_Hexe),
    ("Hexe", "y", Hexe_y),
    ("Magier", "y", Magier_y),
    ("c", "y", c_y),
    ("Zwerg", "y", Zwerg_y),
    ("Riese", "y", Riese_y),
    ("y", "Schatz", y_Schatz)
]

G = nx.Graph()
for node in nodes:
    G.add_node(node)
for egde in edges:
    G.add_edge(*egde[0:2], weight=np.round(egde[2], 2))

def zeichne(G):

    # Draw the graph with node and edge attributes
    pos = nx.spring_layout(G)  # Layout for node positions
    node_labels = nx.get_node_attributes(G, 'label')  # Get node labels for visualization
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Get edge weights for visualization

    plt.figure(figsize=(5, 5))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=12, font_weight='bold', node_size=50)

    # Draw the edge weights and node labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
