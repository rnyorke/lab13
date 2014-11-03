
### 70-100pt - Making a game ###


# 70pt - Add buttons for left, right and down that move the player circle - done
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')

player = drawpad.create_oval(390,580,410,600, fill="blue")

enemy1 = drawpad.create_oval(390,0,410,20, fill = "red")
enemy1b= drawpad.create_oval(390,0,410,20, fill = "red")
enemy2 = drawpad.create_oval(390,300,410,320, fill = "red")
enemy2b= drawpad.create_oval(390,300,410,320, fill = "red")

direction = 2
velocity = 0
# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "cyan")
       	    self.up.grid(row=0,column=1)
       	    
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background = "cyan")
       	    self.down.grid(row=1,column=1)
       	    
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background = "cyan")
       	    self.left.grid(row=0,column=0)
       	    
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background = "cyan")
       	    self.right.grid(row=0,column=3)
       	    
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    # Bind an event to the first button
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    global enemy1
	    global enemy2
	    global enemy3
	    global enemy4
	    global enemy5
	    global enemy6
	    global enemy7
	    global enemy8
	    global enemy9
	    global enemy10
        def motion():
            x1, y1, x2, y2 = drawpad.coords(enemy1)
            x3, y3, x4, y4 = drawpad.coords(enemy1b)
            # Making the enemy wrap around smoothly
            if x2 > 840: 
                direction = 0
                drawpad.move(circle,-841,0)
                velocity = 2
            if x4 > 840:
                direction = 2
                drawpad.move(circle2,-841, 0 )
                velocity = 0
            drawpad.move(enemy1,direction,0)
            drawpad.move(enemy2,velocity,0)
            drawpad.after(1, animate)
		
	def upClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,0,-20)
        def downClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,0,20)
        def leftClicked(self,event):
            global oval
            global player
            drawpad.move(player,-20,0)
        def rightClicked(self,event):
            global oval
            global player
            drawpad.move(player,20,0)
drawpad.grid(row=0, column=0)

direction = 2
velocity = 0
# Creating animation function
def animate():
    global direction
    global velocity

    x1, y1, x2, y2 = drawpad.coords(enemy1)
    x3, y3, x4, y4 = drawpad.coords(enemy1b)
    if x2 > 840: 
        direction = 0
        drawpad.move(enemy1,-841,0)
        velocity = 2
    if x4 > 840:
        direction = 2
        drawpad.move(enemy1b,-841, 0 )
        velocity = 0



    x5, y5, x6, y6 = drawpad.coords(enemy2)
    x7, y7, x8, y8 = drawpad.coords(enemy2b)
    if x6 > 840: 
        direction = 0
        drawpad.move(enemy2,-841,0)
        velocity = 2
    if x8 > 840:
        direction = 2
        drawpad.move(enemy2b,-841, 0 )
        velocity = 0
    drawpad.move(enemy1,direction,0)
    drawpad.move(enemy1b,velocity,0)
    drawpad.move(enemy2,direction,0)
    drawpad.move(enemy2b,velocity,0)
    drawpad.after(1, animate)

animate()
app = MyApp(root)
root.mainloop()