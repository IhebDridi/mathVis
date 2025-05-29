import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None
plot_label = None

# Function to clear previous plots and labels
def clear_canvas():
    global canvas, plot_label
    if canvas:
        canvas.get_tk_widget().pack_forget()
        canvas = None
    if plot_label:
        plot_label.pack_forget()
        plot_label = None

# Function to show plot in Tkinter window
def show_plot(fig, explanation):
    global canvas, plot_label
    clear_canvas()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plot_label = tk.Label(window, text=explanation, wraplength=400)
    plot_label.pack()

# Function to plot a convex cone
def plot_convex_cone():
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
    show_plot(fig, explanation)

# Function to plot a polytope
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
    show_plot(fig, explanation)

# Function to plot a polyhedral cone
def plot_polyhedral_cone():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([0, 0], [0, 1], [0, 0], color='gray')
    ax.plot([0, 1], [0, 0], [0, 1], color='gray')
    ax.plot([0, 1], [0, 1], [0, 0], color='gray')
    plt.title('Polyhedral Cone')
    explanation = ("A polyhedral cone is defined by linear inequalities, "
                   "featuring directionality and extending infinitely.")
    show_plot(fig, explanation)

# Function to plot a polyhedron
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
    show_plot(fig, explanation)

# Tkinter window setup
window = tk.Tk()
window.title("Geometric Structures Visualization")

# Buttons
button_cone = tk.Button(window, text="Convex Cone", command=plot_convex_cone)
button_cone.pack()

button_polytope = tk.Button(window, text="Polytope", command=plot_polytope)
button_polytope.pack()

button_polyhedral_cone = tk.Button(window, text="Polyhedral Cone", command=plot_polyhedral_cone)
button_polyhedral_cone.pack()

button_polyhedron = tk.Button(window, text="Polyhedron", command=plot_polyhedron)
button_polyhedron.pack()

# Run the GUI main loop
window.mainloop()