from tkinter import *

def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return "Error"

def click_common(event):
    global svalue
    text = event.widget.cget("text")
    if text == "=":
        result = evaluate_expression(screen.get())
        svalue.set(result)
        screen.update()
    elif text == "C":
        svalue.set("")
        screen.update()
    else:
        svalue.set(svalue.get() + text)
        screen.update()

top = Tk()
top.minsize(500, 500)
top.maxsize(500, 500)
top.title("calculator")
svalue = StringVar()
svalue.set("")
screen = Entry(top, textvar=svalue, font="lucida 40 ")
screen.pack(ipadx=10, pady=10, padx=10)

l = ["/", "C", "0", "=", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+"]
for i in range(4):
    frame1 = Frame(top, bg="beige")
    for j in range(4):
        n = 4 * i + j
        b = Button(frame1, text=l[n], height=1, width=2, bg='#b3ad8d', borderwidth=0, font="lucida 35 ")
        b.pack(side=LEFT, padx=18, pady=18)
        b.bind("<Button-1>", click_common)
    frame1.pack()

top.mainloop()
