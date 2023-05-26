from tkinter import *

canvas_height=400
canvas_width=600
canvas_colour="black"

p1_x=canvas_width*1/3
p1_y=canvas_height
p1_colour="green"
line_width=5
line_length=5

def p1_move_N(event):
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

p2_x=canvas_width*2/3
p2_y=canvas_height
p2_colour="red"
line_width=5
line_length=5

def p2_move_N(event):
    global p2_y    
    canvas.create_line(p2_x, p2_y, p2_x, (p2_y-line_length), width = line_width, fill = p2_colour)
    p2_y = p2_y - line_length

def p2_move_S(event):
    global p2_y    
    canvas.create_line(p2_x, p2_y, p2_x, p2_y+line_length, width = line_width, fill = p2_colour)
    p2_y = p2_y + line_length

def p2_move_E(event):
    global p2_x    
    canvas.create_line(p2_x, p2_y, p2_x+line_length,p2_y, width = line_width, fill = p2_colour)
    p2_x = p2_x + line_length

def p2_move_W(event):
    global p2_x    
    canvas.create_line(p2_x, p2_y, p2_x-line_length,p2_y, width = line_width, fill = p2_colour)
    p2_x = p2_x - line_length


def erase_all(event):
    canvas.delete(ALL)

window=Tk()
window.title("MyEtchASketch")
canvas=Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("<w>", p2_move_N)
window.bind("<s>", p2_move_S)
window.bind("<a>", p2_move_W)
window.bind("<d>", p2_move_E)
window.bind("<u>",erase_all)
window.mainloop()
