from tkinter import*

class Table3:
    def __init__(self, window, colour="black", net_colour="green",
                 width=600, height=400,
                 vertical_net = False, horizontal_net=False,
                 top_right_net=False, top_left_net=False,
                 square1=False, square2=False, square3=False, square4=False):
        self.width = width
        self.height = height
        self.colour = colour
        
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()

        if (vertical_net):
            self.canvas.create_line(self.width/2, 0,
                                    self.width/2, self.height, width=2,
                                    fill=net_colour, dash=(15,23))
        if (horizontal_net):
            self.canvas.create_line(0, self.height/2,
                                    self.width, self.height/2, width=2,
                                    fill=net_colour, dash=(15,23))
        if (top_left_net):
            self.canvas.create_line(0, 0,
                                    self.width, self.height, width=2,
                                    fill=net_colour, dash=(15, 23))
        if (top_right_net):
            self.canvas.create_line(self.width, 0,
                                    0, self.height, width=2,
                                    fill=net_colour, dash=(15, 23))
        if (square1):
            self.canvas.create_line(self.width/3, self.height/3,
                                    self.width/3, self.height*2/3, width=2,
                                    fill=net_colour, dash=(15, 23))
        if (square2):
            self.canvas.create_line(self.width/3, self.height/3,
                                    self.width*2/3, self.height/3, width=2,
                                    fill=net_colour, dash=(15, 23))
        if (square3):
            self.canvas.create_line(self.width/3, self.height*2/3,
                                    self.width*2/3, self.height*2/3, width=2,
                                    fill=net_colour, dash=(15, 23))
        if (square4):
            self.canvas.create_line(self.width*2/3, self.height/3,
                                    self.width*2/3, self.height*2/3, width=2,
                                    fill=net_colour, dash=(15, 23))
