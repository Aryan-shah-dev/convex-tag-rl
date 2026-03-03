class Player:
    def __init__(self,x,y,radius, color):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0 
        self.radius = radius
        self.color = color

        self.max_speed = 5 
        self.acceleration = 0.5
        self.friction = 0.95

        self.hp = 100
        self.tag_active = False 
        self.tag_timer = 0
        self.tag_cooldown = 0

    def apply_accel(self,ax,ay):
        self.vx += ax*self.acceleration
        self.vy += ay*self.acceleration

    def clamp_speed(self):
        speed = (self.vx**2 + self.vy**2)**0.5 
        if speed>self.max_speed:
            scale = self.max_speed/speed 
            self.vx*=scale
            self.vy*=scale 

    def update(self):

        self.vx*=self.friction
        self.vy*=self.friction

        self.x += self.vx 
        self.y += self.vy 