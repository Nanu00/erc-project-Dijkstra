import random
import networkx as nx
from utils import Point
from obstacle import Obstacle, EndArea

class Graph(nx.Graph):
    def __init__(self, start_point: Point, obstacles: list[Obstacle], end_zone: EndArea, boundaries: tuple[Point, Point]):
        super().__init__()

        self.add_node(start_point)
        self.obstacles = obstacles
        self.end_zone = end_zone
        self.boundaries = boundaries
        self.start_point = start_point

        self.dist_limit = abs(min([self.boundaries[0].x - self.boundaries[1].x, self.boundaries[0].y - self.boundaries[1].y]))/5

    def sample(self, num: int):
        i = 0
        while i < num:
            if i == 0:
                minx, miny, maxx, maxy = self.end_zone.pol.bounds
                new_point = None
                while not new_point:
                    p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
                    if self.end_zone.pol.contains(p):
                        new_point = p
            else:
                new_point = Point.random_with_boundaries(self.boundaries)

            outside = [o.pol.contains(new_point) for o in self.obstacles]
            if any(outside):
                continue

            self.add_node(new_point)

            i+=1

            for node in self.nodes:
                intersections = [o.checkint(node, new_point) for o in self.obstacles]

                if any(intersections):
                    continue
                if new_point.distance(node) > self.dist_limit:
                    continue

                self.add_edge(node, new_point)

    def get_plottable(self):
        plottables = []
        for (u, v) in self.edges:
            plottables.append(([u.x, v.x], [u.y, v.y], "b-"))
        return plottables
