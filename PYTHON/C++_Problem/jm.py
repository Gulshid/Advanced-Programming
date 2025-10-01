
from graphviz import Digraph

dfa = Digraph("DFA", format="png")
dfa.attr(rankdir="LR")

# States:
# q0 = start (no input yet)
# q1 = started with 'a', last seen 'a'
# q2 = started with 'a', last seen 'b'
# q3 = started with 'b', last seen 'a'
# q4 = started with 'b', last seen 'b'

states = ["q0", "q1", "q2", "q3", "q4"]
accept_states = ["q1", "q4"]  # start and end with same symbol

for state in states:
    if state in accept_states:
        dfa.attr("node", shape="doublecircle")
    else:
        dfa.attr("node", shape="circle")
    dfa.node(state)

# Start arrow
dfa.attr("node", shape="none")
dfa.node("")
dfa.edge("", "q0")

# Transitions
dfa.edge("q0", "q1", label="a")  # first symbol 'a'
dfa.edge("q0", "q4", label="b")  # first symbol 'b'

# From q1 (start=a, last=a)
dfa.edge("q1", "q1", label="a")  # still ends with a
dfa.edge("q1", "q2", label="b")  # now ends with b

# From q2 (start=a, last=b)
dfa.edge("q2", "q1", label="a")  # now ends with a
dfa.edge("q2", "q2", label="b")  # still ends with b

# From q4 (start=b, last=b)
dfa.edge("q4", "q4", label="b")  # still ends with b
dfa.edge("q4", "q3", label="a")  # now ends with a

# From q3 (start=b, last=a)
dfa.edge("q3", "q3", label="a")  # still ends with a
dfa.edge("q3", "q4", label="b")  # now ends with b

dfa.render("dfa_start_end_same_corrected", view=True)







# from graphviz import Digraph

# # Create DFA graph
# dfa = Digraph("DFA", format="png")
# dfa.attr(rankdir="LR")

# # States: q0 (start), q1, q2, q3 (accept), q4 (accept), q5 (accept), ...
# states = ["q0", "q1", "q2", "q3"]
# accept_states = ["q3"]




# # Add states
# for state in states:
#     if state in accept_states:
#         dfa.attr("node", shape="doublecircle")
#     else:
#         dfa.attr("node", shape="circle")
#     dfa.node(state)

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.edge("q0", "q1", label="0,1")
# dfa.edge("q1", "q2", label="0,1")
# dfa.edge("q2", "q3", label="0,1")
# dfa.edge("q3", "q3", label="0,1")  # loop to stay in accepting state

# # Save and render
# dfa.render("dfa_length_ge3", view=True)


# import graphviz
# import os

# # Create DFA diagram
# dfa = graphviz.Digraph(format="png")
# dfa.attr(rankdir="LR", size="8")

# # Nodes
# dfa.attr("node", shape="doublecircle")
# dfa.node("q2")  # Accepting state

# dfa.attr("node", shape="circle")
# dfa.node("q0")  # Start state
# dfa.node("q1")  # Seen 'a'

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.attr("node", shape="circle")
# dfa.edge("q0", "q1", label="a")
# dfa.edge("q0", "q0", label="b")
# dfa.edge("q1", "q1", label="a")
# dfa.edge("q1", "q2", label="b")
# dfa.edge("q2", "q2", label="a,b")

# # Save and open automatically (macOS)
# output_path = dfa.render("dfa_contains_ab", format="png", cleanup=True)
# os.system(f"open {output_path}")  # use "xdg-open" on Linux, "start" on Windows


# import graphviz
# import os

# # Create DFA diagram
# dfa = graphviz.Digraph(format="png")
# dfa.attr(rankdir="LR", size="8")

# # Nodes
# dfa.attr("node", shape="doublecircle")
# dfa.node("q2")  # Accepting state (ends with 01)

# dfa.attr("node", shape="circle")
# dfa.node("q0")  # Start state
# dfa.node("q1")  # Last was 0

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.attr("node", shape="circle")
# dfa.edge("q0", "q1", label="0")
# dfa.edge("q0", "q0", label="1")
# dfa.edge("q1", "q1", label="0")
# dfa.edge("q1", "q2", label="1")
# dfa.edge("q2", "q1", label="0")
# dfa.edge("q2", "q0", label="1")

# # Save and open automatically (macOS/Linux)
# output_path = dfa.render("dfa_ending_with_01", format="png", cleanup=True)
# os.system(f"open {output_path}")  # Use "xdg-open" for Linux, "start" for Windows


# import graphviz
# import os

# # Create DFA diagram
# dfa = graphviz.Digraph(format="png")
# dfa.attr(rankdir="LR", size="8")

# # Nodes
# dfa.attr("node", shape="doublecircle")
# dfa.node("q1")  # final state

# dfa.attr("node", shape="circle")
# dfa.node("q0")  # Start state
# dfa.node("q2")  # Dead state

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.attr("node", shape="circle")
# dfa.edge("q0", "q1", label="a")
# dfa.edge("q0", "q2", label="b")
# dfa.edge("q1", "q1", label="a,b")
# dfa.edge("q2", "q2", label="a,b")

# # Save and get file path
# output_path = dfa.render("dfa_starting_with_a", format="png", cleanup=True)

# # Open automatically in Preview (macOS)
# os.system(f"open {output_path}")


# import graphviz
# import os

# # Create DFA diagram
# dfa = graphviz.Digraph(format="png")
# dfa.attr(rankdir="LR", size="8")

# # Nodes
# dfa.attr("node", shape="doublecircle")
# dfa.node("q1")  # Accepting state (ends with a)

# dfa.attr("node", shape="circle")
# dfa.node("q0")  # Start state
# dfa.node("q2")  # Non-accepting (ends with b)

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.attr("node", shape="circle")
# dfa.edge("q0", "q1", label="a")
# dfa.edge("q0", "q2", label="b")
# dfa.edge("q1", "q1", label="a")
# dfa.edge("q1", "q2", label="b")
# dfa.edge("q2", "q1", label="a")
# dfa.edge("q2", "q2", label="b")

# # Save and open automatically (macOS)
# output_path = dfa.render("dfa_ending_with_a", format="png", cleanup=True)
# os.system(f"open {output_path}")


# import graphviz
# import os

# # Create DFA diagram
# dfa = graphviz.Digraph(format="png")
# dfa.attr(rankdir="LR", size="8")

# # Nodes
# dfa.attr("node", shape="doublecircle")
# dfa.node("q1")  # Accepting state (strings starting with b)

# dfa.attr("node", shape="circle")
# dfa.node("q0")  # Start state
# dfa.node("q2")  # Dead state (if starts with a)

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.attr("node", shape="circle")
# dfa.edge("q0", "q1", label="b")  # first symbol b → accept
# dfa.edge("q0", "q2", label="a")  # first symbol a → dead

# dfa.edge("q1", "q1", label="a,b")  # once accepted, always accepted
# dfa.edge("q2", "q2", label="a,b")  # stuck in dead state

# # Save and open automatically (macOS)
# output_path = dfa.render("dfa_starting_with_b", format="png", cleanup=True)
# os.system(f"open {output_path}")


# import graphviz
# import os

# # Create DFA diagram
# dfa = graphviz.Digraph(format="png")
# dfa.attr(rankdir="LR", size="8")

# # Accepting states
# dfa.attr("node", shape="doublecircle")
# dfa.node("q2")  # Accepting state (starts with a and ends with b)

# # Other states
# dfa.attr("node", shape="circle")
# dfa.node("q0")  # Start
# dfa.node("q1")  # After starting with a
# dfa.node("qd")  # Dead state

# # Start arrow
# dfa.attr("node", shape="none")
# dfa.node("")
# dfa.edge("", "q0")

# # Transitions
# dfa.edge("q0", "q1", label="a")      # first must be a
# dfa.edge("q0", "qd", label="b")      # if starts with b → dead

# dfa.edge("q1", "q1", label="a")      # middle part with a’s
# dfa.edge("q1", "q2", label="b")      # move to accepting if last seen b

# dfa.edge("q2", "q1", label="a")      # if a comes after b → not accepting yet
# dfa.edge("q2", "q2", label="b")      # stays accepting on b

# # Dead state loops
# dfa.edge("qd", "qd", label="a,b")

# # Save and open
# output_path = dfa.render("dfa_starting_a_ending_b", format="png", cleanup=True)
# os.system(f"open {output_path}")



