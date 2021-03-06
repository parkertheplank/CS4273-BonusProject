from io import open_code
from tkinter import *
import time
from operator import pow, truediv, mul, add, sub  

def main():
    #creates root window
    root = Tk()
    root.title("Calculator")
    #root.geometry("260x465")
    root.resizable(0,0)
    root.configure(bg='Black')
    
    #creates the UI componenets
    create_components(root)
    #makes the window visible, must be put last
    root.mainloop()

#button event functions
def append_calc(e, symbol):
    global x                  # tracker for spot to insert 
    global text               # tracker for equation 
    if(valid_append(symbol)):   # for 8 dig rule
        e.insert(x,symbol)    # adds text to screen
        text += str(symbol)   # add to str for equation
        x+=1                  # to track where to put the text   
        return

def valid_append(symbol):     #determins if the symbol is valid to add to the calculation
    global text
    global dotCount
    global digitCount
    global startCount
    global alreadyHaveOp
    global opCount
    op1 = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }



    try:    #determins if a - can be added 
        if(text[len(text)-1] in op1 and symbol == "-" and alreadyHaveOp == False): 
            alreadyHaveOp = True
            opCount +=1 
            return True
    except:
        pass
    
    
    if (symbol in op1):     #handles adding a operation to the calculation
        if(alreadyHaveOp==False and opCount<1):
            if not (text[len(text)-1] in op1):
                dotCount = 0
                digitCount = 0
                startCount = False
                opCount +=1 
                return True
            else:
                return False
    elif symbol == '.':     #handles adding a decimal to the calculation
        try:
            if((not text[len(text)-1] in op1) and (text[len(text)-1] != '.')):
                startCount = True
                return True
            else:
                return False
        except:
            return True
    else:       #handles adding digits to the calculation
        if int(digitCount) >= 8 or int(dotCount) >= 3:
            return False
        else:
            digitCount+=1
            if startCount:
                dotCount+=1
            return True
    

def length(eight):            # to track how many chars are in this for 8 digit only requirement
    if(len(text)<8):          # just changes from true to false 
        eight=True 
    else:
        False           
    return eight

def postCalc(d):
    leftHasDec = False
    rightHasDec = False
    result, leftNum, rightNum  = calculate(d)
    result= str(result)
    if(type(leftNum) == float):
        leftHasDec = True
        hold1 = str(leftNum)
        leftOfDec, dot, rightOfDec = hold1.partition(".")
        lengthOfDecOnLefttNum = len(rightOfDec)
        leftHasDec = True

    if(type(rightNum) == float):
        hold2 = str(rightNum)
        leftOfDec, dot, rightOfDec = hold2.partition(".")
        lengthOfDecOnRightNum = len(rightOfDec)
        rightHasDec = True
    
    floatResult = float(result)
    if(leftHasDec == True and rightHasDec ==True ):
        if(lengthOfDecOnLefttNum >= lengthOfDecOnRightNum):
            if lengthOfDecOnLefttNum == 3: floatResult = "{:.3f}".format(floatResult)
            if lengthOfDecOnLefttNum == 2: floatResult = "{:.2f}".format(floatResult)
            if lengthOfDecOnLefttNum == 1: floatResult = "{:.1f}".format(floatResult)
        else:
            if lengthOfDecOnRightNum == 3: floatResult = "{:.3f}".format(floatResult)
            if lengthOfDecOnRightNum == 2: floatResult = "{:.2f}".format(floatResult)
            if lengthOfDecOnRightNum == 1: floatResult = "{:.1f}".format(floatResult)

    if(leftHasDec == True and rightHasDec !=True ):
            if lengthOfDecOnLefttNum == 3: floatResult = "{:.3f}".format(floatResult)
            if lengthOfDecOnLefttNum == 2: floatResult = "{:.2f}".format(floatResult)
            if lengthOfDecOnLefttNum == 1: floatResult = "{:.1f}".format(floatResult)

    if(leftHasDec != True and rightHasDec ==True ):
            if lengthOfDecOnRightNum == 3: floatResult = "{:.3f}".format(floatResult)
            if lengthOfDecOnRightNum == 2: floatResult = "{:.2f}".format(floatResult)
            if lengthOfDecOnRightNum == 1: floatResult = "{:.1f}".format(floatResult)

    try:
        leftOfDecResult, dot, rightOfDecResult = floatResult.partition(".")
        resultWithoutDec= leftOfDecResult+rightOfDecResult
    except:
        resultWithoutDec = len(str(floatResult))-1

    lengthOfResult = len(resultWithoutDec)
    if(lengthOfResult > 8):
        print("User can see 'ERR' displayed if any operation would exceed the 8 digit maximum.")
        return "ERR"
    return floatResult

def calculate(d):
    global text
    global negtive
    global alreadyHaveOp

    if d[:1] == '-':
        d = str(d[1:])
        negtive=True
    if d.find("+")!=-1:
       left, operator, right = d.partition("+")
       l = float(left)
       r = float(right)
       if(negtive==True):
            negtive = False
            alreadyHaveOp = False
            return (-l+r), l,r
       else:
             alreadyHaveOp = False
             return (l+r), l,r
    elif d.find("/")!=-1:
       left, operator, right = d.partition("/")
       l = float(left)
       r = float(right)
       if(negtive==True):
            negtive = False
            alreadyHaveOp = False
            return (-l/r), l,r
       else:
             alreadyHaveOp = False
             return (l/r)  , l,r 
    elif d.find("*")!=-1:
       left, operator, right = d.partition("*")
       l = float(left)
       r = float(right)
       if(negtive==True):
            negtive = False
            alreadyHaveOp = False
            return (-l*r), l,r
       else:
             alreadyHaveOp = False
             return (l*r), l,r
    elif d.find("-")!=-1:
       left, operator, right = d.partition("-")
       l = float(left)
       r = float(right)
       if(negtive==True):
            negtive = False
            alreadyHaveOp = False
            return (-l-r), l,r
       else:
             alreadyHaveOp = False
             return (l-r), l,r

 
'''
def calculate(d):
    op1 = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    print ("d= " + d)
    try:
        d = float(d)
    except:
        pass
    if type(d) == float:
        return float(d)
    for c in op1.keys():
        left, operator, right = d.partition(c)
        if operator in op1:
            return op1[operator](calculate(left), calculate(right))
'''

def eval_calc():
    global calc
    global x
    global text
    global digitCount
    global dotCount
    global startCount
    global opCount
    calc = str(postCalc(text))
    all_clr()
    x = len(calc)
    text = calc
    e.insert(1, calc) 
    opCount = 0

    # to fix going over  digits on the evaled number on the screen and 3 dec
    if calc.find(".")!=-1:
        calcedLeft, dot, calcedRight = calc.partition(".")
        digit = calcedLeft+calcedRight
        digit = str(digit)
        digitCount = len(digit)
        dotCount = len(calcedRight)
        startCount = True


        


def clr_calc():     #clears the last digit from the calculation
    global x
    global text
    global dotCount
    global digitCount
    global alreadyHaveOp
    global cheatingWay
    global startCount
    global opCount

    hold = text[-1:]
   
    if(hold=="."):
        cheatingWay=True


    op1 = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    if (text[len(text)-1] in op1):
        alreadyHaveOp = False
        opCount = opCount-1
        



    if x>=0:                  # keeps spot to insert from going negtive
        e.delete(x-1, 'end')  # deletes last number on screen 
        text = text[:-1]      # deletes last number on text str
        x=x-1                 # moves spot to insert back 1
        if(dotCount>0):dotCount = dotCount-1
        if(digitCount>0):digitCount = digitCount -1
    if(cheatingWay==True):
        digitCount +=1
        #dotCount += 1
        startCount=False
        cheatingWay =False
    


# for AC button
def all_clr():  #deletes every value on the screen 
    global x
    global text
    global dotCount
    global startCount
    global digitCount
    global alreadyHaveOp
    global opCount
    opCount =0
    alreadyHaveOp = False
    startCount=False          # resets 3 dot count
    dotCount = 0              # resets 3 dot count
    digitCount = 0
    e.delete(0, 'end')        # deletes everything 
    text =""                  # deletes everything on text str
    x=0                       # resets spot to insert
    return

    
def change_sign(e):            # negates the first number in the calculation
    global text
    global x
    if(text[:1] == '-'):      # if first char in str - delete it 
        text = str(text[1:])
        e.delete(0)
    else:
        i = x
        x = 0
        text = "-" + text[0:]
        e.insert(x,"-")    # if first char in str is nothing then add + 
        x = i
        x += 1
    return

def dotTracker(symbol):             # for the bonus thats for the bonus part 2
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
    #formatting vars
    fs = 25
    ent_w = 10
    boxw = int(ent_w/2)
    boxh = 1
    bord_pad = 5

    #Entry Box
    global e
    e = Entry(root, width=ent_w+1, font=('Impact', fs*2), bg='light gray', justify=RIGHT)
    e.grid(row = 0, column=0, padx=bord_pad, pady=bord_pad, columnspan=4)

    #numerical buttons
    #instantiates buttons
    button0 = Button(root, font=('Impact', fs), text="0", width = 2*boxw, height= boxh, padx=2*bord_pad, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"0"))
    button1 = Button(root, font=('Impact', fs), text="1", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"1"))
    button2 = Button(root, font=('Impact', fs), text="2", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"2"))
    button3 = Button(root, font=('Impact', fs), text="3", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"3"))
    button4 = Button(root, font=('Impact', fs), text="4", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"4"))
    button5 = Button(root, font=('Impact', fs), text="5", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"5"))
    button6 = Button(root, font=('Impact', fs), text="6", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"6"))
    button7 = Button(root, font=('Impact', fs), text="7", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"7"))
    button8 = Button(root, font=('Impact', fs), text="8", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"8"))
    button9 = Button(root, font=('Impact', fs), text="9", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"9"))
    #arranges where button will display
    button0.grid(row = 5, column=0, padx=bord_pad, pady=bord_pad, columnspan=2)
    button1.grid(row = 4, column=0, padx=bord_pad, pady=bord_pad)
    button2.grid(row = 4, column=1, padx=bord_pad, pady=bord_pad)
    button3.grid(row = 4, column=2, padx=bord_pad, pady=bord_pad)
    button4.grid(row = 3, column=0, padx=bord_pad, pady=bord_pad)
    button5.grid(row = 3, column=1, padx=bord_pad, pady=bord_pad)
    button6.grid(row = 3, column=2, padx=bord_pad, pady=bord_pad)
    button7.grid(row = 2, column=0, padx=bord_pad, pady=bord_pad)
    button8.grid(row = 2, column=1, padx=bord_pad, pady=bord_pad)
    button9.grid(row = 2, column=2, padx=bord_pad, pady=bord_pad)

    #operation buttons
    #instantiates button
    buttonEnter = Button(root, font=('Impact', fs), text="=", width = boxw, height= boxh, activebackground='light blue', bg='#d68d00', command=eval_calc)
    buttonMinus = Button(root, font=('Impact', fs), text="-", width = boxw, height= boxh, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"-"))
    buttonPlus = Button(root, font=('Impact', fs), text="+", width = boxw, height= boxh, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"+"))
    buttonMultiply = Button(root, font=('Impact', fs), text="X", width = boxw, height= boxh, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"*"))
    buttonDivide = Button(root, font=('Impact', fs), text="/", width = boxw, height= boxh, activebackground='light blue', bg='#d68d00', command=lambda: append_calc(e,"/"))
    buttonClear = Button(root, font=('Impact', fs), text="C", width = boxw, height= boxh, activebackground='light blue', bg='#ffb11a', command= clr_calc)
    buttonAllClear = Button(root, font=('Impact', fs), text="AC", width = boxw, height= boxh, activebackground='light blue', bg='#ffb11a', command=all_clr)
    buttonChangeSign = Button(root, font=('Impact', fs), text="+/-", width = boxw, height= boxh, activebackground='light blue', bg='#ffb11a', command=lambda: change_sign(e))
    buttonDot = Button(root, font=('Impact', fs), text=".", width = boxw, height= boxh, activebackground='light blue', bg='dark gray', command=lambda: append_calc(e,"."))

    #arranges where button will display
    buttonEnter.grid(row = 5, column=3, padx=bord_pad, pady=bord_pad)
    buttonPlus.grid(row = 4, column=3, padx=bord_pad, pady=bord_pad)
    buttonMultiply.grid(row = 2, column=3, padx=bord_pad, pady=bord_pad)
    buttonDivide.grid(row=1, column=3, padx=bord_pad, pady=bord_pad)
    buttonClear.grid(row=1,column=0, padx=bord_pad, pady=bord_pad)
    buttonAllClear.grid(row=1,column=2, padx=bord_pad, pady=bord_pad)
    buttonChangeSign.grid(row=1,column=1, padx=bord_pad, pady=bord_pad)
    buttonDot.grid(row=5,column=2, padx=bord_pad, pady=bord_pad)
    buttonMinus.grid(row=3,column=3, padx=bord_pad, pady=bord_pad)

opCount=0
x=0
text =""
dotCount=0
digitCount = 0
three = True
startCount = False
negtive = False
alreadyHaveOp = False
once = False
cheatingWay = False

#ensures code can only be run as the main file
if __name__ == "__main__":
    main()