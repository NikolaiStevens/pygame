from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # initialize player attributes here
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.PLAYER_RADIUS = PLAYER_RADIUS
        self.PLAYER_TURN_SPEED = PLAYER_TURN_SPEED
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.PLAYER_RADIUS / 1.5  # Use self.PLAYER_RADIUS
        a = self.position + forward * self.PLAYER_RADIUS  # Use self.PLAYER_RADIUS
        b = self.position - forward * self.PLAYER_RADIUS - right  # Use self.PLAYER_RADIUS
        c = self.position - forward * self.PLAYER_RADIUS + right  # Use self.PLAYER_RADIUS
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += self.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.timer > 0:
            self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Create a new Shot at the position of the player
        if self.timer <= 0:  # Only allow shooting if the cooldown timer is 0 or less
            self.timer = PLAYER_SHOOT_COOLDOWN
            return Shot(self.position.x, self.position.y, self.rotation)
        return None