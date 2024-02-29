import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import math


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 1")

        self.scale = 10

        self.controls_frame = ttk.Frame(self, borderwidth=2, relief="groove", padding=(10, 10, 10, 10))
        self.controls_frame.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))

        self.controls_separator = ttk.Separator(self, orient="vertical")
        self.controls_separator.grid(row=0, rowspan=10, column=1, sticky="ns")

        self.point_label = ttk.Label(self.controls_frame, text="Point:")
        self.point_label.grid(row=0, column=0, padx=(0, 5), pady=(0, 5))

        self.point_coords_frame = ttk.Frame(self.controls_frame)
        self.point_coords_frame.grid(row=1, column=0, columnspan=4)

        self.x_label = ttk.Label(self.point_coords_frame, text="X:")
        self.x_label.grid(row=0, column=0, padx=(0, 5), pady=(0, 5))
        self.x_entry = ttk.Entry(self.point_coords_frame, width=5)
        self.x_entry.grid(row=0, column=1, padx=(0, 5), pady=(0, 5))

        self.y_label = ttk.Label(self.point_coords_frame, text="Y:")
        self.y_label.grid(row=0, column=2, padx=(0, 5), pady=(0, 5))
        self.y_entry = ttk.Entry(self.point_coords_frame, width=5)
        self.y_entry.grid(row=0, column=3, padx=(0, 5), pady=(0, 5))

        self.point_separator = ttk.Separator(self.controls_frame, orient="horizontal")
        self.point_separator.grid(row=2, column=0, columnspan=5, sticky="ew", pady=(5, 10))

        self.side_length_label = ttk.Label(self.controls_frame, text="Side length:")
        self.side_length_label.grid(row=3, column=0, padx=(0, 5), pady=(0, 5))
        self.side_length_entry = ttk.Entry(self.controls_frame, width=5)
        self.side_length_entry.grid(row=3, column=1, padx=(0, 5), pady=(0, 5))

        self.side_lenght_separator = ttk.Separator(self.controls_frame, orient="horizontal")
        self.side_lenght_separator.grid(row=4, column=0, columnspan=5, sticky="ew", pady=(5, 5))

        self.colorpicker_frame = ttk.Frame(self.controls_frame)
        self.colorpicker_frame.grid(row=5, column=0, columnspan=5, pady=(5, 5))

        self.colorpicker_button = ttk.Button(self.colorpicker_frame, text="Pick fill color", command=self.choose_fill_color)
        self.colorpicker_button.grid(row=0, column=0)

        self.color_frame = tk.Frame(self.colorpicker_frame, width=12, height=12, bg="black")
        self.color_frame.grid(row=0, column=1, padx=(15, 0))

        self.colorpicker_separator = ttk.Separator(self.controls_frame, orient="horizontal")
        self.colorpicker_separator.grid(row=6, column=0, columnspan=5, sticky="ew", pady=(5, 5))

        self.fill_checkbutton = ttk.Checkbutton(self.controls_frame, text="Залити фігуру")
        self.fill_checkbutton.grid(row=7, column=0, columnspan=5, pady=(0, 5), sticky="w")

        self.inscribes_square = ttk.Checkbutton(self.controls_frame, text="Вписати квадрат")
        self.inscribes_square.grid(row=8, column=0, columnspan=5, pady=(0, 5), sticky="w")

        self.choices_separator = ttk.Separator(self.controls_frame, orient="horizontal")
        self.choices_separator.grid(row=9, column=0, columnspan=5, sticky="ew", pady=(5, 5))

        self.draw_button = ttk.Button(self.controls_frame, text="Draw", command=self.draw_triangle)
        self.draw_button.grid(row=10, column=0, columnspan=5)

        self.canvas_setup_frame = ttk.Frame(self, borderwidth=2, relief="groove", padding=(10, 10, 10, 10))
        self.canvas_setup_frame.grid(row=1, column=2, rowspan=6)

        self.clear_canvas_button = ttk.Button(self.canvas_setup_frame, text="Clear canvas", command=self.clear_canvas)
        self.clear_canvas_button.grid(row=0, column=0, padx=(0, 5), pady=(0, 5))

        self.angle_frame = ttk.Frame(self.canvas_setup_frame)
        self.angle_frame.grid(row=1, column=0, padx=(0, 5), pady=(0, 5))

        self.angle_label = ttk.Label(self.angle_frame, text="Angle:")
        self.angle_label.grid(row=0, column=0, padx=(0, 5), pady=(0, 5))
        self.angle_entry = ttk.Entry(self.angle_frame, width=5)
        self.angle_entry.grid(row=0, column=1, padx=(0, 5), pady=(0, 5))

        self.message = tk.Message(self.canvas_setup_frame, text="Вказуйте кут у градусах з метою повороту трикутника навколо його центру."
                                                                " За замовчуванням, трикутник відображається паралельно до осі координат.")
        self.message.grid(row=2, column=0, columnspan=2, padx=(0, 5), pady=(0, 5))

        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.grid(row=0, column=0, rowspan=6)

        self.canvas = tk.Canvas(self.canvas_frame, width=500, height=500, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.draw_axes()

    def canvas_to_cartesian(self, x, y):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        cartesian_x = (x - canvas_width / 2) / (self.scale * 2)  # Adjust scale as needed
        cartesian_y = (canvas_height / 2 - y) / (self.scale * 2)  # Adjust scale as needed
        return cartesian_x, cartesian_y

    def draw_axes(self):
        canvas_width = 500
        canvas_height = 500

        # Draw x-axis
        self.canvas.create_line(0, canvas_height / 2, canvas_width, canvas_height / 2, fill="black")
        # Draw y-axis
        self.canvas.create_line(canvas_width / 2, 0, canvas_width / 2, canvas_height, fill="black")

        # Add ticks and labels for x-axis
        for i in range(-10, 10):
            x = canvas_width / 2 + i * canvas_width / (self.scale * 2)
            self.canvas.create_line(x, canvas_height / 2 - 5, x, canvas_height / 2 + 5, fill="black")
            if i % 2 != 0:
                self.canvas.create_text(x, canvas_height / 2 + 10, text=str(i), anchor="n")

        self.canvas.create_text(canvas_width - 6, canvas_height / 2 - 25, text="X", anchor="n")

        # Add ticks and labels for y-axis
        for i in range(-10, 10):
            y = canvas_height / 2 - i * canvas_height / (self.scale * 2)
            self.canvas.create_line(canvas_width / 2 - 5, y, canvas_width / 2 + 5, y, fill="black")
            if i % 2 != 0:
                self.canvas.create_text(canvas_width / 2 - 15, y, text=str(i), anchor="e")

        self.canvas.create_text(canvas_width / 2 + 16, 3, text="Y", anchor="n")

        # Add arrows at the ends of the axes
        arrow_length = 8
        # Arrow on x-axis
        self.canvas.create_line(canvas_width - arrow_length, canvas_height / 2 - arrow_length,
                                canvas_width, canvas_height / 2, fill="black")
        self.canvas.create_line(canvas_width - arrow_length, canvas_height / 2 + arrow_length,
                                canvas_width, canvas_height / 2, fill="black")
        # Arrow on y-axis
        self.canvas.create_line(canvas_width / 2 - arrow_length, arrow_length,
                                canvas_width / 2, 0, fill="black")
        self.canvas.create_line(canvas_width / 2 + arrow_length, arrow_length,
                                canvas_width / 2, 0, fill="black")

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        cartesian_x, cartesian_y = self.canvas_to_cartesian(x, y)

        self.x_entry.delete(0, tk.END)
        self.x_entry.insert(0, f"{cartesian_x:.2f}")
        self.y_entry.delete(0, tk.END)
        self.y_entry.insert(0, f"{cartesian_y:.2f}")

        print("Canvas coordinates:", x, y)
        print("Cartesian coordinates:", cartesian_x, cartesian_y)

    def choose_fill_color(self):
        color = askcolor()
        self.color_frame.config(bg=color[1])

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw_axes()

    def get_user_choices(self):
        fill = self.fill_checkbutton.instate(['selected'])
        inscribes_square = self.inscribes_square.instate(['selected'])

        fill_color = self.color_frame.cget("bg")

        return fill, fill_color, inscribes_square

    def check_if_fig_visible(self, points):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        for point in points:
            x, y = point
            if not (0 <= x <= canvas_width and 0 <= y <= canvas_height):
                messagebox.showerror("Warning", "Triangle is partially or fully outside the visible range.")
                return False

        return True

    def validate_input(self):
        x = self.x_entry.get()
        y = self.y_entry.get()
        side = self.side_length_entry.get()
        angle = self.angle_entry.get()

        if not x or not y or not side:
            messagebox.showerror("Error", "All fields must be filled.")
            return False

        try:
            float(x)
            float(y)
            side = float(side)
            if len(angle):
                float(angle)
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")
            return False

        if side <= 0:
            messagebox.showerror("Error", "Side length must be a positive number.")
            return False

        return True

    def convert_to_canvas_coords(self, x, y):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        canvas_x = x * (self.scale * 2) + canvas_width / 2
        canvas_y = canvas_height / 2 - y * (self.scale * 2)
        return canvas_x, canvas_y

    def convert_to_canvas_x(self, x):
        canvas_width = self.canvas.winfo_width()
        return x * (self.scale * 2) + canvas_width / 2

    def convert_to_canvas_y(self, y):
        canvas_height = self.canvas.winfo_height()
        return canvas_height / 2 - y * (self.scale * 2)

    def draw_triangle(self):
        if not self.validate_input():
            return

        x, y = float(self.x_entry.get()), float(self.y_entry.get())
        side = float(self.side_length_entry.get())
        angle_degrees = float(self.angle_entry.get().strip()) if self.angle_entry.get().strip() else 0

        fill, fill_color, inscribes_square = self.get_user_choices()

        triangle_points = self.calculate_triangle_points(x, y, side, angle_degrees)

        # Draw triangle
        self.draw_polygon(triangle_points, fill_color, fill)

        if inscribes_square:
            # Draw inscribed square
            square_points = self.calculate_inscribed_square_points(x, y, side, angle_degrees)
            self.draw_polygon(square_points, fill_color, fill)

    def calculate_triangle_points(self, x, y, side, angle_degrees):
        x2, y2 = x + side, y
        x3, y3 = x + side / 2, y + side * math.sqrt(3) / 2

        points = [[x, y], [x2, y2], [x3, y3]]
        triangle_center = (x + side / 2, y + side * math.sqrt(3) / 6)
        return self.rotate(points, angle_degrees, triangle_center)

    def calculate_inscribed_square_points(self, x, y, side, angle_degrees):
        side_length = (2 * 3 ** 0.5 - 3) * side
        rect_x = x + (side - side_length) / 2
        rect_y = y
        rect_x2, rect_y2 = rect_x + side_length, rect_y
        rect_x3, rect_y3 = rect_x + side_length, rect_y + side_length
        rect_x4, rect_y4 = rect_x, rect_y + side_length

        square_points = [[rect_x, rect_y], [rect_x2, rect_y2], [rect_x3, rect_y3], [rect_x4, rect_y4]]
        triangle_center = (x + side / 2, y + side * math.sqrt(3) / 6)
        return self.rotate(square_points, angle_degrees, triangle_center)

    def draw_polygon(self, points, fill_color, fill):
        canvas_points = [self.convert_to_canvas_coords(x, y) for x, y in points]
        self.canvas.create_polygon(canvas_points, fill=fill_color if fill else '', outline='black')

        if len(canvas_points) == 3:
            if not self.check_if_fig_visible(canvas_points):
                return

    def rotate(self, points, angle, center):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
