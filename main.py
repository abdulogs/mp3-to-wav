from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

selectedFolder = ""
selectedFile = ""
selectedFormat = ".wav"


def selectFormat(val):
    global selectedFormat
    selectedFormat = val


def selectFolder():
    global selectedFolder
    folder = filedialog.askdirectory()
    selectedFolder = folder


def selectFile():
    global selectedFile
    file = filedialog.askopenfilename(
        initialdir="/", title="Select audio", filetypes=(("Audio files", "*.mp3*"), ("all files", "*.*")))
    selectedFile = file


def convert():
    global selectedFile, selectedFormat, selectedFolder
    if selectedFormat == "":
        messagebox.showwarning("Missing information",
                               "Conversion format is required")
    elif selectedFolder == "":
        messagebox.showwarning("Missing information",
                               "Folder for conversion is required")
    elif selectedFile == "":
        messagebox.showwarning("Missing information", "File is required")
    else:
        filename = os.path.basename(selectedFile)
        filename = filename.replace(".mp3", selectedFormat)
        filename = selectedFolder + "/" + filename
        try:
            sound = AudioSegment.from_mp3(selectedFile)
            sound.export(filename, format=selectedFormat.replace(".", ""))
            messagebox.showinfo(
                f'mp3 to {selectedFormat.replace(".", "")} conversion', "Converted successfully")
        except:
            messagebox.askretrycancel("askretrycancel", "Try again?")


# Create the root window
window = tk.Tk()
# Set window title
window.title('Mp3 converter')
# Set window size
window.geometry("500x200")
# Set window background color
window.config(background="white")
# Create file explorer button


format = tk.StringVar(window)
format.set(".wav")

tk.Label(window, text="Choose format",  bg='#ffffff', width=40, anchor='w').grid(row=1, column=1, pady=(10, 10), padx=(10, 10))
tk.OptionMenu(window, format, ".wav", ".aac", ".aiff", command=selectFormat).grid(row=1, column=2)

tk.Label(window, text="Choose folder",  bg='#ffffff',  width=40, anchor='w').grid(row=2, column=1, pady=(10, 10), padx=(10, 10))
tk.Button(window, text="Choose", command=selectFolder).grid(row=2, column=2)

tk.Label(window, text="Choose file",  bg='#ffffff', width=40, anchor='w').grid(row=3, column=1, pady=(10, 10), padx=(10, 10))
tk.Button(window, text="Browse", command=selectFile).grid(row=3, column=2)

tk.Button(window, text="Convert audio", command=convert).grid(row=4, column=1)

window.mainloop()
