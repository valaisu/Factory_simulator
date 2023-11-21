import tkinter as tk
from tkinter import messagebox


class RecipeManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Manager")
        self.master.geometry("800x600")

        self.menu_bar = tk.Menu(self.master)

        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit) # At some point add some save feature here
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Recipe Menu
        recipe_menu = tk.Menu(self.menu_bar, tearoff=0)
        recipe_menu.add_command(label="Add Recipe", command=self.add_recipe)
        recipe_menu.add_command(label="View Recipes", command=self.view_recipes)
        recipe_menu.add_command(label="Edit Recipes", command=self.edit_recipes)
        self.menu_bar.add_cascade(label="Recipes", menu=recipe_menu)

        self.master.config(menu=self.menu_bar)

        # Create a Canvas widget
        self.canvas = tk.Canvas(self.master, width=800, height=550, bg="white")
        self.canvas.pack()

        # Create a frame at the bottom
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create buttons in the frame
        self.add_square_button = tk.Button(self.bottom_frame, text="Add Square", command=self.add_square)
        self.add_square_button.pack(side=tk.LEFT, padx=10, pady=10)

        button2 = tk.Button(self.bottom_frame, text="Button 2", command=self.nothing)
        button2.pack(side=tk.LEFT, padx=10, pady=10)
        button3 = tk.Button(self.bottom_frame, text="Button 3", command=self.nothing)
        button3.pack(side=tk.LEFT, padx=10, pady=10)


    def add_square(self):
        square_size = 100
        x = (800 - square_size) // 2
        y = (500 - square_size) // 2
        self.canvas.create_rectangle(x, y, x + square_size, y + square_size, fill="blue")

    def nothing(self):
        pass

    def add_recipe(self):
        messagebox.showinfo("Add Recipe", "Functionality for adding recipes will be implemented here.")

    def view_recipes(self):
        messagebox.showinfo("View Recipes", "Functionality for viewing recipes will be implemented here.")

    def edit_recipes(self):
        messagebox.showinfo("Edit Recipes", "Functionality for editing recipes will be implemented here.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeManagerApp(root)
    root.mainloop()
