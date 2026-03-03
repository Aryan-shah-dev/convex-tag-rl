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
def handle_tag(player,tag,global_tag):
    if player.tag_cooldown == 0 and tag and not global_tag:
        player.tag_cooldown = 180
        player.tag_active = True 
        player.tag_timer = 60
        return True
    else:
        if player.tag_timer == 1:
            player.tag_cooldown = max(0, player.tag_cooldown-1)
            player.tag_timer = max(0 , player.tag_timer-1)
            player.tag_active = False
            return False
        else:
            player.tag_cooldown = max(0, player.tag_cooldown-1)
            player.tag_timer = max(0, player.tag_timer-1)
            return global_tag