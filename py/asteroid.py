import random
from constants import *
from player import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.set_random_velocity()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Update position using velocity
        self.position += self.velocity * dt
        
        # Wrap around screen edges
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def set_random_velocity(self):
        speed = random.uniform(50, 100)
        angle = random.uniform(0, 360)
        self.velocity = pygame.Vector2(speed, 0).rotate(angle)
    
    def split(self):
        self.kill()
        angle = random.uniform(20, 50)
        new_asteroid1_velocity = self.velocity.rotate(angle) * 1.2  # Increase speed slightly
        new_asteroid2_velocity = self.velocity.rotate(-angle) * 1.2

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        # Only spawn new asteroids if the new radius is larger than the minimum
        if new_asteroid_radius >= ASTEROID_MIN_RADIUS:
            # Spawn two new asteroids with the new radius and velocities
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_asteroid1.velocity = new_asteroid1_velocity  # Assign new velocity

            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_asteroid2.velocity = new_asteroid2_velocity  # Assign new velocity