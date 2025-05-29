import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_polyhedron():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    ax.add_collection3d(Poly3DCollection(
        [[vertices[0], vertices[1], vertices[2]],
         [vertices[0], vertices[1], vertices[3]],
         [vertices[0], vertices[2], vertices[3]],
         [vertices[1], vertices[2], vertices[3]]],
        alpha=0.5, color='blue'))
    plt.title('Polyhedron')

    explanation = ("A polyhedron is a flat-faced solid bounded by polygons, "
                   "ideal for representing feasible regions in optimization.")
    math_explanation = (
    "Mathematical Explanation:\n\n"
    "A polyhedron in $\\mathbb{R}^n$ is the solution set of a finite system of linear inequalities (and possibly equalities):\n\n"
    "$$ P = \\{ x \\in \\mathbb{R}^n \\mid A x \\leq b \\} $$\n"
    "where $A$ is a real $m \\times n$ matrix and $b \\in \\mathbb{R}^m$.\n\n"
    "A polyhedron may be bounded (then it is a polytope), or unbounded.\n"
    "Each face (of any dimension) of a polyhedron is itself a polyhedron."
)

    return fig, explanation, math_explanation