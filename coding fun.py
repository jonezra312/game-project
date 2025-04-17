import pyglet
from pyglet.shapes import Rectangle, Circle
from pyglet.window import Window, key
from pyglet.text import Label

from random import randint

# Window config
window_width = 800
window_height = 600
window = Window(height=window_height, width=window_width, caption="My Game")

keys = key.KeyStateHandler()
window.push_handlers(keys)

# Colors
GRAY=(170,170,170)
GREEN = (34,139,34)
WHITE = (255,255,255)
RED = (255,0,0)

# path config
path_width = 400
path_x = (window_width-path_width)/2
path = Rectangle(path_x,0,path_width,window_height,GRAY)

# backgronud
green_background = Rectangle(0,0, window_width, window_height, GREEN)

# player config
player_y = 100
player_x = window_width / 2
player_radius = 40

player = Circle(player_x,player_y,player_radius, color=WHITE )
player_speed = 150

obstacle_size = 40
obstacle_speed = 200

obstacles = []

def add_obstacle(dt):
    x_pos = randint(
        int(path.x+obstacle_size), 
        int(path.x + path_width - obstacle_size)
        )
    obstacle = Rectangle(x_pos,window_height-obstacle_size, obstacle_size, obstacle_size,RED)
    obstacles.append(obstacle)

points = 0
points_label = Label("Points: 0", font_name="Arial",font_size=18,
                     x=10, y=window_height-30)

def update_points(dt):
    global points
    points += 1
    points_label.text = f'Points: {points}'

health = 100
health_label = Label(
    f'Health: {health}', 
    font_name='Arial', 
    font_size=18, 
    x=10, 
    y=window_height - 60
)

game_over = False
game_over_label = Label(
    'Game Over',
    font_size=36,
    color=RED,
    x=window_width / 2,
    anchor_x='center',
    y=window_height / 2,
    anchor_y='center'
)

def check_collision():
    for obstacle in obstacles:
        if(
            player.x - player_radius < obstacle.x + obstacle.width and
            player.x + player_radius > obstacle.x and
            player.y - player_radius < obstacle.y + obstacle.height and
            player.y + player_radius > obstacle.y
        ):
            return obstacle
    return None

def update(dt):

    if keys[key.LEFT]:
        player.x -= player_speed * dt

    if keys[key.RIGHT]:
        player.x += player_speed * dt
       
    if keys[key.UP]:
        player.Y += player_speed * dt

    if keys[key.DOWN]:
        player.Y -= player_speed * dt

    if player.x > path_width+path_x-player_radius:
        player.x =  path_width+path_x-player_radius

    if player.x < path_x+player_radius:
        player.x = path_x + player_radius

    for obstacle in obstacles[:]:
        obstacle.y -= obstacle_speed * dt
        if obstacle.y + obstacle_size < 0:
            obstacle.delete()
            obstacles.remove(obstacle)
    obstacle_hit = check_collision()
    global health
    if obstacle_hit:
        health -= 10
        health_label.text = f'Health: {health}'
        obstacles.remove(obstacle_hit)
        obstacle_hit.delete()

    if health <= 0:
        global game_over
        game_over = True
        pyglet.clock.unschedule(update)
        pyglet.clock.unschedule(update_points)
        pyglet.clock.unschedule(add_obstacle)

@window.event
def on_draw():
    global game_over
    window.clear()
    green_background.draw()
    path.draw()
    player.draw()
    for obstacle in obstacles[:]:
        obstacle.draw()

    points_label.draw()
    health_label.draw()
    if game_over:
        game_over_label.draw()

@window.event
def on_mouse_press(x,y,button, modifiers):
    global game_over, health, points, obstacles
    if game_over:
        game_over = False
        health = 100
        points = 0
        obstacles.clear()
        add_obstacle(1)
        health_label.text = f'Health: {health}'
        points_label.text =f'Points: {points}'
        pyglet.clock.schedule_interval(update_points,1)
        pyglet.clock.schedule_interval(add_obstacle, 2)
        pyglet.clock.schedule_interval(update, 1/60)

add_obstacle(1)
pyglet.clock.schedule_interval(update_points,1)
pyglet.clock.schedule_interval(add_obstacle, 2)
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()