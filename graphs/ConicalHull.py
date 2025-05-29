import numpy as np
import matplotlib.pyplot as plt

def plot_conicalhull(color='magenta', alpha=0.5):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Generate points for conical hull
    r = np.linspace(0, 1, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    R, PHI = np.meshgrid(r, phi)
    X = R * np.cos(PHI)
    Y = R * np.sin(PHI)
    Z = R
    ax.plot_surface(X, Y, Z, color=color, alpha=alpha)
    plt.title('Conical Hull')

    explanation = ("A conical hull is the set of all non-negative linear "
                   "combinations of a set of vectors, forming a cone that "
                   "extends indefinitely from the origin.")

    math_explanation = (
    "Mathematical Explanation:\n\n"
    "Given a set of vectors $X = \\{x_1, x_2, \\dots, x_m\\}$ in $\\mathbb{R}^n$, "
    "the conical hull (also called the convex cone) is the set of all non-negative linear "
    "combinations of these vectors. That is:\n\n"
    "$$ \\text{cone}(X) = \\left\\{ \\sum_{i=1}^m \\lambda_i x_i \\mid \\lambda_i \\geq 0 \\right\\} $$\n"
    "Here, $\\lambda_i$ are non-negative real scalars. "
    "The conical hull thus forms a (possibly infinite) cone with apex at the origin (if the vectors start at 0).\n\n"
    "If the $x_i$'s are linearly independent, the cone is 'pointed'; if all $\\lambda_i \\leq 0$, it's just the origin."
)

    return fig, explanation, math_explanation