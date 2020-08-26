from math import inf
from heapq import heappush, heappop, heapify
from time import time

#https://pythontic.com/algorithms/heapq/introduction
#https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes

def MST_prim(graph):
    #s is any arbitrary vertex in Graph. Here, vertex 1
    s = list(graph)[0]
    #S is Set consisting of the arbitrary vertex s
    S = set([s])
    V = set(graph)
    dv = []
    Q = []
   
    #pushing v and dv of vertex V in the queue
    #for vertex 1
    #[2, 5] and [8, 12] are the associated vertices and weights.
    for v in graph[s]:
        heappush(Q, [v[1], v[0]])
    #S = {1} and V = {all the vertices}
    #Run while loop, for all the vertices in V
    while S != V:
        #The heappop() function removes and returns the smallest element from the heap, So [2,5] will be popped and stored in u.
        u = heappop(Q)

        #S = S{u}
        #https://docs.python.org/2/library/sets.html
        S |= set([u[1]])
        print(S)
        #Adding the weight of the smaller vertex chosen to list dv
        dv.append(u[0])
        
        #https://www.tutorialspoint.com/python_data_structure/python_heaps.htm
        #https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
        #Considering the case now where we can reach a vertex v from u while adding u we find smaller weight then update
        for v in Q:
            if v[1] == u[1]:
                v[0] = inf
        heapify(Q)

        for v in graph[u[1]]:
            if v[0] not in S:
                heappush(Q, [v[1], v[0]])

    return sum(dv)

def main():
    graph = {}
    with open('input.txt') as f:
        edges_vertices = next(f)
        e_v = list(map(int,edges_vertices[:-1].split(" ")))
        n = e_v[0]
        m = e_v[1]

        data = f.readlines() 
        #https://www.quora.com/What-does-the-following-line-mean-in-Python-list-map-int-input-strip-split-I
		#https://stackoverflow.com/
        for line in data:
            elements = list(map(int,line[:-1].strip().split(" ")))
            vertex1 = elements[0]
            vertex2 = elements[1]
            weight = elements[2]

            try:
                (graph[vertex1]).append([vertex2 , weight])
            except KeyError:
                graph[vertex1] = [[vertex2 , weight]]
            try:
                (graph[vertex2]).append([vertex1 , weight])
            except KeyError:
                graph[vertex2] = [[vertex1 , weight]]
                

    print(MST_prim(graph))
    
if __name__ == '__main__':
    main()