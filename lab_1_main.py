import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 1")

        self.controls_frame = ttk.Frame(self)
        self.controls_frame.grid(row=0, column=1)

        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.grid(row=0, column=0)

        self.canvas = tk.Canvas(self.canvas_frame, width=400, height=400, bg="white")
        self.canvas.pack()

        # # Відображення осей X та Y
        # self.canvas.create_line(0, 200, 400, 200, fill="black")  # Ось X
        # self.canvas.create_line(200, 0, 200, 400, fill="black")  # Ось Y
        #
        # # Приклад створення точки (3, 4)
        # x, y = 3, 4
        # self.canvas.create_oval(200 + x - 2, 200 - y - 2, 200 + x + 2, 200 - y + 2, fill="red")






if __name__ == "__main__":
    app = MainApp()
    app.mainloop()