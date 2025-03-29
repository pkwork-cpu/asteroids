from CircleShape import *
import random

class Asteroid(CircleShape):
        def __init__(self, x, y, radius):
                super().__init__(x, y, radius)

        def draw(self, screen):
                pygame.draw.circle(screen, "white", self.position, self.radius, 2)
                

        def update(self, dt):
                # Move the asteroid in a random direction 
                self.position += self.velocity * dt
        def split(self):
                self.kill()
                if self.radius <= ASTEROID_MIN_RADIUS:
                        return
                else:
                        random_angle = random.uniform(20, 50)
                        astroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                        astroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                        astroid1.velocity = self.velocity.rotate(random_angle)
                        astroid2.velocity = self.velocity.rotate(-random_angle)
                        astroid1.velocity *= 1.2
                        astroid2.velocity *= 1.2
