import streamlit as st
import glob
import importlib.util
import os
import matplotlib.pyplot as plt

graph_dir = 'graphs'

def load_graph_modules():
    graph_files = glob.glob(os.path.join(graph_dir, '*.py'))

    modules = {}
    for graph_file in graph_files:
        module_name = os.path.splitext(os.path.basename(graph_file))[0]
        spec = importlib.util.spec_from_file_location(module_name, graph_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        modules[module_name] = getattr(module, f"plot_{module_name.lower()}")

    return modules

def display_graph(plot_function, show_math_explanation):
    fig, description, math_explanation = plot_function()
    st.pyplot(fig)
    st.markdown(f"**Description:** {description}")
    if show_math_explanation:
        st.markdown(f"**Mathematical Explanation:** {math_explanation}")

def main():
    st.title("Geometric Structures Visualization")
    st.markdown("Select a graph to display:")

    graph_modules = load_graph_modules()
    selected_graph = st.selectbox("Choose a graph:", list(graph_modules.keys()))

    show_math_explanation = st.checkbox("Show Mathematical Explanation")

    if st.button("Display Graph"):
        display_graph(graph_modules[selected_graph], show_math_explanation)

    if st.button("Close Graph"):
        st.empty()

if __name__ == "__main__":
    main()