from tkinter import filedialog as fd
from tkinter import *


def select_file(filetypes):

    root = Tk()
    root.update()
    filename = fd.askopenfilename(
        title="Open a file", initialdir="./", filetypes=filetypes
    )
    root.destroy()
    return filename
