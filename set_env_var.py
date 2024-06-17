import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Environment Variable Holder")
        self.create_widgets()

    def create_widgets(self):
        self.message_label = tk.Label(self.root, text="Environment variable OPENSSL_ia32cap is set. Close this window to unset it.")
        self.message_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
