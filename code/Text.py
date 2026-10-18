import pygame
import pymunk
import pymunk.pygame_util


# Render a text label once and keep its surface and screen position together.
class Text:
    # RGB colors used for the game interface.
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    # Base font size, scaled when a label is created.
    SIZE = 100
    MAIN_FONT = "res/fonts/BKANT.ttf"

    def __init__(self, font_source, scale_factor, text_color, text, text_pos_x=0, text_pos_y=0):
        # Load the requested font at an integer size adjusted to the window scale.
        main_font = pygame.font.Font(font_source, int(Text.SIZE * scale_factor))
        self.text_surf = main_font.render(text, True, text_color)
        # Store the rendered dimensions for positioning other interface elements.
        self.text_size = pymunk.Vec2d(self.text_surf.get_width(), self.text_surf.get_height())

        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (text_pos_x, text_pos_y)

    def to_draw(self):
        """Return the source surface and destination rectangle."""
        return self.text_surf, self.text_rect

    def set_text_center(self, text_pos):
        """Move the existing label without rendering the text again."""
        self.text_rect.center = text_pos
