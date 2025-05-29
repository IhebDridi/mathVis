import tkinter as tk
import glob
import importlib.util
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Directory where the graph scripts are located
graph_dir = 'graphs'

window = tk.Tk()
window.title("Geometric Structures Visualization")

# Tracking current canvas and label
current_canvas = None
current_label = None

def load_and_create_buttons():
    graph_files = glob.glob(os.path.join(graph_dir, '*.py'))

    for graph_file in graph_files:
        module_name = os.path.splitext(os.path.basename(graph_file))[0]

        spec = importlib.util.spec_from_file_location(module_name, graph_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        plot_function_name = f"plot_{module_name.lower()}"
        plot_function = getattr(module, plot_function_name)

        button = tk.Button(window, text=module_name.capitalize(),
                           command=lambda func=plot_function: display_graph(func))
        button.pack()

def display_graph(plot_function):
    global current_canvas, current_label

    # Clear previous graph and description
    if current_canvas:
        current_canvas.get_tk_widget().pack_forget()
    if current_label:
        current_label.pack_forget()

    # Generate new graph and description
    fig, explanation = plot_function()
    current_canvas = FigureCanvasTkAgg(fig, master=window)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

    current_label = tk.Label(window, text=explanation, wraplength=400)
    current_label.pack()

load_and_create_buttons()

window.mainloop()