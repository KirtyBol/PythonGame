import pyglet
from random import randint

window = pyglet.window.Window(height=720, width=1280)

panda_objects = []

import abc


class Component(metaclass=abc.ABCMeta):

    def __init__(self, **kwargs):
        """
        Constructs Component object given passed kwargs.
        
        :param active Defines if the object has to update 
        :param render Defines if the object has to render 
        :param x Defines the x location of the object 
        :param y Defines the y location of the object
        :param width Defines the width of the object
        :param height Defines the height of the object
        """

        # Basic stuff
        self.active = kwargs.get('active', True)
        self.render = kwargs.get('render', True)
        self.debug = kwargs.get('debug', False)
        self.x = kwargs.get('x', 0.0)
        self.y = kwargs.get('y', 0.0)
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)

    @abc.abstractmethod
    def update_self(self):
        pass

    @abc.abstractmethod
    def draw_self(self):
        pass

class panda(Component):

    def __init__(self, *args, **kwargs):
        """
        Creates a sprite using a panda image.
        """
        super(panda, self).__init__(*args, **kwargs)
        self.speed = kwargs.get('speed', 5)
        self.panda_image = pyglet.image.load('panda.png')
        self.width = 50
        self.height = 50
        self.panda_sprite = pyglet.sprite.Sprite(self.panda_image, self.x, self.y)
        self.x_direction = 1
        self.y_direction = 1

        print('panda Created')

    def update_self(self):
        """
        Increments x and y value and updates position.
        Also ensures that the panda does not leave the screen area by changing its axis direction
        :return:
        """
        self.x += (self.speed * self.x_direction)
        self.y += (self.speed * self.y_direction)
        self.panda_sprite.set_position(self.x, self.y)

        if self.x < 0 or (self.x + self.width) > 1280:
            self.x_direction *= -1

        if self.y < 0 or (self.y + self.height) > 720:
            self.y_direction *= -1

    def draw_self(self):
        """
        Draws our panda sprite to screen
        :return:
        """
        self.panda_sprite.draw()

def draw():
    """
    Clears screen and then renders our list of panda objects
    :return:
    """
    window.clear()
    for panda in panda_objects:
        panda.draw_self()


def update(time):
    """
    Updates our list of panda objects
    :param time:
    :return:
    """
    for panda in panda_objects:
        if isinstance(panda, Component):
            panda.update_self()


@window.event
def on_mouse_press(x, y, button, modifiers):
    """
    On each mouse click, we create a new panda object
    """
    print('x: {}, y: {}'.format(x, y))
    panda_objects.append(panda(x=x, y=y, speed=randint(3, 12)))


def main():
    """
    This is the main method. This contains an embedded method
    :return:
    """
    @window.event
    def on_draw():
        draw()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()

main()