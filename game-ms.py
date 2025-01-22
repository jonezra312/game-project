import pyglet

from pyglet.shapes import Rectangle

window_width = 800
window_height = 600
window = pyglet.window.Window(height=window_height, width=window_width, caption="My Game")

GRAY=(170,170,170)
GREEN = (34,139,34)

path_width = 400
path_x = (window_width-path_width)/2
path = Rectangle(path_x,0,path_width,window_height,GRAY)
green_background = Rectangle(0,0, window_width, window_height, GREEN)

@window.event
def on_draw():
    window.clear()
    green_background.draw()
    path.draw()
pyglet.app.run()
