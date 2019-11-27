
class Graph:

    def __init__(self, graph, nb_node):
        self.graph = graph
        self.nb_node = nb_node

    '''Returns true if path found, return False if end can't be found
    Also fills parents[] to store the path '''
    def BFS(self, start, end, parents):
   # OPEN // the list of nodes to be evaluated
   # visited // the list of nodes already visited
        open_list = []
        visited = []
        open_list.append(start)
        visited.append(start)
        while open_list:
            # sortir le premier element dans open_list, c'est-à-dire qu'il n'est plus
            # dans open_list
            current = open_list.pop(0)
            visited.append(current)

            if current == end:
                return (True)

            # parcourir graph[current], i est index, value = graph[current][i]
            # si value > 0 : node i est lié à node current, et pipe non occcupé
            for i, value in enumerate(self.graph[current]):
                if  value > 0 and i not in visited:
                    open_list.append(i)
                    visited.append(i)
                    parents[i] = current
        return (False)


    def print_graph(self):
        for x in range(self.nb_node):
            print(self.graph[x])




    def Fulkerson_algo(self, start, end):
        parents = [-1 for i in range(self.nb_node)]
        max_flow = 0

                # décommente deux lines ci dessous pour voir graph
        # print("Initial graph")
        # self.print_graph()

        #augmenter flow tant qu'il y a nouveau path
        while self.BFS(start, end, parents):
            max_flow += 1
            child = end;

            #suivre le chemin, à partir de "end" jusqu'à "start"
            # pour reset le valeur dans graph
            while (child != start):
                papa = parents[child]
                #les pipes de start à end devient 0
                self.graph[papa][child] -=1
                # l'autre sens devient 2
                self.graph[child][papa] +=1
                # remote vers le node precedent
                child = papa;

                # décommente deux lines ci dessous pour voir graph
        # print("algo done graph:")
        # self.print_graph()
        return max_flow

    # une fois paths récupéré, graph revient son etat initial
    def get_paths_from_graph(self, nb_path, start, end):
        paths = []
        i = 0
        while i < nb_path:
            paths.append([])
            paths[i].append(end)
            y = end
            while y != start:
                for x in range(self.nb_node):
                    if self.graph[y][x] == 2:
                        paths[i].insert(0, x);
                        self.graph[x][y] += 1
                        self.graph[y][x] -= 1
                        break
                y = x
            i += 1
        return paths


def print_paths(paths):
    for i in range(len(paths)):
        print("Path No ", i , ':')
        for x in paths[i]:
            print (index_to_name[x], "-> ", end='')
        print('\n\n')



graph = [[ 0, 0, 1, 0, 1, 0, 0, 0],
   [ 0, 0, 0, 1, 0, 0, 0, 1],
   [ 1, 0, 0, 1, 0, 0, 1, 0],
   [ 0, 1, 1, 0, 0, 1, 0, 0],
   [ 1, 0, 0, 0, 0, 1, 0, 0],
   [ 0, 0, 0, 1, 1, 0, 0, 0],
   [ 0, 0, 1, 0, 0, 0, 0, 1],
   [ 0, 1, 0, 0, 0, 0, 1, 0]]

index_to_name = {0: 'S', 1 : 'T', 2:  'a', 3 :'b', 4: 'c', 5: 'd', 6 :'e', 7:'f'}




g = Graph(graph, 8)
# id of start node is 0, id of end node is 2
start = 0;
end = 1;
print('graph initial')
g.print_graph()



max_flow = g.Fulkerson_algo(start, end)
print('graph after Fulkerson_algo')
g.print_graph()
print('\n\n')

print("max_flow:", max_flow, '\n\n')

paths = g.get_paths_from_graph(max_flow, start, end)
print_paths(paths)




