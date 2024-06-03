import sys

import pygame

import assets.Nature as Nature
from assets.farm import WIDTH, HEIGHT, FPS, CREATURE_LIST, FOOD_LIST, STATS_TEMPLATE, STATS

pygame.init()
font = pygame.font.SysFont('Arial', 24)
# pygame.Surface.blit(dest=(WIDTH, HEIGHT))
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def display_stats():
    text_surface = font.render(
        STATS_TEMPLATE.format(
            STATS["creatures"],
            STATS["food"],
            STATS["dna"]
        ),
        True,
        (255, 255, 255)
    )
    game_display.blit(text_surface, (WIDTH - 20 - text_surface.get_width(), 30))


def main():
    for _ in range(50):
        Nature.create_creature()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        Nature.create_food()
        game_display.fill((0, 0, 0))
        for creature in CREATURE_LIST:
            creature.redraw()
        display_stats()
        for food in FOOD_LIST:
            food.redraw()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
