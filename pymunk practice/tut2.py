#############  CREATE A PLOY BODY  ############


#   pyglet is a cross-platform windowing and multimedia library for Python,
#    intended for developing games and other visually rich applications.
#   It supports windowing, user interface event handling, Joysticks, OpenGL graphics, loading images and videos,
#   and playing sounds and music. pyglet works on Windows, OS X and Linux.

import pyglet
import pymunk

# This submodule contains helper functions to help with quick prototyping using pymunk together with pyglet.
from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1080, 620, "Angry bird game", resizable=False)

options = DrawOptions()

# Spaces are the basic simulation unit in Pymunk. You add bodies, shapes and constraints to a space, and then update the space as a whole. They control how all the rigid bodies, shapes, and constraints interact together
space = pymunk.Space()
space.gravity = 0, -1000  # (x,y)


    # A rigid body holds the physical properties of an object. (mass, position, rotation, velocity, etc.) It does not have a shape by itself. If you’ve done physics with particles before, rigid bodies differ mostly in that they are able to rotate. Rigid bodies generally tend to have a 1:1 correlation to sprites in a game. You should structure your game so that you use the position and rotation of the rigid body for drawing your sprite.
body = pymunk.Body(1, 1666) # It require mass and moment of inertia
body.position = 540, 600  # (x,y)

poly = pymunk.Poly.create_box(body, size=(50, 50))

    # Add one or many shapes, bodies or joints to the space
space.add(body, poly)

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()