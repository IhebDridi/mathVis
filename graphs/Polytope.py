import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_polytope():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    polytope_faces = [
        [vertices[0], vertices[1], vertices[2]],
        [vertices[0], vertices[1], vertices[3]],
        [vertices[0], vertices[2], vertices[3]],
        [vertices[1], vertices[2], vertices[3]]
    ]
    ax.add_collection3d(Poly3DCollection(polytope_faces, alpha=0.5, color='orange'))
    plt.title('Polytope')

    explanation = ("A polytope is a bounded polyhedron, representing the "
                   "convex hull of a finite set of points with flat faces.")

    math_explanation = ("")

    return fig, explanation, math_explanation