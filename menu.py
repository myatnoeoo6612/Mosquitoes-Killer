import pygame
import sys
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
import ui

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound("Assets/Sounds/slap.wav")

        # Initialize mixer only if it's not already initialized
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Load and play background music for the menu
        self.menu_music_path = "Assets/Sounds/Komiku - Opening !.mp3"
        self.game_music_path = "Assets/Sounds/Komiku_-_12_-_Bicycle.mp3"
        
        self.play_music(self.menu_music_path)
    
    def play_music(self, music_path):
        """Loads and plays the specified music file."""
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)  # Loop indefinitely
            print(f"Playing music: {music_path}")
        except pygame.error as e:
            print(f"Error loading music: {e}")

    def draw_game_title(self):
        # Load custom arcade-style font (ensure the file path is correct)
        arcade_font = pygame.font.Font("Assets/Pixel.otf", 60)  # Custom font
        title_surface = arcade_font.render(GAME_TITLE, True, COLORS["buttons"]["text"])
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 120))

        # Draw the arcade-style box
        box_color = (154, 92, 182)  # Vibrant purple color
        border_rect = pygame.Rect(title_rect.x - 20, title_rect.y - 20, title_rect.width + 40, title_rect.height + 40)
        pygame.draw.rect(self.surface, box_color, border_rect, border_radius=15)

        # Draw the title text on top of the box
        self.surface.blit(title_surface, title_rect)

    def draw(self):
        # Ensure the background appears
        self.background.draw(self.surface)  # Draw the background
        self.draw_game_title()  # Draw the game title
        # Draw other UI elements

    def update(self):
        self.draw()

        if ui.button(self.surface, 320, 540, "START", click_sound=self.click_sound):
            self.play_music(self.game_music_path)
            return "game"

        if ui.button(self.surface, 700, 540, "QUIT", click_sound=self.click_sound):
            pygame.quit()
            sys.exit()


