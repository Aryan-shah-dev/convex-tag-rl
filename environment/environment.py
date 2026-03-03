from environment.arena import Map 
from environment.player import Player
from environment.physics import handle_boundary
from environment.physics import handle_tag
from environment.physics import handle_collisions
class Environment:
    def __init__ (self):
        self.map = Map(800,600) 
        self.players = [Player(400,500,15,color="blue") ,Player(400,100,15,color="green")]
        self.global_tag = False
        self.game_over = False
    def step(self,actions):
        handle_collisions(self.players)
        for i in range(len(self.players)):
            ax,ay,tag = actions[i]
            player = self.players[i]
            player.apply_accel(ax,ay)
            player.clamp_speed()
            self.global_tag = handle_tag(player,tag,self.global_tag)
            player.update()
            handle_boundary(player,self.map)
            if player.hp <= 0 :
                self.game_over = True
