import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data for the graph
x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 1]

# Create the main Tkinter window
root = tk.Tk()
root.title("Graph Example")

# Create a Matplotlib figure and plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sample Graph")

# Embed the Matplotlib figure into a Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Run the main loop (keeps the window open)
root.mainloop()
