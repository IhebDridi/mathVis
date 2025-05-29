import matplotlib.pyplot as plt

def plot_polyhedralcone():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([0, 0], [0, 1], [0, 0], color='gray')
    ax.plot([0, 1], [0, 0], [0, 1], color='gray')
    ax.plot([0, 1], [0, 1], [0, 0], color='gray')
    plt.title('Polyhedral Cone')

    explanation = ("A polyhedral cone is defined by linear inequalities, "
                   "featuring directionality and extending infinitely.")


    math_explanation = (
    "Mathematical Explanation:\n\n"
    "A polyhedral cone is a convex cone defined as the intersection of finitely many linear half-spaces that all pass through the origin. "
    "Formally, for a matrix $A \\in \\mathbb{R}^{m \\times n}$, the polyhedral cone is:\n\n"
    "$$ C = \\{ x \\in \\mathbb{R}^n \\mid A x \\leq 0 \\} $$\n"
    "Polyhedral cones can also be described as the conical hull of finitely many vectors:\n"
    "$$ C = \\text{cone}(v_1, \\dots, v_k) $$\n"
    "where each element is a non-negative linear combination of the vectors $v_1, \\ldots, v_k$."
)

    math_properties = (
    "**Properties:**\n"
    "- Always convex and closed.\n"
    "- Bounded: No (except for the trivial cone $\{0\}$).\n"
    "- Generators: Finite set of rays/vectors (via conical hull) or as the intersection of a finite number of linear half-spaces through the origin.\n"
    "- May or may not be pointed (contains a line through $0$ or not).\n"
    "- Every polyhedral cone can be defined either by inequalities ($Ax \leq 0$) or generators."
)
    return fig, explanation, math_explanation, math_properties