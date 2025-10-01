
import graphviz
import os

# Create DFA diagram
dfa = graphviz.Digraph(format="png")
dfa.attr(rankdir="LR", size="8")

# Nodes
dfa.attr("node", shape="doublecircle")
dfa.node("q1")  # final state

dfa.attr("node", shape="circle")
dfa.node("q0")  # Start state
dfa.node("q2")  # Dead state

# Start arrow
dfa.attr("node", shape="none")
dfa.node("")
dfa.edge("", "q0")

# Transitions
dfa.attr("node", shape="circle")
dfa.edge("q0", "q1", label="a")
dfa.edge("q0", "q2", label="b")
dfa.edge("q1", "q1", label="a,b")
dfa.edge("q2", "q2", label="a,b")

# Save and get file path
output_path = dfa.render("dfa_starting_with_a", format="png", cleanup=True)

# Open automatically in Preview (macOS)
os.system(f"open {output_path}")


import graphviz
import os

# Create DFA diagram
dfa = graphviz.Digraph(format="png")
dfa.attr(rankdir="LR", size="8")

# Nodes
dfa.attr("node", shape="doublecircle")
dfa.node("q1")  # Accepting state (ends with a)

dfa.attr("node", shape="circle")
dfa.node("q0")  # Start state
dfa.node("q2")  # Non-accepting (ends with b)

# Start arrow
dfa.attr("node", shape="none")
dfa.node("")
dfa.edge("", "q0")

# Transitions
dfa.attr("node", shape="circle")
dfa.edge("q0", "q1", label="a")
dfa.edge("q0", "q2", label="b")
dfa.edge("q1", "q1", label="a")
dfa.edge("q1", "q2", label="b")
dfa.edge("q2", "q1", label="a")
dfa.edge("q2", "q2", label="b")

# Save and open automatically (macOS)
output_path = dfa.render("dfa_ending_with_a", format="png", cleanup=True)
os.system(f"open {output_path}")
