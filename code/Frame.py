import pymunk
import pymunk.pygame_util


# Base class for the static collision segments that form the court.
class Frame:

    def __init__(self, space, pos1, pos2, width):
        # Store both endpoints as vectors for later coordinate access.
        self.position1 = pymunk.Vec2d(*pos1)
        self.position2 = pymunk.Vec2d(*pos2)
        self.width = width
        # Static bodies remain fixed and are not moved by gravity or collisions.
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, pos1, pos2, width)
        space.add(self.body, self.shape)

    def get_shape(self):
        """Expose the collision shape for contact checks and material properties."""
        return self.shape

    def get_positions(self):
        """Return the segment endpoints in physics coordinates."""
        return self.position1, self.position2


# Ground segments use the base shape without overriding its material properties.
class Ground(Frame):

    def __init__(self, space, pos1, pos2, width):
        super(Ground, self).__init__(space, pos1, pos2, width)


# Court boundaries with bounce and friction configured below.
class Wall(Frame):

    def __init__(self, space, pos1, pos2, width):
        super(Wall, self).__init__(space, pos1, pos2, width)
        # Configure restitution (bounce) and friction for collisions.
        self.shape.elasticity = 0.99
        self.shape.friction = 0.99


# The net shares the static segment behavior and adds its own drawing color.
class Net(Frame):
    NET_COLOR = (150, 80, 0, 255)
    # Base size used by the game when calculating the scaled segment radius.
    THICKNESS = 5

    def __init__(self, space, pos1, pos2, width):
        super(Net, self).__init__(space, pos1, pos2, width)
        # Configure restitution (bounce) and friction for collisions.
        self.shape.elasticity = 0.99
        self.shape.friction = 0.99
        self.shape.color = Net.NET_COLOR
