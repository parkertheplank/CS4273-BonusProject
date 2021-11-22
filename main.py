from tkinter import *
import time
from operator import pow, truediv, mul, add, sub  

def main():
    #creates root window
    root = Tk()
    root.title("Calculator")
    root.geometry("250x365")
    root.configure(bg='Black')
    
    #creates the UI componenets
    create_components(root)
    #makes the window visible, must be put last
    root.mainloop()

#button event functions
def append_calc(e, symbol):
    global x                  # tracker for spot to insert 
    global text               # tracker for equation 
    if(length(text)==True and dotTracker()==True):   # for 8 dig rule
        e.insert(x,symbol)    # adds text to screen
        text += str(symbol)   # add to str for equation
        x+=1                  # to track where to put the text    
        return

def length(eight):            # to track how many chars are in this for 8 digit only requirement
    if(len(text)<8):          # just changes from true to false 
        eight=True            
    return eight


def calculate(d):
    op1 = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    if d.isdigit():
        return float(d)
    for c in op1.keys():
        left, operator, right = d.partition(c)
        if operator in op1:
            return op1[operator](calculate(left), calculate(right))

def eval_calc():
    global calc
     
    calc = str(calculate(text))
    all_clr()
    e.insert(1, calc)  

def clr_calc():
    global x
    global text
    global dotCount
    if x>=0:                  # keeps spot to insert from going negtive
        e.delete(x-1, 'end')  # deletes last number on screen 
        text = text[:-1]      # deletes last number on text str
        x=x-1                 # moves spot to insert back 1
        dotCount = dotCount-1


# for AC button
def all_clr():
    global x
    global text
    global dotCount
    global startCount
    startCount=False          # resets 3 dot count
    dotCount = 0              # resets 3 dot count
    e.delete(0, 'end')        # deletes everything 
    text =""                  # deletes everything on text str
    x=0                       # resets spot to insert
    return

    
def change_sign():            # for the bonus thats for the bonus
    global text
    if(text[:1] == "-"):      # if first char in str - delete it 
        text = text[1:]
    else:
        text = "-" + text     # if first char in str is nothing then add + 
    return

def dotTracker():             # for the bonus thats for the bonus part 2
    global startCount
    global three
    global dotCount
    if(dotCount>=3):
        three=False
    if(dotCount<3):
        three=True
    if(text[x-1:] == "."):
        startCount=True
    if(startCount==True and three == True):
        dotCount += 1
    return three


#creates UI components
def create_components(root):
    #Entry Box
    global e
    e = Entry(root, width=40, borderwidth=5, justify=RIGHT)
    e.grid(row = 0, column=0, columnspan=4, padx=1, pady=1)

    #numerical buttons
    #instantiates buttons
    button0 = Button(root, font= 30, text="0", height=2, width=10, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"0"))
    button1 = Button(root, font= 30, text="1", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"1"))
    button2 = Button(root, font= 30, text="2", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"2"))
    button3 = Button(root, font= 30, text="3", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"3"))
    button4 = Button(root, font= 30, text="4", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"4"))
    button5 = Button(root, font= 30, text="5", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"5"))
    button6 = Button(root, font= 30, text="6", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"6"))
    button7 = Button(root, font= 30, text="7", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"7"))
    button8 = Button(root, font= 30, text="8", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"8"))
    button9 = Button(root, font= 30, text="9", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"9"))
    #arranges where button will display
    button0.grid(row = 5, column=0, columnspan=2)
    button1.grid(row = 4, column=0)
    button2.grid(row = 4, column=1)
    button3.grid(row = 4, column=2)
    button4.grid(row = 3, column=0)
    button5.grid(row = 3, column=1)
    button6.grid(row = 3, column=2)
    button7.grid(row = 2, column=0)
    button8.grid(row = 2, column=1)
    button9.grid(row = 2, column=2)

    #operation buttons
    #instantiates button
    buttonEnter = Button(root, font= 30, text="=", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#d68d00', command=eval_calc)
    buttonMinus = Button(root, font= 30, text="-", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"-"))
    buttonPlus = Button(root, font= 30, text="+", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"+"))
    buttonMultiply = Button(root, font= 30, text="X", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"*"))
    buttonDivide = Button(root, font= 30, text="/", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"/"))
    buttonClear = Button(root, font= 30, text="C", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#ffb11a', command= clr_calc)
    buttonAllClear = Button(root, font= 30, text="AC", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#ffb11a', command=all_clr)
    buttonChangeSign = Button(root, font= 30, text="+/-", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='#ffb11a', command=change_sign)
    buttonDot = Button(root, font= 30, text=".", height=2, width=3, padx=10, pady=5, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"."))

    #arranges where button will display
    buttonEnter.grid(row = 5, column=3)
    buttonPlus.grid(row = 4, column=3)
    buttonMultiply.grid(row = 2, column=3)
    buttonDivide.grid(row=1, column=3)
    buttonClear.grid(row=1,column=0)
    buttonAllClear.grid(row=1,column=2)
    buttonChangeSign.grid(row=1,column=1)
    buttonDot.grid(row=5,column=2)
    buttonMinus.grid(row=3,column=3)

    # Helps With Allginment of buttons, I couldn't find a better way that didn't use 100 lines of code
    buttonHelpsWithAllginment0 = Button(root, font= 30, text="you", height=3, width=4, padx=10, pady=1, activebackground='gray', bg='yellow')
    buttonHelpsWithAllginment0.grid(row=1,column=4)
    buttonHelpsWithAllginment1 = Button(root, font= 30, text="see", height=3, width=4, padx=10, pady=1, activebackground='gray', bg='yellow')
    buttonHelpsWithAllginment1.grid(row=2,column=4)
    buttonHelpsWithAllginment2 = Button(root, font= 30, text="nothing", height=3, width=4, padx=10, pady=1, activebackground='gray', bg='yellow')
    buttonHelpsWithAllginment2.grid(row=3,column=4)
    buttonHelpsWithAllginment3 = Button(root, font= 30, text="okay?", height=3, width=4, padx=10, pady=1, activebackground='gray', bg='yellow')
    buttonHelpsWithAllginment3.grid(row=4,column=4)
    buttonHelpsWithAllginment4 = Button(root, font= 30, text="bye", height=3, width=4, padx=10, pady=1, activebackground='gray', bg='yellow')
    buttonHelpsWithAllginment4.grid(row=5,column=4)


x=0
text =""
dotCount=0
three = True
startCount = False
#ensures code can only be run as the main file
if __name__ == "__main__":
    main()