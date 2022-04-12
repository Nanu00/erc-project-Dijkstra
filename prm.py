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

        self.dist_limit = abs(min([self.boundaries[0].x - self.boundaries[1].x, self.boundaries[0].y - self.boundaries[1].y]))/5

    def sample(self, num: int):
        for _ in range(num):
            new_point = Point.random_with_boundaries(self.boundaries)

            outside = [o.pol.contains(new_point) for o in self.obstacles]
            if any(outside):
                break

            self.add_node(new_point)

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
