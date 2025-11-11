import tkinter as tk

class Node:
    def __init__(self,  key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def RR(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def LR(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # No duplicates

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance factor
        balance = self.get_balance(root)

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.RR(root)
        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.LR(root)
        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.LR(root.left)
            return self.RR(root)
        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.RR(root.right)
            return self.LR(root)

        return root

class AVLVisualizer:
    def __init__(self, window):
        self.window = window
        self.window.title("AVL Tree Visualizer")
        self.window.geometry("900x600")
        self.window.configure(bg="white")

        self.tree = AVL()
        self.root = None

        # Entry
        self.entry = tk.Entry(self.window, width=15, font=('Arial', 14))
        self.entry.pack(pady=10)

        # Insert Button
        self.insert_button = tk.Button(self.window,
                                text="Insert", command=self.insert_value,
                                font=("Arial", 12), bg="#4CAF50", fg="black")
        self.insert_button.pack(pady=5)

        # Canvas for drawing the tree
        self.canvas = tk.Canvas(self.window, width=880, height=480, bg="white", highlightthickness=1,
                                highlightbackground="gray")
        self.canvas.pack(pady=10)

        # Label for messages
        self.status = tk.Label(self.window, text="Enter a number and click Insert", font=('Arial', 12), bg="white")
        self.status.pack()

        # Function to handle inserting values

    def insert_value(self):
        value = self.entry.get().strip()

        # Validate input
        if not value.lstrip('-').isdigit():
            self.status.config(text="Please enter a valid integer.", fg="red")
            return

        key = int(value)
        self.root = self.tree.insert(self.root, key)
        self.entry.delete(0, tk.END)
        self.status.config(text=f"Inserted {key} into the BST.", fg="green")

        # Redraw tree after insertion
        self.redraw_tree()

        # Recursive function to draw the tree

    def draw_tree(self, node, x, y, x_offset):
        if node is not None:
            # Draw left child and connecting line
            if node.left:
                self.canvas.create_line(x, y, x - x_offset, y + 80, fill="gray", width=2)
                self.draw_tree(node.left, x - x_offset, y + 80, x_offset / 1.8)

            # Draw right child and connecting line
            if node.right:
                self.canvas.create_line(x, y, x + x_offset, y + 80, fill="gray", width=2)
                self.draw_tree(node.right, x + x_offset, y + 80, x_offset / 1.8)

            # Draw node (circle)
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#4CAF50", outline="black", width=2)
            self.canvas.create_text(x, y, text=str(node.key), fill="white", font=('Arial', 12, 'bold'))

        # Function to refresh the canvas

    def redraw_tree(self):
        self.canvas.delete("all")
        if self.root:
            self.draw_tree(self.root, 450, 50, 200)
        else:
            self.status.config(text="Tree is empty.", fg="black")

if __name__ == "__main__":
    window = tk.Tk()
    app = AVLVisualizer(window)
    window.mainloop()
