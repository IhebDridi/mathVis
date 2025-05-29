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

    math_explanation = ("")

    return fig, explanation, math_explanation