import pygame
import random
import image
from settings import *
from mosquito import Mosquito

class Bee(Mosquito):
    def __init__(self):
        # Size
        random_size_value = random.uniform(BEE_SIZE_RANDOMIZE[0], BEE_SIZE_RANDOMIZE[1])
        size_multiplier = 1.2  # Increase bee size by 20%
        size = (int(BEE_SIZES[0] * random_size_value * size_multiplier),
                int(BEE_SIZES[1] * random_size_value * size_multiplier))
        
        # Moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        
        # Sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0] // 1.4, size[1] // 1.4)
        self.images = [image.load(f"Assets/bee/{nb}.png", size=size, flip=moving_direction == "right") 
                        for nb in range(1, 7)]  # Load the images
        self.current_frame = 0
        self.animation_timer = 0

    def kill(self, mosquitos):  # Remove the mosquito from the list
        mosquitos.remove(self)
        return -BEE_PENALITY
