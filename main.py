import tkinter as tk 
from environment.arena import Map
from environment.player import Player
from environment.environment import Environment
from renderer.renderer import Renderer 

def update():
    ax = 0
    ay = 0
    bx = 0
    by = 0
    atag = False
    btag = False
    if keys["w"]:
        ay-=1 
    if keys["a"]:
        ax-=1 
    if keys["s"]:
        ay+=1 
    if keys["d"]:
        ax+=1 
    if keys["up"]:
        by-=1 
    if keys["left"]:
        bx-=1 
    if keys["right"]:
        bx+=1 
    if keys["down"]:
        by+=1
    if keys["space"]:
        atag = True 
    if keys["k"]:
        btag = True
    env.step([(ax,ay,atag), [bx,by,btag]])
    renderer.render()
    root.after(16,update)
    if env.game_over:
        root.destroy()
    
keys = {
    "w" : False,
    "a" : False,
    "s" : False,
    "d" : False,
    "up": False,
    "left": False,
    "right": False,
    "down" : False,
    "k" : False,
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