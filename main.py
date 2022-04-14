from prm import Graph
from obstacle import EndArea, Obstacle
from utils import Point as P
from matplotlib import pyplot as plt

from astar import AStar

# Define all the obstables
obs = [
    Obstacle((P(700, 700), P(800, 700), P(800, 600), P(600, 600), P(600, 800), P(700, 800))),
    Obstacle((P(1, 12), P(20, 42), P(80, 20))),
    Obstacle((P(120, 90), P(90, 200), P(400, 200))),
]

# Define the end area
end = EndArea((P(700, 700), P(750, 700), P(750, 750), P(700, 750)))

g = Graph(P(1, 1), obs, end, (P(0, 0), P(1000, 1000)))

g.sample(500)

plottables_statics = [o.get_plottable() for o in g.obstacles]
plottables_statics.append(end.get_plottable())

plottables_graph = g.get_plottable()

plt.ion()
[plt.plot(*p, linewidth=1) for p in plottables_statics]
[plt.plot(*p, marker='.', markersize=1, linewidth=0.1) for p in plottables_graph]
plt.show()
plt.pause(5)

a = AStar(g)
astar_path = a.pathfind()

if astar_path is not None:
    plt.plot([p.x for p in astar_path], [p.y for p in astar_path], 'y-', marker='x', markersize=5, linewidth=1)
    plt.ioff()
    plt.show()
else:
    print("A* failed!")
