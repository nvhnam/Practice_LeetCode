# import sys
# import heapq
# from collections import defaultdict

# class CountryRoads:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def read_input(self):
#         input = sys.stdin.read
#         data = input().split()
#         print("data: ", data)
        
#         self.t = int(data[0])
#         self.index = 1
#         self.test_cases = []

#         for _ in range(self.t):
#             n = int(data[self.index])
#             # print("self.index: ", self.index)
#             m = int(data[self.index + 1])
#             # print("self.index + 1: ", self.index)
#             self.index += 2
#             # print("self.index += 2: " , self.index)
            
#             graph = defaultdict(list)
#             # print("Graph before: ", graph)
#             for _ in range(m):
#                 u = int(data[self.index])
#                 # print("self.index in m: " , self.index)
#                 v = int(data[self.index + 1])
#                 # print("self.index in m + 1: " , self.index)
#                 w = int(data[self.index + 2])
#                 self.index += 3
#                 graph[u].append((v, w))
#                 graph[v].append((u, w))
            
#             # print("Graph after: ", graph)
#             target = int(data[self.index])
#             self.index += 1

#             self.test_cases.append((n, graph, target))

#     def dijkstra(self, n, graph, target):
#         INF = float('inf')
#         dist = [INF] * n
#         print("dist: ", dist)
#         dist[target] = 0
#         print("dist[target]: ", dist[target])

#         min_heap = [(0, target)]
#         print("Min_heap: ", min_heap)

#         while min_heap:
#             current_cost, u = heapq.heappop(min_heap)
#             print("current_cost: ", current_cost)
#             print("u: ", u)
#             print("dist[u]: ", dist[u])

#             if current_cost > dist[u]:
#                 continue

#             for v, weight in graph[u]:
#                 new_cost = max(current_cost, weight)
#                 print("new_cost: ", new_cost)
#                 print("current_cost and weight: ", current_cost, weight)
#                 if new_cost < dist[v]:
#                     dist[v] = new_cost
#                     print("accepted_new_cost: ", dist[v])
#                     heapq.heappush(min_heap, (new_cost, v))

#         return dist

#     def solve(self):
#         self.read_input()
#         results = []
#         print("self.test_cases: ", self.test_cases)

#         for case_num, (n, graph, target) in enumerate(self.test_cases, start=1):
#             dist = self.dijkstra(n, graph, target)
            
#             results.append(f"Case {case_num}:")
#             for d in dist:
#                 results.append("Impossible" if d == float('inf') else str(d))

#         print("\n".join(results))


# import sys
#     input = sys.stdin.read
#     data = input().split()

import heapq
from collections import defaultdict
import sys

class CountryRoads:
    def __init__(self):
        self.graph = defaultdict(list)

    def read_put(self):
        input = sys.stdin.read
        data = input().split()
        
        self.t = int(data[0])
        self.index = 1
        self.test_case = []

        for _ in range(self.t):
            n = int(data[self.index])
            m = int(data[self.index + 1])
            self.index += 2

            graph = defaultdict(list)
            for _ in range(m):
                u = int(data[self.index])
                v = int(data[self.index + 1])
                w = int(data[self.index + 2])

                self.index += 3

                graph[u].append((v, w))
                graph[v].append((u, w))
            
            target = int(data[self.index])

            self.index += 1

            self.test_case.append((n, graph, target))

    def dijkstra(self, n, graph, target):
        INF = float("inf")
        dist = [INF] * n
        dist[target] = 0

        min_heap = [(0, target)]

        while min_heap:
            current_cost, u = heapq.heappop(min_heap)

            if(current_cost > dist[u]):
                continue


            for v, weight in graph[u]:
                new_cost = max(current_cost, weight)
                if (new_cost < dist[v]):
                    dist[v] = new_cost
                    heapq.heappush(min_heap, (new_cost, v))
        
        return dist
    
    
    def solve(self):
        self.read_put()
        results = []

        for case_num, (n, graph, target) in enumerate(self.test_case, start=1):
            dist = self.dijkstra(n, graph, target)

            results.append(f"Case {case_num}: ")

            for d in dist:
                results.append("Impossible" if d == float("inf") else str(d))
        print("\n".join(results))
