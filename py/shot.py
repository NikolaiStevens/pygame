import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        # Initialize the shot at the player's position
        super().__init__(x, y, SHOT_RADIUS)  # Use the SHOT_RADIUS constant
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED  # Set velocity based on player rotation

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)  # Draw using the shot's radius

    def update(self, dt):
        # Update position using velocity
        self.position += self.velocity * dt
        
        # Remove bullet if it goes off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  # Remove bullet from all groups
