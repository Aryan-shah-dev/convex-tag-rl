from environment.arena import Map 
from environment.player import Player
from environment.physics import handle_boundary
class Environment:
    def __init__ (self):
        self.map = Map(800,600) 
        self.players = [Player(400,500,15) ,Player(400,100,15)]
    def step(self,actions):
        for i in range(len(self.players)):
            ax,ay = actions[i]
            player = self.players[i]
            player.apply_accel(ax,ay)
            player.clamp_speed()
            player.update()
            handle_boundary(player,self.map)
