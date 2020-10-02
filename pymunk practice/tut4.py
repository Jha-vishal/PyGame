############ CALCULATE MOMENT OF INERTIA FOR POLY   ##################


import pyglet
import pymunk

from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1080, 620, "Angry bird game", resizable=False)

options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, -1000  # (x,y)

body = pymunk.Body(1, 1666) # It require mass and moment of inertia
body.position = 540, 600  # (x,y)

poly = pymunk.Poly.create_box(body, size=(50, 50))

    # Calculate the moment of inertia for a solid polygon shape.
    # Assumes the polygon center of gravity is at its centroid. The offset is added to each vertex.
moment = pymunk.moment_for_poly(1, poly.get_vertices())    # It require mass, vertices
print(moment)
    
    
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