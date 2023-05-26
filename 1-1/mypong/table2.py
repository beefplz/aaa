from tkinter import*

class Table2:
    def __init__(self, window, colour="black", net_colour="green",
                 width=600, height=400, vertical_net1 = False, vertical_net2=False):
        self.width = width
        self.height = height
        self.colour = colour
        
        self.canvas = Canvas(window, bg=self.colour,
                             height=self.height, width=self.width)
        self.canvas.pack()

        if (vertical_net1):
            self.canvas.create_line(self.width/3, 0, self.width/3,
                                    self.height, width=2, fill=net_colour,
                                    dash=(15,1))
        if (vertical_net2):
            self.canvas.create_line(self.width*2/3, 0, self.width*2/3,
                                    self.height, width=2, fill=net_colour,
                                    dash=(100,255))
        
