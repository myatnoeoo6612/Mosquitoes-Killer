import pygame

WINDOW_NAME = "Mosquito Killer"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 160
HAND_HITBOX_SIZE = (60, 80)
MOSQUITOS_SIZES = (60, 48)
MOSQUITO_SIZE_RANDOMIZE = (1,2) # for each new mosquito, it will multiply the size with an random value beteewn X and Y
BEE_SIZES = (60, 60)
BEE_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 # the frame of the insects will change every X sec

# difficulty
GAME_DURATION = 30 # the game will last X sec
MOSQUITOS_SPAWN_TIME = 1
MOSQUITOS_MOVE_SPEED = {"min": 4, "max": 8}
BEE_PENALITY = 1 # will remove X of the score of the player (if he kills a bee)

COLORS = {
    "title": (38, 61, 39),
    "score": (38, 61, 39),
    "timer": (38, 61, 39),
    "buttons": {
        "default": (72, 38, 97),  # Dark purple default
        "second": (102, 51, 153),  # Dark purple on hover
        "text": (255, 255, 255),  # White text
        "shadow": (46, 54, 163)  # Shadow color for button
    }
}

# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
