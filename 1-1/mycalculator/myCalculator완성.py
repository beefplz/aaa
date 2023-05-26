from tkinter import*


window = Tk()
window.title("MyCalculator")

top_row = Frame(window)
top_row.grid(row=0, column=0,columnspan=2, sticky=N)

display = Entry(top_row, width=45, bg="light green")
display.grid()

num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list=['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '=']

r=0
c=0

for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)

    c=c+1
    if c>2:
        c=0
        r=r+1

operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = ['*', '/', '+', '-', '(', ')', 'C' ]

r=0
c=0

for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text, width=5,command=cmd).grid(row=r, column=c)

    c=c+1
    if c>1:
        c=0
        r=r+1
def click(key):
    if key == "=":
        result = str(eval(display.get()))[0:10]
        display.insert(END, "=" + result)
        
    elif key == "C":
        display.delete(0, END)

    else:
        display.insert(END, key)



window.mainloop()
