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
        st.markdown("---")
        st.markdown(f"### Mathematical Explanation")
        st.latex(math_explanation.lstrip('Mathematical Explanation:\n\n'))  # show main formula in latex
        st.markdown(math_explanation)    # fallback: show full explanation (with equations in Markdown if more text)

def main():
    st.set_page_config(
        page_title="Geometric Structures Visualization",
        layout="wide"
    )

    st.markdown(
        "<h1 style='text-align: center;'>Geometric Structures Visualization</h1>",
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.header("Options")
        graph_modules = load_graph_modules()
        selected_graph = st.selectbox("Choose a geometric object", list(graph_modules.keys()))
        show_math_explanation = st.checkbox("Show Mathematical Explanation", value=True)

        st.info("Select the geometric object to visualize. Toggle the box to view the mathematical formulation.")

    st.write("")
    st.write("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(f"{selected_graph.replace('_', ' ')} Visualization")
        fig, description, math_explanation = graph_modules[selected_graph]()
        st.pyplot(fig, use_container_width=True)
        st.write(description)
    with col2:
        if show_math_explanation:
            st.subheader("Mathematical Explanation")
            # Show only the latex block if it exists, otherwise show full text
            # (You may refine how you extract main latex formula from your math_explanation string)
            st.markdown(math_explanation)

if __name__ == "__main__":
    main()