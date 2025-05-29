import streamlit as st
import glob
import importlib.util
import os
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Geometric Structures Visualization",
    layout="wide"
)

# ------ Utility to load all graph modules ------
def load_graph_modules():
    graph_dir = 'graphs'
    graph_files = glob.glob(os.path.join(graph_dir, '*.py'))
    modules = {}
    for graph_file in graph_files:
        module_name = os.path.splitext(os.path.basename(graph_file))[0]
        spec = importlib.util.spec_from_file_location(module_name, graph_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Each module must have a function plot_<modulename>() (e.g., plot_convex_hull_2d)
        funcname = [n for n in dir(module) if n.startswith('plot_')][0]
        modules[module_name] = getattr(module, funcname)
    return modules

# ------ Load modules ------
graph_modules = load_graph_modules()
all_graphs = sorted(list(graph_modules.keys()), key=lambda x: x.lower())

# ------ Sidebar layout ------
with st.sidebar:
    st.title("Options")
    selected_graph = st.selectbox("Choose a geometric object", all_graphs)
    show_math_explanation = st.checkbox("Show Mathematical Explanation", value=True)
    show_math_properties = st.checkbox("Show Mathematical Properties", value=True)
    st.info("Choose a geometric object to visualize and optionally toggle the detailed math sections.")

st.markdown("<h1 style='text-align:center; margin-bottom:1.2em;'>Geometric Structures Visualization</h1>", unsafe_allow_html=True)

# ------ Main layout ------
col1, col2 = st.columns([1.4, 1])

# ---- Left Column: Graph and Basic Description ----
with col1:
    fig, description, math_explanation, math_properties = graph_modules[selected_graph]()
    st.subheader(f"{selected_graph.replace('_', ' ').title()} Visualization")
    st.pyplot(fig, use_container_width=True)
    st.markdown(f"**Description:**  {description}")

# ---- Right Column: Math ----
with col2:
    if show_math_explanation:
        st.subheader("Mathematical Explanation")
        st.markdown(math_explanation)
    if show_math_properties:
        st.subheader("Mathematical Properties")
        st.markdown(math_properties)

# ---- Optional: stylish divider ----
st.markdown("<hr style='margin:2em 0'>", unsafe_allow_html=True)

st.caption("Created with Streamlit • Author: Iheb Dridi")