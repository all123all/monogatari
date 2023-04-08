import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog, colorchooser


def new_file():
    global text_widget, file_name
    text_widget.delete("1.0", tk.END)
    file_name = None


def save_file():
    global file_name
    if file_name is None:
        file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_name:
        with open(file_name, "w") as f:
            f.write(text_widget.get("1.0", tk.END))


def save_file_as():
    global text_widget
    file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_name:
        with open(file_name, "w") as f:
            f.write(text_widget.get("1.0", tk.END))


def open_file():
    global text_widget, file_name
    file_name = filedialog.askopenfilename(defaultextension=".txt")
    if file_name:
        with open(file_name, "r") as f:
            text_widget.delete("1.0", tk.END)
            text_widget.insert("1.0", f.read())


def change_background_color():
    global text_widget
    color = colorchooser.askcolor()[1]
    if color:
        text_widget.configure(background=color)


def on_close():
    global text_widget, file_name
    if text_widget.edit_modified():
        save_changes = messagebox.askyesnocancel(
            "Save Changes", "Do you want to save changes to the file?")
        if save_changes is None:
            return
        elif save_changes:
            save_file()
    root.destroy()

def change_font_size():
    global text_widget
    font_size = simpledialog.askinteger("Font Size", "Enter the font size:")
    if font_size:
        text_widget.configure(font=("TkDefault", font_size))

root = tk.Tk()
root.title("MONOGATARI - Text Editor")
root.geometry("500x500")
root.configure(background="#000000")

text_widget = tk.Text(
    root, undo=True, background="#000000", foreground="#FFFFFF")
text_widget.pack(fill=tk.BOTH, expand=True)
text_widget.config(insertbackground="white")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
options_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
""" file_menu.add_separator()
file_menu.add_command(label="Change Background Color",
                      command=change_background_color) """
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_close)
options_menu.add_command(label="Background", command=change_background_color)
options_menu.add_command(label="Font Size", command=change_font_size)
options_menu.add_command(label="Mystery", command=print("What's next?"))
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Customize", menu=options_menu)
root.config(menu=menu_bar)

file_name = None

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
