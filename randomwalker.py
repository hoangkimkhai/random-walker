import pygame
from random import shuffle
import time

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* - DFS - BFS - Dijkstra Path Finding Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.intensity = 0
        self.step = 5
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = (self.intensity, self.intensity, self.intensity)
        self.visited = False
        self.rad = width / 2
        self.bg = BLACK
        self.center_x = self.x + self.rad
        self.center_y = self.y + self.rad

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.bg, (self.x, self.y, self.width, self.width))
        pygame.draw.circle(win, self.color, (self.center_x, self.center_y), self.rad / 2)

    def __lt__(self, other):
        return False

    def is_visited(self):
        return self.visited

    def visit(self):
        if self.intensity + self.step <= 255:
            self.intensity += self.step
        else:
            self.intensity = 255
        self.color = (0, self.intensity, 0)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw(win, grid):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    rows = 40
    grid = make_grid(rows, width)
    draw(win, grid)
    start = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos, rows, width)
            start = grid[row][col]
        if start:
            row, col = start.get_pos()
            for option in DIRECTIONS:
                if rows > row + option[0] >= 0 and rows > col + option[1] >= 0:
                    next_spot = grid[row + option[0]][col + option[1]]
                    next_spot.visit()
                    start = next_spot
                    shuffle(DIRECTIONS)
                    draw(win, grid)
                    break


main(WIN, WIDTH)
