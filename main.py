#main file
from tkinter import *

def main():
    root = Tk()
    root.title("Calculator")
    create_components(root)
    root.mainloop()

def button_add():
    return

def create_components(root):
    e = Entry(root, width=40, borderwidth=5)
    e.grid(row = 0, column=0, columnspan=4, padx=1, pady=1)
    
    button0 = Button(root, text="0", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button1 = Button(root, text="1", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button2 = Button(root, text="2", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button3 = Button(root, text="3", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button4 = Button(root, text="4", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button5 = Button(root, text="5", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button6 = Button(root, text="6", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button7 = Button(root, text="7", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button8 = Button(root, text="8", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    button9 = Button(root, text="9", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())

    buttonEnter = Button(root, text="=", padx=40, pady=20, activebackground='gray', bg='white', command=button_add())
    buttonPlus = Button(root, text="+", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())
    buttonMultiply = Button(root, text="X", padx=20, pady=20, activebackground='gray', bg='white', command=button_add())

    button0.grid(row = 4, column=1)
    button1.grid(row = 3, column=0)
    button2.grid(row = 3, column=1)
    button3.grid(row = 3, column=2)
    button4.grid(row = 2, column=0)
    button5.grid(row = 2, column=1)
    button6.grid(row = 2, column=2)
    button7.grid(row = 1, column=0)
    button8.grid(row = 1, column=1)
    button9.grid(row = 1, column=2)
    buttonEnter.grid(row = 4, column=2, columnspan=2)
    buttonPlus.grid(row = 3, column=3)
    buttonMultiply.grid(row = 2, column=3)

if __name__ == "__main__":
    main()