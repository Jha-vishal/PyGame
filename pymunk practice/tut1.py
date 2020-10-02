import pymunk
import time

    # Spaces are the basic simulation unit in Pymunk. You add bodies, shapes and constraints to a space, and then update the space as a whole. They control how all the rigid bodies, shapes, and constraints interact together
space = pymunk.Space()
space.gravity = 0, -1000  # (x,y)


    # A rigid body holds the physical properties of an object. (mass, position, rotation, velocity, etc.) It does not have a shape by itself. If you’ve done physics with particles before, rigid bodies differ mostly in that they are able to rotate. Rigid bodies generally tend to have a 1:1 correlation to sprites in a game. You should structure your game so that you use the position and rotation of the rigid body for drawing your sprite.
#By default set to the dynamic body.
body = pymunk.Body(1, 1666) # It require mass and inertia
body.position = 50, 100  # (x,y)

    # Add one or many shapes, bodies or joints to the space
space.add(body)

while True:
    space.step(0.02)  # 1/50 frames per second
    print(body.position)
    time.sleep(0.5)