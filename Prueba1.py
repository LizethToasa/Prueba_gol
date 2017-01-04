from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
my_image=PhotoImage(file="pelt.png")
my_image1=PhotoImage(file="arc.png")
my_image2=PhotoImage(file="gol.png")

canvas.create_image(150,300,anchor=NW,image=my_image)
canvas.create_image(300,300,anchor=NW,image=my_image1)
def movetriangle(event):
    x=0
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        x=100
    else:
        canvas.move(1, 3, 0)
    print("coordenada: ",x)
    print(canvas.create_image(300,300,anchor=NW,image=my_image2))


canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()
