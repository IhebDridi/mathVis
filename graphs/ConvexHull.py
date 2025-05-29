import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def plot_convexhull(color='blue', alpha=0.5):
    # Generate random points
    points = np.random.rand(30, 3)
    hull = ConvexHull(points)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'o')

    # Plot the convex hull
    for simplex in hull.simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], color=color)

    plt.title('Convex Hull')

    explanation = ("A convex hull is the smallest convex set that contains "
                   "a given set of points, forming a polyhedron that covers "
                   "all the points.")
    math_explanation = ("")

    return fig, explanation, math_explanation