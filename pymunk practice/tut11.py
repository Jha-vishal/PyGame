""" COLLISION HANDLER  """


import pyglet
import pymunk

from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1080, 620, "Angry bird game", resizable=False)

options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, -1000  # (x,y)

mass = 1
radius = 30

######## Circle ##############
circle_moment = pymunk.moment_for_circle(mass, 0, radius)
circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = 700, 600
circle_shape = pymunk.Circle(circle_body, radius)
## Set Elasticity ##
circle_shape.elasticity = 0.8   # By using this the object can jump on the surface
circle_shape.friction = 1.0      # By using this we can rotate the object

space.add(circle_body, circle_shape)

############# Segment (Line) ###########
# segment_moment1 = pymunk.moment_for_segment(mass, (0,0), (800,0), 2)
# segment_body1 = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape1 = pymunk.Segment(space.static_body, (0,0), (800,40), 2)   # Static body used to hold the object on the screen
# segment_body1.position = 500, 400
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

##### Collision handler
def coll_begin(arbiter, space, data):
    print("begin")
    return True

def coll_pre(arbiter, space, data):
    print("Pre solve")
    return True

def coll_post(arbiter, space, data):
    print("Post solve")

def coll_seprate(arbiter, space, data):
    print("Seprate")

handler = space.add_default_collision_handler()
handler.begin = coll_begin
handler.pre_solve = coll_pre
handler.post_solve = coll_post
handler.separate = coll_seprate

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()