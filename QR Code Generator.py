import qrcode
import os, sys
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox


# _______________EXE_File_Convietion_Funtion________________
def resource_path(relative_path):
    try:
        # Pylnstaller creates a temp folder and stores path in MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ________________Engine___________________
def Generate_QR():
    data = text_entry.get()

    if data:
        img = qrcode.make(data)  # QR Code
        resized_img = img.resize((280, 250))
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showinfo("Sorry you enter same data again")

    text_entry.focus()


def Save_QR():
    data = text_entry.get()

    if data:
        img = qrcode.make(data)  # QR Code
        resized_img = img.resize((280, 250))

        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Your QR Code is successfully saved")
    else:
        messagebox.showinfo("Sorry you enter same data again")


    text_entry.focus()

def Exit_QR():
    result = messagebox.askyesno("Do you want to exit")
    if result:
        window.destroy()

def Clier_Text():
    text_entry.delete(0, END)
    text_entry.focus()


# _________GUI_MODULE___________

window = tk.Tk()
window.title('QR Code Generator')
window.geometry("300x400")
window.config(bg='White')
# window.resizable(0, 0)

# Frame
frame1 = tk.Frame(window, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=0, width=280, height=250)

frame2 = tk.Frame(window, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=260, width=280, height=120)

# Logo/QR Code Display
cover_img = tk.PhotoImage(file=resource_path("QRlogo.png"))

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0, 0, anchor=tk.NW, image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>", Save_QR)
qr_canvas.pack(fill=tk.BOTH)

# Entry
text_entry = ttk.Entry(frame2, width=24, font=('Sitka Small', 12), justify=tk.CENTER)
text_entry.bind("Return", Generate_QR)
text_entry.place(x=4, y=5)
text_entry.focus()

# Button
button_1 = ttk.Button(frame2, text="Generate", width=10, command=Generate_QR)
button_1.place(x=25, y=50)

button_2 = ttk.Button(frame2, text="Save", width=10, command=Save_QR)
button_2.place(x=100, y=50)

button_3 = ttk.Button(frame2, text="Exit", width=10, command=Exit_QR)
button_3.place(x=175, y=50)

button_4 = ttk.Button(frame2, text="Clier", width=35, command=Clier_Text)
button_4.place(x=25, y=80)

window.mainloop()
