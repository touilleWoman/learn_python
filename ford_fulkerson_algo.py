8 nodes en total.

      [S]
    /  |
  [c] [a]--[e]
  /    |    |
[d]-- [b] [f]
       |   /
      [T]


----------------------
structure t_lemin:

int32_t   **gragh;     #residual graph, index correspond à id de node,
                        #si valeur == 0, pas de pipe entre les deux node
                        #si valeur == 1, les deux nodes sont liés, et capacité de passage est 1
                        #si valeur == -1, les deux nodes sont liés, ce pipe est occupé.
# malloc gragh[8][8]

t_node   *tab;        #tableau de l'adresse de node, index correspond à id de node,
                        #c'est pas un hashtab, pas de doublon
                        #tab[0] est start node, tab[1] est end node.
# malloc tab[8]
int32_t     nb_ants;
int32_t     nb_nodes;
-----------------------

Etat de Residual gragh Initialisé:

        Index   0   1   2   3   4   5   6   7
Index  Name     S   T   a   b   c   d   e   f
0       S     [ 0   0   1   0   1   0   0   0   ]
1       T     [ 0   0   0   1   0   0   0   1   ]
2       a     [ 1   0   0   1   0   0   1   0   ]
3       b     [ 0   1   1   0   0   1   0   0   ]
4       c     [ 1   0   0   0   0   1   0   0   ]
5       d     [ 0   0   0   1   1   0   0   0   ]
6       e     [ 0   0   1   0   0   0   0   1   ]
7       f     [ 0   1   0   0   0   0   1   0   ]

On va trouvé les valeurs avec leur index, j ai écrit quand même le nom pour plus clair.

--------------------
structure t_node:

uint32_t        id;           #index dans tab
char            *name;        #Nom du noeud
int32_t         x;            #position de noeud
int32_t         y;
int32_t         parent_id;    #Initialisé à -1 , it sera rempli au moment de BFS
                              # il sert à retracer le chemin une fois le chemin trouvé par BFS.

uint32_t        weight;         #pour BFS
--------------------


OPEN // the set of nodes to be evaluated
CLOSED // the set of nodes already evaluated

add start node to OPEN, weight = 0

while
current = node in OPEN with lowest Weight
remove current from OPEN
add current to CLOSED

if current == end
    return

for each neigbour of current node
    if neighbour in CLOSED
        skip to next neighbor

    if neighbour not in OPEN
        add neighbour to OPEN
        set weight of neighbour = weight of current +1
        set parent of neighbour is current
        //parent sera utilisé par retracer une fois le chemin trouvé.






