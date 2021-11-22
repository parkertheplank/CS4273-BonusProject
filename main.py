from tkinter import *

def main():
    #creates root window
    root = Tk()
    root.title("Calculator")
    root.geometry("300x500")
    
    #creates the UI componenets
    create_components(root)

    #makes the window visible, must be put last
    root.mainloop()

#button event functions
def append_calc(e, symbol):
    e.insert(0,symbol)
    return

def eval_calc(symbol):
    return

def clr_calc():
    e.delete(0, 'end')
# for AC button
def all_clr():
    return

#creates UI components
def create_components(root):
    #Entry Box
    e = Entry(root, width=40, borderwidth=5)
    e.grid(row = 0, column=0, columnspan=4, padx=1, pady=1)

    #numerical buttons
    #instantiates buttons
    button0 = Button(root, text="0", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"0"))
    button1 = Button(root, text="1", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"1"))
    button2 = Button(root, text="2", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"2"))
    button3 = Button(root, text="3", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"3"))
    button4 = Button(root, text="4", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"4"))
    button5 = Button(root, text="5", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"5"))
    button6 = Button(root, text="6", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"6"))
    button7 = Button(root, text="7", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"7"))
    button8 = Button(root, text="8", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"8"))
    button9 = Button(root, text="9", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"9"))
    #arranges where button will display
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

    #operation buttons
    #instantiates button
    buttonEnter = Button(root, text="=", padx=50, pady=20, activebackground='gray', bg='white', command=lambda: append_calc("1"))
    buttonPlus = Button(root, text="+", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"+"))
    buttonMultiply = Button(root, text="X", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"*"))
    buttonDivide = Button(root, text="/", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"/"))
    buttonClear = Button(root, text="C", padx=20, pady=20, activebackground='gray', bg='white', command= clr_calc)
    # needs added
    # buttonAllClear = Button(root, text="AC", padx=20, pady=20, activebackground='gray', bg='white', command=lambda: append_calc(e,"/"))

    #arranges where button will display
    buttonEnter.grid(row = 4, column=2, columnspan=2)
    buttonPlus.grid(row = 3, column=3)
    buttonMultiply.grid(row = 2, column=3)
    buttonDivide.grid(row=1, column=3)
    buttonClear.grid(row=4,column=0)
    #buttonAllClear.grid(row=6,column=3)

#ensures code can only be run as the main file
if __name__ == "__main__":
    main()