############## TYPES OF BODY   ###############


# DYNAMIC = cp.CP_BODY_TYPE_DYNAMIC
"""Dynamic bodies are the default body type.

    They react to collisions,
    are affected by forces and gravity, and have a finite amount of mass.
    These are the type of bodies that you want the physics engine to
    simulate for you. Dynamic bodies interact with all types of bodies
    and can generate collision callbacks.
    """

# KINEMATIC = cp.CP_BODY_TYPE_KINEMATIC
"""Kinematic bodies are bodies that are controlled from your code
    instead of inside the physics engine.

    They arent affected by gravity and they have an infinite amount of mass
    so they don't react to collisions or forces with other bodies. Kinematic
    bodies are controlled by setting their velocity, which will cause them
    to move. Good examples of kinematic bodies might include things like
    moving platforms. Objects that are touching or jointed to a kinematic
    body are never allowed to fall asleep.
    """

# STATIC = cp.CP_BODY_TYPE_STATIC
"""Static bodies are bodies that never (or rarely) move.

    Using static bodies for things like terrain offers a big performance
    boost over other body types- because Chipmunk doesn't need to check for
    collisions between static objects and it never needs to update their
    collision information. Additionally, because static bodies don't
    move, Chipmunk knows it's safe to let objects that are touching or
    jointed to them fall asleep. Generally all of your level geometry
    will be attached to a static body except for things like moving
    platforms or doors. Every space provide a built-in static body for
    your convenience. Static bodies can be moved, but there is a
    performance penalty as the collision information is recalculated.
    There is no penalty for having multiple static bodies, and it can be
    useful for simplifying your code by allowing different parts of your
    static geometry to be initialized or moved separately.
    """

import pyglet
import pymunk

from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1080, 620, "Angry bird game", resizable=False)

options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, -1000  # (x,y)

body = pymunk.Body(1, 1666, pymunk.Body.DYNAMIC) # It require mass and moment of inertia
body2 = pymunk.Body(1, 1666, pymunk.Body.KINEMATIC) # It ignore mass and moment of inertia
# body2 = pymunk.Body(body_type= pymunk.Body.KINEMATIC) # It ignore mass and moment of inertia
body3 = pymunk.Body(1, 1666, pymunk.Body.STATIC) # It ignore mass and moment of inertia
# body3 = pymunk.Body(body_type= pymunk.Body.STATIC) # It ignore mass and moment of inertia
body.position = 640, 300  # (x,y)
body2.position = 540, 500  # (x,y)
body3.position = 440, 400  # (x,y)

poly = pymunk.Poly.create_box(body, size=(50, 50))
poly2 = pymunk.Poly.create_box(body2, size=(50, 50))
poly3 = pymunk.Poly.create_box(body3, size=(50, 50))

    # Add one or many shapes, bodies or joints to the space
space.add(body, poly)
space.add(body2, poly2)
space.add(body3, poly3)

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()