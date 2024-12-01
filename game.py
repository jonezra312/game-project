import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
