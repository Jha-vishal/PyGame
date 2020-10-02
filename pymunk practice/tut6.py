############ CREATE CUSTOM SHAPES   ##################


import pyglet
import pymunk

from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1080, 620, "Angry bird game", resizable=False)

options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, 0  # (x,y)

mass = 1
radius = 30

######## Circle ##############
circle_moment = pymunk.moment_for_circle(mass, 0, radius)
circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = 100, 100
circle_shape = pymunk.Circle(circle_body, radius)

#############  Square(POLY) ##############
poly_shape = pymunk.Poly.create_box(None, size=(50,50))
poly_moment = pymunk.moment_for_poly(mass, poly_shape.get_vertices())
poly_body = pymunk.Body(mass, poly_moment)
poly_shape.body = poly_body
poly_body.position = 250,100

############# Segment (Line) ###########
segment_moment = pymunk.moment_for_segment(mass, (0,0), (0,400), 2)
segment_body = pymunk.Body(mass, segment_moment)
segment_shape = pymunk.Segment(segment_body, (0,0), (0,400), 2)
segment_body.position = 400, 100

############ Triangle ###########
triangle_shape = pymunk.Poly(None, ((0,0), (100,0), (50,100)))
triangle_moment = pymunk.moment_for_poly(mass, triangle_shape.get_vertices())
triangle_body = pymunk.Body(mass, triangle_moment)
triangle_body.position = 550, 100
triangle_shape.body = triangle_body

########### Pentagon #########
penta_shape = pymunk.Poly(None, ((0,0), (100,0), (150,100), (50,200), (-50, 100)))
penta_moment = pymunk.moment_for_poly(mass, penta_shape.get_vertices())
penta_body = pymunk.Body(mass, penta_moment)
penta_body.position = 700,100
penta_shape.body = penta_body

space.add(circle_body, circle_shape, poly_body, poly_shape, segment_body, segment_shape, triangle_body, triangle_shape,
                    penta_body,penta_shape)


@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()