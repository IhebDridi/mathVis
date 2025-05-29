import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def plot_convexhull2d():
    # Generate random 2D points
    points = np.random.rand(30, 2)
    hull = ConvexHull(points)

    fig, ax = plt.subplots()
    ax.plot(points[:, 0], points[:, 1], 'o', color='grey')

    for simplex in hull.simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], 'k-', linewidth=2)

    plt.title('2D Convex Hull')

    description = ("The convex hull is the smallest convex boundary that "
                   "encloses a set of points, forming a convex polygon "
                   "with outer points as vertices.")

    # Mathematical explanation with corrected LaTeX notation
    math_explanation = (
        "Mathematical Explanation:\n\n"
        "Given a set of points $X$ in a Euclidean space, the convex hull $\\text{conv}(X)$ "
        "is defined as the intersection of all convex sets containing $X$. "
        "It is the smallest convex set that can envelop the points.\n\n"
        "Mathematically, for a finite set of points in $\\mathbb{R}^n$, "
        "the convex hull can be expressed as:\n\n"
        "$$ \\text{conv}(X) = \\left\\{ \\sum_{i=1}^{m} \\lambda_i x_i \\mid \\sum_{i=1}^{m} \\lambda_i = 1, \\lambda_i \\geq 0 \\right\\} $$\n"
        "where $x_i \\in X$ are the given points, and $\\lambda_i$ are non-negative scalars representing weights.\n\n"
        "This set is always convex, meaning for any two points within the hull,"
        "the line segment joining them is entirely contained within the set."
    )

    return fig, description, math_explanation