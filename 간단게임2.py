# 기본틀 만들기
import tkinter as tk
import random

game = tk.Tk()
game.title("누가 먹냐")
game.geometry("600x600")

canvas = tk.Canvas(game , width=500, height=500,bg = "white")
canvas.pack()
for i in range(10):
    line = canvas.create_line(0,50*i,500,50*i , fill="red" )
    line = canvas.create_line(50*i,0,50*i,500 , fill="blue")

# 플레이어 만들기
p1 = canvas.create_oval(0,0,50,50 , fill="red")
p2 = canvas.create_oval(450,450,500,500 , fill="blue")

# 먹이 만들기 
def 먹이만들기():
    x = random.randrange(0,500,50) # 0 ~ 500 , 50 간격 
    y = random.randrange(0,500,50)
    g = canvas.create_oval(x,y,x + 50 ,y + 50 , fill="green")
    return g

food = 먹이만들기()
점수 = 0 
def 충돌():
    global food
    global 점수
    pp1 = canvas.coords(p1)
    f1 = canvas.coords(food)
    if pp1[0] == f1[0] and pp1[1] == f1[1]:
        canvas.delete(food)
        food = 먹이만들기()
        점수 += 100
        label.config(text = f"player1 점수 : {점수}")

# 이동 (상하좌우)
def 하(event):
    pp1 = canvas.coords(p1)
    if pp1[1] == 450:
        canvas.move(p1, 0,-500)
    canvas.move(p1 , 0,50)
    충돌()
def 상(event):
    pp1 = canvas.coords(p1)
    if pp1[1] == 0:
        canvas.move(p1, 0,500)
    canvas.move(p1 , 0,-50)
    충돌()
def 좌(event):
    pp1 = canvas.coords(p1)
    if pp1[0] == 0:
        canvas.move(p1, 500,0)
    canvas.move(p1 , -50,0)
    충돌()
def 우(event):
    pp1 = canvas.coords(p1)
    if pp1[0] == 450:
        canvas.move(p1, -500,0)
    canvas.move(p1 , 50,0)
    충돌()

game.bind("s" , 하)  # s 키를 눌렀 을때 "하" 함수 동작
game.bind("w" , 상)  # s 키를 눌렀 을때 "상" 함수 동작
game.bind("a" , 좌)  # s 키를 눌렀 을때 "좌" 함수 동작
game.bind("d" , 우)  # s 키를 눌렀 을때 "우" 함수 동작

label = tk.Label(game , text = "player1 점수 : ")
label.pack()

game.mainloop()