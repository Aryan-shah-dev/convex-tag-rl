import tkinter as tk 
from environment.arena import Map
from environment.player import Player
from environment.environment import Environment
from renderer.renderer import Renderer 

def update():
    ax = 0
    ay = 0
    if keys["w"]:
        ay-=1 
    if keys["a"]:
        ax-=1 
    if keys["s"]:
        ay+=1 
    if keys["d"]:
        ax+=1 
    env.step((ax,ay))
    renderer.render()
    root.after(16,update)
    
keys = {
    "w" : False,
    "a" : False,
    "s" : False,
    "d" : False,
    "space" : False
 }
def key_press(event):
    k = event.keysym.lower() 
    if k in keys:
        keys[k] = True
def key_release(event):
    k = event.keysym.lower()
    if k in keys:
        keys[k] = False
root = tk.Tk()
root.title("convex-tag-rl")

canvas = tk.Canvas(root,width=800,height=600,bg="black",highlightthickness=0,bd=0)
canvas.pack()

root.bind("<KeyPress>" , key_press) 
root.bind("<KeyRelease>",key_release)

env = Environment()
renderer = Renderer(canvas, env)

update()
root.mainloop()