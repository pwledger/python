import tkinter as tk
import time 

game = tk.Tk()

game.title("game")
game.geometry("600x600")

canvas = tk.Canvas(game , width=500 , height=500 , bg = "white")
canvas.pack()
for i in range(10):
    line = canvas.create_line(0,50*i,500,50*i)
    line = canvas.create_line(50*i,0,50*i,500)

b = canvas.create_oval(0,0,50,50,fill="red")
#b = canvas.create_oval(450,450,500,500,fill="red")

def 아래이동(event):
    x1,y1,x2,y2 = canvas.coords(b)  # 현재 b 의 위치
    if y1 < 450:
        canvas.move(b , 0, 50)
def 위이동(event):
    x1,y1,x2,y2 = canvas.coords(b)  # 현재 b 의 위치
    if y1 > 0:
        canvas.move(b , 0,-50)
def 왼쪽이동(event):
    canvas.move(b , -50, 0)
def 오르쪽이동(event):
    canvas.move(b , 50, 0)

game.bind("d" , 오르쪽이동)
game.bind("a" , 왼쪽이동)
game.bind("w" , 위이동)
game.bind("s" , 아래이동)

game.mainloop()