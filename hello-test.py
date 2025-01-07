import pyglet
window = pyglet.window.Window(width=960, height=540)
label = pyglet.text.Label('Hello, Jon Ezra', font_size=36, x=20, y=490)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
