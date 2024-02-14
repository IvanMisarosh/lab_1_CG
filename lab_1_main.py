import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 1")

        self.controls_frame = ttk.Frame(self)
        self.controls_frame.grid(row=0, column=1)

        self.point_label = ttk.Label(self.controls_frame, text="Point:")
        self.point_label.grid(row=0, column=0)

        self.x_label = ttk.Label(self.controls_frame, text="X:")
        self.x_label.grid(row=0, column=1)
        self.x_entry = ttk.Entry(self.controls_frame, width=5)
        self.x_entry.grid(row=0, column=2)

        self.y_label = ttk.Label(self.controls_frame, text="Y:")
        self.y_label.grid(row=0, column=3)
        self.y_entry = ttk.Entry(self.controls_frame, width=5)
        self.y_entry.grid(row=0, column=4)

        self.side_length_label = ttk.Label(self.controls_frame, text="Side length:")
        self.side_length_label.grid(row=1, column=0, columnspan=2)
        self.side_length_entry = ttk.Entry(self.controls_frame, width=5)
        self.side_length_entry.grid(row=1, column=1, columnspan=4)

        self.figures = tk.StringVar()
        self.triangle = ttk.Radiobutton(self.controls_frame, text="Triangle", variable=self.figures, value="triangle", command=self.figure_select)
        self.triangle.grid(row=2, column=0, columnspan=5)

        self.draw_button = ttk.Button(self.controls_frame, text="Draw")
        self.draw_button.grid(row=3, column=0, columnspan=5)

        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.grid(row=0, column=0)

        self.fig, self.ax = plt.subplots()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.configure_plot()
        self.canvas.get_tk_widget().pack()

    def configure_controls(self):
        pass

    def configure_plot(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        ticks_frequency = 1
        self.ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')

        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

    def figure_select(self):
        option = self.figures.get()





if __name__ == "__main__":
    app = MainApp()
    app.mainloop()