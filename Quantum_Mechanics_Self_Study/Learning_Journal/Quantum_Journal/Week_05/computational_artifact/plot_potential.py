## Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# --- Define the Parameters of the Finite Potential Well ---
# We will set the potential V0 to be 10 (in some arbitrary units of energy)
# and the width of the well 'a' to be 2 (from -1 to 1).
V0 = 10
a = 1

# --- Create the x-axis values ---
# We will plot from -3 to 3 to see the area outside the well.
# np.linspace creates 400 points evenly spaced between -3 and 3.
x = np.linspace(-3, 3, 400)

# --- Define the Potential Function V(x) ---
# We create a list to hold the potential values for each x.
potential = []
for position in x:
    if -a <= position <= a:
        # Inside the well, the potential is 0
        potential.append(0)
    else:
        # Outside the well, the potential is V0
        potential.append(V0)

# --- Create the Plot ---
plt.figure(figsize=(8, 6)) # Set the figure size

# Plot the potential V(x) against the position x
plt.plot(x, potential, linewidth=2, color='blue')

# --- Add Labels and Title for a Professional Look ---
plt.title('The Finite Potential Well', fontsize=16)
plt.xlabel('Position (x)', fontsize=12)
plt.ylabel('Potential Energy V(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) # Add a grid for readability
plt.ylim(-1, V0 + 5) # Set the y-axis limits to make the plot look good

# --- Save the plot to a file ---
# In Datacamp, you can download this file after it's created.
plt.savefig('finite_well_potential.png')

# --- Show the plot ---
plt.show()
