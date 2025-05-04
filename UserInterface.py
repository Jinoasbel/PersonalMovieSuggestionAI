import tkinter as tk

class UserInterface:

    Window = tk.Tk()
    Window.title("CinePhile")
    Window.geometry("500x500")
    logo = tk.PhotoImage(file="b49.png")
    label = tk.Label(Window,image=logo)
    label.pack()
    Window.mainloop()
