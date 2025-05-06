import pygame
import sys
import random
import config

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        buffer = 10

        self.x = random.randint(self.radius + buffer, config.WINDOW_WIDTH - self.radius - buffer)
        self.y = random.randint(self.radius + buffer, config.WINDOW_HEIGHT - self.radius - buffer)

        self.change_x = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.change_y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y


        if self.x <= self.radius or self.x >= config.WINDOW_WIDTH - self.radius:
            self.change_x *= -1

        if self.y <= self.radius or self.y >= config.WINDOW_HEIGHT - self.radius:
            self.change_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption("Bouncing Circles")

    circles = [
        Circle(25, config.RED),
        Circle(30, config.GREEN),
        Circle(35, config.LIGHT_BLUE),
        Circle(40, config.ORANGE)
    ]

    clock = pygame.time.Clock()
    running = True

    while running:
        running = handle_events()

        for circle in circles:
            circle.move()

        screen.fill(config.WHITE)

        for circle in circles:
            circle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
