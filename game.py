from pyglet.window import key
import pyglet
from random import randint

class Panda():      #the one thing that appears 
    def __init__(self, width, height, speed):
        """
        Creates a sprite using a panda image.
        """
        self.speed = speed
        panda_image = pyglet.image.load('panda.png')    #loads the image 
        self.width = width
        self.height = height

        self.panda_sprite = pyglet.sprite.Sprite(panda_image)   #makes a sprite of the image
        self.panda_sprite.scale = 0.1                   #makes my panda 10 times smaller 
        self.x_direction = 1
        self.y_direction = 1
        self.x = randint(self.panda_sprite.width, self.width - self.panda_sprite.width)     #random x for the place of the sprite
        self.y = randint(self.panda_sprite.height, self.height - self.panda_sprite.height)  #random y for the place of the sprite
 
        print('panda Created')                          #to see that a panda was created in the window

    def get_sprite(self):
        return self.panda_sprite                        #gives the sprite that gets created

    def update(self, dt):                               #updates the stuff for the panda
        speed = self.speed * dt                         #sets a speed for the sprite
        self.x += (speed * self.x_direction)            #the speed the sprite moves in direction x
        self.y += (speed * self.y_direction)            #the speed the sprite moves in direction y
        self.panda_sprite.set_position(self.x, self.y)  #gives a psoition to the sprite

        if self.x < 0 or self.x > (self.width - self.panda_sprite.width):   #makes sure that the sprite doesn't pass the x of the window
            self.x_direction *= -1

        if self.y < 0 or self.y > (self.height - self.panda_sprite.height): #makes sure that the sprite doesn't pass the y of the window
            self.y_direction *= -1
        return

    def draw(self):                                     #draws the panda sprite 
        self.panda_sprite.draw()


class Spawner():                                        #makes sure that a new panda pops up after x seconds
    def __init__(self, height, width, panda_array):
        self.panda_array = panda_array                  #adds the new sprite to the array
        self.height = height    
        self.width = width
        self.next = 5                                   #next sprite after 5 seconds
        self.tick = 0                                   #to let pyglet know at what tick we are

    def update(self, dt, score):                        #keeps updating to see if a new panda pops up
        self.tick += dt

        if self.tick > self.next:                       #uses the ticks to see 
            speed = 200 + (score * 20)                  #makes sure that the speed gets faster after each point
            print(speed)                                #to see if the speed really gets faster
            self.panda_array.append(Panda(self.width, self.height, speed))
            if (self.next > 2):                         #takes care of the minimum time between sprites
                self.next -= 0.2                        #makes sure that the time between sprites gets smaller
            self.tick = 0                               #resets the amount of ticks


class Window(pyglet.window.Window):                     #creates the window with everything that you need
    def __init__(self):
        super(Window, self).__init__(vsync=False)       #makes sure my background doesn't show any other programs

        #pyglet.clock.schedule(self.update)
        pyglet.clock.schedule_interval(self.update, 1/300)
        pyglet.clock.set_fps_limit(120)

        self.score = 0                                  #starts theh score at 0

        self.panda = []                                 #array with panda sprites
        self.spawner = Spawner(self.height, self.width, self.panda) #the place where the sprite spawns

        self.score_label = pyglet.text.Label('Score: 0',    #the score when the game hasn't started yet
                          font_name='Times New Roman',      #the font for the score
                          font_size=36,                     #the size you see the score in
                          x=self.width//2, y=self.height//2,
                          anchor_x='center', anchor_y='center') #makes sure the score is displayed in the middle of the screen


    def update(self, dt):
        self.spawner.update(dt, self.score)             #updates the score

        for p in self.panda:
            p.update(dt)

        if len(self.panda) > 20:                        #checks if the length of the array is bigger than 20
            self.score = 0                              #resets the score to 0 by an array bigger than 20
            self.panda = []                             #checks the array
            self.spawner = Spawner(self.height, self.width, self.panda)  # Reset the spawner

    def on_draw(self):
        pyglet.clock.tick()                             # Make sure you tick o'l the clock!
        self.clear()

        self.score_label.text = "Score: %s" % self.score    #displays thew score according to the amount of clicked pandas
        self.score_label.draw()                             #possible to draw the score label

        for p in self.panda:
            p.draw()

    def on_mouse_press(self, x, y, button, modifiers):  #what happens when you click
        print('x: {}, y: {}'.format(x, y))              #to see what happens when you click

        for p in self.panda:
            if self.is_colliding(p.get_sprite(), x, y): #if statement for when mouse and sprite collide
                self.panda.remove(p)                    #makes sure that the sprite disappears when clicked
                self.score += 1
                print(self.score)
        #panda_objects.append(panda(x=x, y=y, speed=randint(3, 12)))

    def is_colliding(self, prj, x ,y):                  #sets the click box for the sprite, to make sure that you really have to click the sprite
        x1 = prj.x
        x2 = prj.x + prj.width

        y1 = prj.y
        y2 = prj.y + prj.height

        return x1 < x < x2 and y1 < y < y2

# Create a window and run
win = Window()
pyglet.app.run()