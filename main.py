from prm import Graph
from obstacle import EndArea, Obstacle
from utils import Point as P
from matplotlib import pyplot as plt

from astar import AStar

# Define all the obstables
obs = [ Obstacle((P(600, 700), P(700, 600), P(700, 700))) ]

# Define the end area
end = EndArea((P(700, 700), P(750, 700), P(750, 750), P(700, 750)))

g = Graph(P(500, 500), obs, end, (P(0, 0), P(1000, 1000)))

g.sample(200)

plottables_statics = [o.get_plottable() for o in g.obstacles]
plottables_statics.append(end.get_plottable())

plottables_graph = g.get_plottable()

plt.ion()
[plt.plot(*p, linewidth=1) for p in plottables_statics]
[plt.plot(*p, marker='.', markersize=1, linewidth=0.1) for p in plottables_graph]
plt.show()
plt.pause(1)

a = AStar(g)
astar_path = a.pathfind()

if astar_path is not None:
    plt.plot([p.x for p in astar_path], [p.y for p in astar_path], 'y-', marker='x', markersize=5, linewidth=1)
    plt.show()
    plt.pause(100)
else:
    print("A* failed!")
