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
    math_explanation = (
    "Let $X = \\{x_1, x_2, \\ldots, x_m\\} \\subseteq \\mathbb{R}^n$ be a finite set of points. "
    "The **convex hull** of $X$, denoted $\\mathrm{conv}(X)$, is defined as the intersection of all convex sets containing $X$. "
    "Equivalently, it is the set of all convex combinations of the points in $X$:\n\n"
    "$$ "
    "\\mathrm{conv}(X) = \\left\\{ \\sum_{i=1}^{m} \\lambda_i x_i : "
    "\\lambda_i \\geq 0, \\ \\sum_{i=1}^m \\lambda_i = 1 \\right\\} "
    "$$\n\n"
    "Here, $\\lambda_i$ are non-negative scalars (called **weights**) that sum to 1. "
    "This means every point in the convex hull can be expressed as a weighted average of the original points.\n\n"
    "Geometrically, the convex hull is the smallest convex set that contains $X$. In $\\mathbb{R}^2$ (the plane), "
    "it corresponds to wrapping a rubber band around the outermost points; the band then traces out the convex hull boundary.\n\n"
    "**Property:** The convex hull of $X$ is always convex: For any two points $y, z \\in \\mathrm{conv}(X)$, the line segment between $y$ and $z$ also lies entirely within $\\mathrm{conv}(X)$."
)

    return fig, explanation, math_explanation