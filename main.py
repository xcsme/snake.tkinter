import tkinter
from tkinter import *
import random
from const import *

def create_food():
    x = random.randint(1,(canvas_size - grid_size) // grid_size ) * grid_size
    y = random.randint(1,(canvas_size - grid_size) // grid_size) * grid_size
    return x, y

def draw_snake():
    canvas.delete('snake')
    i = 0
    for x, y in snake:
        if i==0:
            img = PhotoImage(file="smile.png")
            canvas.create_image(50, 50, anchor=tkinter.CENTER, image=img)
        else:
            canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill='green', tags='snake')
        i+=1


def draw_food():
    canvas.delete('food')
    x,y = food

    canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill='red', tags='food')

def check_collision():
    head_x, head_y = snake[0]
    if head_x < 0 or head_x >= canvas_size or head_y < 0 or head_y >= canvas_size:
        return True
    if (head_x, head_y) in snake[1:]:
        return  True
    return False

def check_food():
    global food
    head_x, head_y = snake[0]
    food_x, food_y = food
    if head_x == food_x and head_y == food_y:
        global score
        score += 1
        snake.append((0,0))
        food = create_food()

def move_snake():
    head_x, head_y = snake[0]
    #print(snake_direction)
    if snake_direction=='w':
        new_head = (head_x, head_y - grid_size)
    elif snake_direction=='s':
        new_head = (head_x, head_y + grid_size)
    elif snake_direction=='a':
        new_head = (head_x - grid_size, head_y)
    elif snake_direction=='d':
        new_head = (head_x + grid_size, head_y)
    snake.insert(0, new_head)
    snake.pop()

def change_direction(event):
    global snake_direction
    new_direction = event.keysym
    if new_direction == 'w' or new_direction == 's' or new_direction == 'a' or new_direction == "d":
        o = {'w':'s', 'a':'d', 'd':'a', 's':'w'}
        if new_direction != o[snake_direction]:
            snake_direction = new_direction

def update():
    if not check_collision():
        move_snake()
        check_food()
        draw_snake()
        draw_food()
        root.after(100, update)
    else:
        label1=tkinter.Label(root,text=f"Игра окончена.Ваш счет:{score}",font=("Arial",14))
        label1.pack()







root=Tk()
root.title("Змейка")
#root.geometry("1700x1000")
root.resizable(False,False)
canvas=Canvas(root,width=canvas_size,height=canvas_size,background="grey")

canvas.pack()
root.bind("<Key>", change_direction)
update()

root.mainloop()

#вместо головы змейки сделать изображение