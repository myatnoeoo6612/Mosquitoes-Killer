import pygame
from settings import *

def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
              shadow=False, shadow_color=(0, 0, 0), shadow_offset=2):
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow:  # make the shadow
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))

    surface.blit(label, label_rect)  # draw the text


def button(surface, pos_x, pos_y, text=None, click_sound=None):
    rect = pygame.Rect((pos_x, pos_y), BUTTONS_SIZES)  # Corrected Rect definition

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = (102, 51, 153)  # Dark purple on hover
        on_button = True
    else:
        color = (72, 38, 97)  # Darker purple by default

    # Draw gradient effect (dark purple with a light border)
    gradient_rect = pygame.Rect(rect.x, rect.y, rect.w, rect.h)
    pygame.draw.rect(surface, color, gradient_rect)
    pygame.draw.rect(surface, (154, 92, 182), gradient_rect, 4)  # Purple border

    # Draw the shadow
    pygame.draw.rect(surface, (46, 54, 163), (rect.x - 6, rect.y - 6, rect.w, rect.h))  # Shadow rectangle

    # Draw the text
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["buttons"]["text"], pos_mode="center",
                  shadow=True, shadow_color=(255, 255, 255))

    if on_button and pygame.mouse.get_pressed()[0]:  # if the user presses on the button
        if click_sound is not None:  # play the sound if needed
            click_sound.play()
        return True
    return False

