from prm import Graph
from obstacle import EndArea, Obstacle
from utils import Point as P
from matplotlib import pyplot as plt

# Define all the obstables
obs = [ Obstacle((P(600, 700), P(700, 600), P(700, 700))) ]

# Define the end area
end = EndArea((P(700, 700), P(750, 700), P(750, 750), P(700, 750)))

g = Graph(P(500, 500), obs, end, (P(0, 0), P(1000, 1000)))

g.sample(200)

plottables = g.get_plottable()
plottables += [o.get_plottable() for o in g.obstacles]
plottables.append(end.get_plottable())

plt.ion()
[plt.plot(*p, marker='.', markersize=1, linewidth=0.1) for p in plottables]
plt.show()
plt.pause(100)
