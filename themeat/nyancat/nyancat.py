import tkinter as tk
from tkinter import PhotoImage
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def show_image():
    root = tk.Tk()
    root.title("Giffy")

    def changeimgonebyone():
        global inum
        if inum < 4:
            img_label.config(image=image_list[inum])
            inum += 1
        else:
            inum = 0  # Reset counter when reaching the end

        root.after(70, changeimgonebyone)  # Schedule the next call after 1000 milliseconds

    # Load the initial images using the resource_path function
    image_list = [
        PhotoImage(file=resource_path(f"./nyancat/frame_{i}_delay-0.1s.gif")) for i in range(4)
    ]
    # Create a label to display the image
    global img_label
    img_label = tk.Label(root, image=image_list[0], height = 1080, width = 1920, justify = 'center')
    img_label.pack()

    # Initialize inum before calling the changeimgonebyone function
    global inum
    inum = 0

    # Schedule the initial call of the changeimgonebyone function
    root.after(4, changeimgonebyone)
    root.attributes('-fullscreen', True)
    root.mainloop()

# Call the function to show the changing image
show_image()
