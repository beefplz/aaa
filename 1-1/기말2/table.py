from tkinter import*
class Table:
    def __init__(self, window, color="black", width=600, height=400,
                 net_color="green", vertical_net=False, horizontal_net=False):
        self.width=width
        self.height=height
        self.color=color
        self.canvas=Canvas(window, bg=self.color,
                           width=self.width, height=self.height)
        self.canvas.pack()
        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height,
                                    width=2, fill=net_color, dash=(15,23))
        if(horizontal_net):
            self.canvas.create_line(0, self.height/2, self,width, self.height/2,
                                    width=2, fill=net_color, dash=(15, 23))
        font=("monaco", 72)
        self.scoreboard=self.canvas.create_text(300, 65, font=font,
                                                 fill="darkgreen")
    def draw_rectangle(self, rectangle):
        x1=rectangle.x_posn
        x2=rectangle.x_posn+rectangle.width
        y1=rectangle.y_posn
        y2=rectangle.y_posn+rectangle.height
        c=rectangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
    def draw_oval(self, oval):
        x1=oval.x_posn
        x2=oval.x_posn+oval.width
        y1=oval.y_posn
        y2=oval.y_posn+oval.height
        c=oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
    def remove_item(self, item):
        self.canvas.delete(item)
    def change_item_color(self, item, c):
        self.canvas.itemconfigure(item, fill=c)
    def draw_score(self, left, right):
        scores=str(right)+"   "+str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)
