from environment.arena import Map 
from environment.player import Player
from environment.physics import handle_boundary
class Environment:
    def __init__ (self):
        self.map = Map(800,600) 
        self.player = Player(400,300,15) 
    def step(self,action):
        ax , ay = action 
        self.player.apply_accel(ax,ay)
        self.player.clamp_speed()
        self.player.update()
        handle_boundary(self.player,self.map)
