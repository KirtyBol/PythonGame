import pyglet
from pyglet import window

animation = pyglet.resource.animation('monster.gif')
monster = pyglet.sprite.Sprite(animation, x = 100, y = 100)


window = pyglet.window.Window(width = 640, height = 800)

def draw():
	animation.draw()

pyglet.app.run()