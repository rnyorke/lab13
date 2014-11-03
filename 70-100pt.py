
### 70-100pt - Making a game ###


# 70pt - Add buttons for left, right and down that move the player circle - done
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')

player = drawpad.create_oval(390,580,410,600, fill="blue")

enemy1 = drawpad.create_oval(-20,5,0,25, fill = "red")
enemy1b= drawpad.create_oval(-20,5,0,25, fill = "red")
enemy2 = drawpad.create_oval(-20,300,0,320, fill = "red")
enemy2b= drawpad.create_oval(-20,300,0,320, fill = "red")
enemy3 = drawpad.create_oval(390,-20,410,0, fill = "red")
enemy3b= drawpad.create_oval(390,-20,410,0, fill = "red")
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
	    global enemy1b
	    global enemy2
            global enemy2b
            global enemy3
            global enemy3b
		
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
lol = 2
haha = 0
lol2 = 2
haha2 = 0
# Creating animation function
def animate():
    global direction
    global velocity
    global lol
    global haha
    global lol2
    global haha2
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    x3, y3, x4, y4 = drawpad.coords(enemy1b)
    x5, y5, x6, y6 = drawpad.coords(enemy2)
    x7, y7, x8, y8 = drawpad.coords(enemy2b)
    x9, y9, x10, y10 = drawpad.coords(enemy3)
    x11, y11, x12, y12 = drawpad.coords(enemy3b)
    if x2 > 840: 
        direction = 0
        drawpad.move(enemy1,-844,0)
        velocity = 2
    if x4 > 840:
        direction = 2
        drawpad.move(enemy1b,-844, 0 )
        velocity = 0
    if x6 > 840: 
        lol = 0
        drawpad.move(enemy2,-848,0)
        haha = 2
    if x8 > 840:
        lol = 2
        drawpad.move(enemy2b,-848, 0 )
        haha = 0
    if y10 > 640: 
        lol2 = 0
        drawpad.move(enemy3,0,-641)
        haha2 = 2
    if y12 > 640:
        lol2 = 2
        drawpad.move(enemy3b,0, -641)
        haha2 = 0
        
    drawpad.move(enemy1,direction * 2,0)
    drawpad.move(enemy1b,velocity * 2,0)
    drawpad.move(enemy2,lol * 1.5,0)
    drawpad.move(enemy2b,haha * 1.5,0)
    drawpad.move(enemy3,0,lol2)
    drawpad.move(enemy3b,0,haha2)
    drawpad.after(1, animate)

animate()
app = MyApp(root)
root.mainloop()