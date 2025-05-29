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

    math_explanation = (
    "Mathematical Explanation:\n\n"
    "A polytope in $\\mathbb{R}^n$ is the convex hull of a finite set of points. More formally:\n\n"
    "$$ P = \\text{conv}(\\{v_1, \\dots, v_k\\}) = \\left\\{ \\sum_{i=1}^k \\lambda_i v_i \\mid \\lambda_i \\geq 0, \\sum_{i=1}^k \\lambda_i = 1 \\right\\} $$\n"
    "where $v_i \\in \\mathbb{R}^n$ are the vertices of the polytope, and $\\lambda_i$ are non-negative real numbers.\n\n"
    "Alternatively, a polytope can be defined as the bounded solution set to a finite system of linear inequalities:\n"
    "$$ P = \\{ x \\in \\mathbb{R}^n \\mid A x \\leq b \\} $$\n"
    "if $P$ is bounded. Every polytope is both convex and bounded."
)

    math_properties = (
    "**Properties:**\n"
    "- Always convex.\n"
    "- Bounded: Yes.\n"
    "- Generators: Vertices (finite list of points); all other points are convex combinations of these.\n"
    "- Has finite vertices, edges, and faces.\n"
    "- The intersection of finitely many half-spaces, if bounded, is a polytope.\n"
    "- Is a special case of a polyhedron."
)
    return fig, explanation, math_explanation, math_properties