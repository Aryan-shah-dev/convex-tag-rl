class Renderer:
    def __init__(self,canvas,env):
        self.canvas = canvas 
        self.env = env 

        player = self.env.player 

        self.player_shape = self.canvas.create_oval(
            player.x-player.radius,
            player.y+player.radius,
            player.x+player.radius,
            player.y-player.radius 
        )
    def render(self):
        player = self.env.player 

        self.canvas.coords(
            self.player_shape,
            player.x - player.radius,
            player.y + player.radius,
            player.x + player.radius,
            player.y - player.radius
        )