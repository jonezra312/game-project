import pyglet

from pyglet.shapes import Rectangle, Circle
from pyglet.window import Window, key 
print(key.LEFT)

#Window config 
window_width = 800
window_height = 600
window = Window(height=window_height, width=window_width, caption="My Game")

keys = key.KeyStateHandler()
window.push_handlers(keys)

# colors
GRAY=(170,170,170)
GREEN = (34,139,34)
WHITE = (255,255,255)

# path config
path_width = 400
path_x = (window_width-path_width)/2
path = Rectangle(path_x,0,path_width,window_height,GRAY)

#backround
green_background = Rectangle(0,0, window_width, window_height, GREEN)

#player config
player_y = 100
player_x = window_width/2
player_radius = 40

player = Circle(player_x,player_y,player_radius, color=WHITE)
player_speed = 150
player_dir = 'left'
def update(dt):
    
    # if player_dir == 'right' and player.x > path_x + path_width - player_radius:
    #     player_dir = 'left'
    # elif player_dir == 'left' and player.x < path_x + player_radius:
    #     player_dir = 'right'

    # if player_dir == 'right':
    #     player.x = player.x + player_speed * dt
    # if player_dir == 'left':
    #     player.x = player.x - player_speed * dt
   #controls     
    def update(dt):
        if keys[key.LEFT]:
         player.x-=player_speed * dt
    if keys[key.RIGHT]:
        player.x+=player_speed * dt
    if keys[key.UP]:
        player.y+=player_speed * dt
    if keys[key.DOWN]: 
        player.y-=player_speed * dt
    
    # if player_dir == 'right':
    #     player.x = player.x + player_speed * dt
    # if player_dir == 'left':
    #     player.x = player.x - player_speed * dt


    # if player_dir == 'right' and player.x > path_x + path_width - player_radius:
    #     player_dir = 'left'
    # elif player_dir == 'left' and player.x < path_x + player_radius:
    #     player_dir = 'right'

 #how the app runs
        @window.event
        def on_draw():
            window.clear()
    green_background.draw()
    path.draw()
    player.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()