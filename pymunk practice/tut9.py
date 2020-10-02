""" SIMPLE SIMULATION PART 1  """


import pyglet
import pymunk

from pymunk.pyglet_util import DrawOptions
from math import degrees

window = pyglet.window.Window(1080, 620, "Angry bird game", resizable=False)

options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, -250  # (x,y)

mass = 1
radius = 30


############# Segment (Line) ###########
segment_shape1 = pymunk.Segment(space.static_body, (0,0), (800,40), 2)   # Static body used to hold the object on the screen
segment_shape1.body.position = 500, 400
## Set Elasticity ##
segment_shape1.elasticity = 0.8    # By using this the object can jump on the surface
segment_shape1.friction = 0.1
space.add(segment_shape1)


segment_shape2 = pymunk.Segment(space.static_body, (0,60), (800,0), 2) 
segment_shape2.body.position = 100, 100
segment_shape2.elasticity = 0.8    # By using this the object can jump on the surface
segment_shape2.friction = 1.0 
space.add(segment_shape2)


# space.add(circle_body, circle_shape, segment_shape1, segment_shape2)

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
   
@window.event
def on_mouse_press(x, y, button, modifiers):
    ######## Circle ##############
    circle_moment = pymunk.moment_for_circle(mass, 0, radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x, y
    circle_shape = pymunk.Circle(circle_body, radius)
    ## Set Elasticity ##
    circle_shape.elasticity = 0.8   # By using this the object can jump on the surface
    circle_shape.friction = 1.0      # By using this we can rotate the object

    space.add(circle_body, circle_shape)


def update(dt):
    space.step(dt)
    ## To reduce the processing time and remove the shapes after they are not on the screen
    for shape in space.shapes:
        if shape.body.position.y < -100 or shape.body.position.x > 1110:
            space.remove(shape.body, shape)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()