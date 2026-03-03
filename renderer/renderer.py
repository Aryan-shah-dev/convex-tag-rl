class Renderer:
    def __init__(self,canvas,env):
        self.canvas = canvas 
        self.env = env 

        players = self.env.players

        self.players_shape = [] 
        for player in players:
            self.players_shape.append(
            self.canvas.create_oval(
            player.x-player.radius,
            player.y+player.radius,
            player.x+player.radius,
            player.y-player.radius,
            fill = player.color
            ))
    def render(self):
        players = self.env.players
        for i,player in enumerate(players):
            self.canvas.coords(
                self.players_shape[i],
                player.x - player.radius,
                player.y + player.radius,
                player.x + player.radius,
                player.y - player.radius,
            )
            if player.tag_active:
                self.canvas.itemconfig(self.players_shape[i], fill="red")
            else:
                self.canvas.itemconfig(self.players_shape[i],fill=player.color)