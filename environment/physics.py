def handle_boundary(player,game_map):
    r = player.radius 
    if player.x - r <0:
        player.x = r
        if player.vx < 0:
            player.vx = 0
    if player.x + r > game_map.width:
        player.x = game_map.width - r
        if player.vx >0:
            player.vx = 0
    if player.y-r  < 0:
        player.y = r 
        if player.vy <0:
            player.vy = 0
    if player.y+r > game_map.height:
        player.y = game_map.height-r 
        if player.vy > 0:
            player.vy = 0