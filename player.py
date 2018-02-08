import pyglet

from drawable import GameObject

class Player(GameObject):
	animation = pyglet.resource.animation("monster.gif")

	def draw(self):
		monster = pyglet.sprite.Sprite(self.animation, self.centerX, self.centerY)
		monster.draw()

	def update(self, dt, keys):
		if keys['left']: 
			self.monster.x -= 100 * dt 
		elif keys['right']: 
			self.monster.x += 100 * dt
		elif keys['up']:
			self.monster.y += 100 * dt
		elif keys['down']:
			self.monster.y -= 100 * dt	


class GameObject:
	def __init__(self, centerX, centerY, height, width):
		self.centerX = centerX
		self.centerY = centerY 
		self.height = height
		self.width = width

class PhysicalPanda(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(Physicalpanda, self).__init__(*args, **kwargs)

		self.velocity_x, self.velocity_y = 0.0, 0.0

	def update(self, dt):
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt

class Player:
    def __init__(self):
        animation = pyglet.resource.animation('panda.png')
        self.player = pyglet.sprite.Sprite(animation, 200, 200)

    def draw(self):
        self.player.draw()

    def update(self, dt, keys):
        if keys['left']:
            self.player.x -= 100 * dt
        elif keys['right']:
            self.player.x += 100 * dt
        elif keys['up']:
            self.player.y += 100 * dt
        elif keys['down']:
            self.player.y -= 100 * dt

def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
