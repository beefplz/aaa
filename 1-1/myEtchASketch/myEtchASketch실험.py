from tkinter import *



p1_x=300
p1_y=400
p1_colour="green"
line_width=5
line_length=5

def p1_move_N():
    global p1_y    
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width = line_width, fill = p1_colour)
    p1_y = p1_y - line_length

def p1_move_S(event):
    global p1_y    
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width = line_width, fill = p1_colour)
    p1_y = p1_y + line_length

def p1_move_E(event):
    global p1_x    
    canvas.create_line(p1_x, p1_y, p1_x+line_length,p1_y, width = line_width, fill = p1_colour)
    p1_x = p1_x + line_length

def p1_move_W(event):
    global p1_x    
    canvas.create_line(p1_x, p1_y, p1_x-line_length,p1_y, width = line_width, fill = p1_colour)
    p1_x = p1_x - line_length

def erase_all(event):
    canvas.delete(ALL)

window=Tk()
window.title("MyEtchASketch")
canvas=Canvas(bg="black", height=400, width=600, highlightthickness=0)
canvas.pack()

window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("<u>", erase_all)

window.mainloop()
