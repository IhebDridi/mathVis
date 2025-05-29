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

    math_explanation = ("")

    return fig, explanation, math_explanation