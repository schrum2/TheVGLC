
from math import sqrt
from heapq import heappush, heappop

def astar_shortest_path(src, isdst, adj,subOptimal,heuristic):
    dist = {}
    prev = {}
    dist[src] = 0
    prev[src] = None
    heap = [(dist[src], src,0)]

    pathLength = float('inf')
    paths = []
    while heap:
        node = heappop(heap)
        if isdst(node[1]):
            if node[0] < pathLength:
                pathLength = node[0]
                path = []
                nodeR = node[1]
                while nodeR:
                    path.append(nodeR)
                    nodeR = prev[nodeR]
                path.reverse()
                paths.append(path)
                continue
            elif node[0] > pathLength+subOptimal:
                break
            else:
                path = []
                nodeR = node[1]
                while nodeR:
                    path.append(nodeR)
                    nodeR = prev[nodeR]
                path.reverse()
                paths.append(path)
                continue

        for next_node in adj(node):
            next_node[0] += heuristic(next_node[1])
            next_node.append(heuristic(next_node[1]))
            if next_node[1] not in dist or next_node[0] < dist[next_node[1]]:
                #print node[1],next_node[1],heuristic(next_node[1])
                #exit()

                dist[next_node[1]] = next_node[0]
                prev[next_node[1]] = node[1]
                heappush(heap, next_node)

    return paths
