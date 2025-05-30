import numpy as np
import matplotlib.pyplot as plt

def plot_convexcone():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    radius = np.linspace(0, 1, 100)
    angles = np.linspace(0, 2 * np.pi, 100)
    radius, angles = np.meshgrid(radius, angles)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    z = radius
    ax.plot_surface(x, y, z, alpha=0.5, color='cyan')
    plt.title('Convex Cone')

    explanation = ("A convex cone is a region formed by stretching vectors "
                   "out from a common point, and includes all non-negative "
                   "linear combinations of these vectors.")

    math_explanation = (
    "Mathematical Explanation:\n\n"
    "A convex cone $K$ in $\\mathbb{R}^n$ is a set closed under addition and multiplication by non-negative scalars:\n\n"
    "$$ \\forall x, y \\in K, \\forall \\alpha, \\beta \\geq 0, \\enspace \\alpha x + \\beta y \\in K $$\n"
    "Any conical hull is a convex cone, and the intersection of any collection of convex cones is a convex cone."
)

    math_properties = (
    "**Properties:**\n"
    "- Always convex by definition.\n"
    "- Bounded: No (except for $\{0\}$).\n"
    "- Generators: May be generated by rays (directions); in finite case, by a finite set of vectors.\n"
    "- Closed under non-negative scalar multiplication and addition.\n"
    "- The intersection of convex cones is also a convex cone.\n"
    "- The origin $0$ is always included."
)

    return fig, explanation, math_explanation, math_properties