import pygame
import random
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        m_x = 0
        m_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x = (event.pos[0] // 32) * 32
                    click_y = (event.pos[1] // 32) * 32

                    if click_x == m_x and click_y == m_y:
                        m_x = (random.randrange(0, 640) // 32) * 32
                        m_y = (random.randrange(0, 512) // 32) * 32
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(m_x, m_y)))
            for x in range(0, 641, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 513, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
