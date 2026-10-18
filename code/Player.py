import pygame
import pymunk
import pymunk.pygame_util


# Manage a player's physics, movement state, ball contacts, and score.
class Player:
    # Base properties scaled to the game window when the player is created.
    MASS = 100
    VELOCITY = 400.0
    JUMP_VELOCITY = 800.0
    RADIUS = 40
    IMAGE = {'player1': "res/img/player1.png", 'player2': "res/img/player2.png"}

    def __init__(self, space, pos, scale_factor):
        # Scale horizontal properties by x and jump velocity by y.
        self.mass = Player.MASS * scale_factor['x']
        self.radius = Player.RADIUS * scale_factor['x']
        self.jump_velocity = Player.JUMP_VELOCITY * scale_factor['y']
        self.speed = Player.VELOCITY * scale_factor['x']

        # Save the initial position for resetting the player between points.
        self.start_pos = pymunk.Vec2d(*pos)
        self.jumping = False

        self.block_move = {'left': False, 'right': False}
        self.won = False
        # Serving status determines the allowed number of consecutive ball contacts.
        self.serves = True
        self.dominates = False
        self.collides_with_ball = False
        self.bounce_counter = 0
        self.score = 0

        # Model the player as a dynamic solid disk with the corresponding inertia.
        moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, moment)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, self.radius)

        self.shape.color = pygame.color.THECOLORS["black"]
        # Set collision bounce and friction.
        self.shape.elasticity = 0.99
        self.shape.friction = 0.4
        # Register both the physical body and its collision shape.
        space.add(self.body, self.shape)

        # Preserve vertical speed only, horizontal movement is controlled by input.
        self.attribute_to_pause = self.body.velocity.y
        # Keep a visible position for rendering while the body is moved off court.
        self.position_to_breaks = self.body.position

    def get_position(self):
        return self.body.position

    def get_radius(self):
        return self.radius

    def get_block_move(self):
        return self.block_move

    def get_start_position(self):
        return self.start_pos

    def get_shape(self):
        return self.shape

    def get_score(self):
        return self.score

    def get_position_to_breaks(self):
        return self.position_to_breaks

    def check_bounce_counter(self):
        """Return whether the player has exceeded the allowed number of ball contacts."""
        if self.serves:
            return self.bounce_counter > 1
        else:
            return self.bounce_counter > 3

    def check_if_won(self):
        """Return whether the player has at least 21 points and leads by at least two."""
        return self.score >= 21 and self.dominates

    def is_jumping(self):
        return self.jumping

    def is_falling(self):
        """Return whether the player is jumping with zero or negative vertical velocity."""
        return self.jumping and self.body.velocity.y <= 0.0

    def is_sleeping(self):
        return self.body.is_sleeping

    def collision_with_ball(self):
        """Return whether the player is marked as being in contact with the ball."""
        return self.collides_with_ball

    def set_dominance(self, dominance):
        self.dominates = dominance

    def set_serving(self, serving):
        self.serves = serving

    def set_collision_with_ball(self, collides):
        self.collides_with_ball = collides

    def set_block_move(self, is_blocked, direction):
        """Set whether movement in the given direction is blocked."""
        self.block_move[direction] = is_blocked

    def set_position_to_start_pos(self):
        """Restore the initial position without changing velocities or gameplay flags."""
        self.body.position = self.start_pos

    def set_jumping(self, is_jumping):
        self.jumping = is_jumping

    def set_position(self, pos):
        self.body.position = pos

    def set_start_rotation(self):
        """Reset the body angle and angular velocity to zero."""
        self.body.angle = 0.0
        self.body.angular_velocity = 0.0

    def reset_bounce_counter(self):
        """Reset the number of consecutive ball contacts to zero."""
        self.bounce_counter = 0

    def increment_bounce_counter(self):
        """Increase the ball contact counter by one."""
        self.bounce_counter += 1

    def is_winner(self):
        """Mark the player as the winner."""
        self.won = True

    def clear_score(self):
        """Reset the score and clear the winner flag."""
        self.won = False
        self.score = 0

    def jump(self):
        """Start a jump by setting upward velocity and clearing horizontal velocity."""
        self.body.velocity = pymunk.Vec2d(0.0, self.jump_velocity)
        self.jumping = True

    def moves(self, direction):
        """Set horizontal velocity preserving vertical velocity."""
        self.body.velocity = pymunk.Vec2d(direction * self.speed, self.body.velocity.y)

    def stop(self):
        """Stop horizontal movement while preserving vertical velocity."""
        self.body.velocity = pymunk.Vec2d(0.0, self.body.velocity.y)

    def definitive_stop(self):
        """Stop linear movement on both axes without changing angular velocity."""
        self.body.velocity = pymunk.Vec2d.zero()

    def wakes_up(self):
        """Restore the saved vertical velocity and clear horizontal velocity."""
        self.body.velocity = pymunk.Vec2d(0.0, self.attribute_to_pause)

    def sleep(self):
        """Put the physical body to sleep until it is activated again."""
        self.body.sleep()

    def save_attribute_to_pause(self):
        """Save the current vertical velocity for resuming after a pause."""
        self.attribute_to_pause = self.body.velocity.y

    def save_position(self):
        """Save the current position for rendering during the break between points."""
        self.position_to_breaks = self.body.position

    def gained_point(self):
        """Increase the score by one."""
        self.score += 1
