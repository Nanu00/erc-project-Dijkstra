from prm import Graph
from utils import Point
import networkx as nx

class AStar():
    def __init__(self, graph: Graph):
        self.graph = graph

        minx, miny, maxx, maxy = self.graph.end_zone.pol.bounds
        self.__end_point_apprx = Point( (minx+maxx)/2, (miny+maxy)/2 )

    @staticmethod
    def trace_path(came_from: dict, pt: Point):
        current = pt
        path = []
        while current:
            path.append(current)
            current = came_from[current]
        return path

    def pathfind(self):
        start = self.graph.start_point
        open_set = [start]
        came_from = {n: None for n in self.graph.nodes}

        g_score = {n: float('inf') for n in self.graph.nodes}
        g_score[start] = 0

        f_score = {n: float('inf') for n in self.graph.nodes}
        f_score[start] = start.distance(self.__end_point_apprx)

        while len(open_set):
            current = sorted(open_set, key = lambda p: f_score[p])[0]

            if self.graph.end_zone.pol.contains(current):
                return self.trace_path(came_from, current)

            open_set.remove(current)

            for neighbor in nx.neighbors(self.graph, current):
                tentative_g_score = g_score[current] + current.distance(neighbor)
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + neighbor.distance(self.__end_point_apprx)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return None
