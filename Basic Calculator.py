
Bhavya248
/
python-patterns
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
python-patterns/cala.py
@Bhavya248
Bhavya248 #
 1 contributor
149 lines (136 sloc)  4.03 KB
from tkinter import *
from math import *
from tkinter import ttk

result_list = []


def compute(x, y=result_list):
    if x in ["0", "1", "2", "3", "4", "5", "6",
             "7", "8", "9", "(", ")", "-", "+", "/"]:
        y.append(x)
        ata.set(" ".join(y))
    elif x == "x":
        y.append("*")
        ata.set("".join(y))
    elif x == ".":
        pass
    elif x == "C":
        y.clear()
        ata.set("".join(y))
    elif x == "<-":
        del y[-1]
        ata.set("".join(y))
    elif x == "MOD":
        y.append("%")
        ata.set("".join(y))
    elif x == "pi":
        if len(y) > 0:
            y.append("*(3.14)")
        else:
            y.append("3.14")
        ata.set("".join(y))
    elif x == "e":
        if len(y) > 0:
            y.append("*(2.718)")
        else:
            y.append("2.718")
        ata.set("".join(y))
    elif x == "=":
        if len(y) > 0:
            w = eval("".join(y))
            ata.set(w)
            y.clear()
            y.append(str(w))
    elif x == "n!":
        if eval("".join(y)) > 0:
            w = factorial(eval("".join(y)))
            ata.set(w)
            y.clear()
            y.append(w)
        else:
            y.clear()
            y.append(str(0))
            ata.set("FACTORIAL NOT EXIST")
    elif x == "|x|":
        ata.set(abs(eval("".join(y))))
        y.append(str(abs(eval("".join(y)))))

    elif x == "1/x":
        print(y)
        w = 1/eval("".join(y))
        ata.set(w)
        y.clear()
        y.append(str(w))
    elif x == "X^2":
        w = eval("".join(y))**2
        ata.set(w)
        y.clear()
        y.append(str(w))
    elif x == "X^0.5":
        w = eval("".join(y))**(0.5)
        ata.set(w)
        y.clear()
        y.append(str(w))
    elif x == "10^x":
        w = 10**eval("".join(y))
        ata.set(w)
        y.clear()
        y.append(str(w))
    elif x == "log":
        if (eval("".join(y))) > 0:
            w = log(eval("".join(y)))/2.302585092994046
            ata.set(w)
            y.clear()
            y.append(str(w))
        else:
            ata.set("Logarithm to base 10 not defined")
            y.clear()
    elif x == "ln":
        if (eval("".join(y))) > 0:
            w = log(eval("".join(y)))
            ata.set(w)
            y.clear()
            y.append(str(w))
        else:
            ata.set("Logarithm to base 10 not defined")
            y.clear()
    else:
        pass


home = Tk()
home.configure(bg='#EFEFEF')
home.geometry('350x400')
home.attributes('-toolwindow', True)
home.rowconfigure(0, weight=1)
home.rowconfigure(1, weight=1)
home.columnconfigure(1, weight=1)
home.columnconfigure(0, weight=1)

frame0 = Frame(home, bg='yellow', highlightbackground="yellow",
               highlightthickness=3, height=1, width=4)
frame2 = Frame(home, bg='blue', height=8, width=10)

frame0.grid(row=0, column=0, sticky='nsew', columnspan=4, padx=1, pady=1)
frame2.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=3, pady=3)

frame0.columnconfigure(0, weight=1)
frame0.rowconfigure(0, weight=1)
frame0.rowconfigure(1, weight=1)

ata = StringVar()
display = Entry(frame0, bg="#FFFFFF", textvariable=ata)
display.grid(row=0, column=0, columnspan=2, sticky='nsew')

a = [["2^x", 0, 0], ["pi", 0, 1], ["e", 0, 2],
     ["C", 0, 3], ["<-", 0, 4], ["X^2", 1, 0],
     ["1/x", 1, 1], ["|x|", 1, 2], ["exp", 1, 3],
     ["MOD", 1, 4], ["X^0.5", 2, 0], ["(", 2, 1],
     [")", 2, 2], ["n!", 2, 3], ["/", 2, 4],
     ["10^x", 3, 0], ["7", 3, 1], ["8", 3, 2],
     ["9", 3, 3], ["x", 3, 4], ["x^y", 4, 0],
     ["4", 4, 1], ["5", 4, 2], ["6", 4, 3],
     ["-", 4, 4], ["log", 5, 0], ["1", 5, 1],
     ["2", 5, 2], ["3", 5, 3], ["+", 5, 4],
     ["ln", 6, 0], ["+/-", 6, 1], ["0", 6, 2],
     [".", 6, 3], ["=", 6, 4]]
b_dict = {}
for i in range(len(a)):
    def com(x=a[i][0]):
        return compute(x)
    b_dict[str(i)] = ttk.Button(
        frame2, text=str(a[i][0]), command=com, width=2)
    b_dict[str(i)].grid(row=a[i][1], column=a[i][2], sticky='nsew')
    frame2.columnconfigure(a[i][2], weight=1)
    frame2.rowconfigure(a[i][1], weight=1)


home.mainloop()
