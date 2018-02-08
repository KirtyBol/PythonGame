import pyglet

monster_image = pyglet.image.load('monster.gif')
monster = pyglet.sprite.Sprite(monster_image, x=50, y=50)

window = pyglet.window.Window()

@window.event
def on_draw():
    monster.draw()

pyglet.app.run()