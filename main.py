import pygame
from Tile import tile
from time import sleep
import json

pygame.init()

tiles = []
tile_grid_size = 50

#
# Управление:
#
# Левая кнопка мыши - закрасить
# Правая кнопка мыши - убрать
# ЦФЫВ (WASD) - движение
# ПРОБЕЛ (SPACE) - следующий ход
# К/Е (R/T) - заполнить/очистить карту
# Й/У (Q/E)- увеличить/уменьшить масштаб
#
# N - сохранить
# M - загрузить
#

def generate_tiles(width, height, window, tile_size):
    global tiles
    for y in range(width):
        this_line = []
        for x in range(height):
            new_tile = tile(x, y, window, tile_size)
            this_line.append(new_tile)
        tiles.append(this_line)

def next_move():
    global tiles
    new_tiles = []
    for line in tiles:
        new_line = []
        for this_tile in line:
            vires = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (x == 0 and y == 0) or this_tile.y + y < 0 or this_tile.y + y > tile_grid_size - 1 or this_tile.x + x < 0 or this_tile.x + x > tile_grid_size - 1: pass
                    else:
                        if tiles[this_tile.y + y][this_tile.x + x].type == 2:
                            vires+=1
            if this_tile.type == 0:
                new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                new_tile.offset_x = this_tile.offset_x
                new_tile.offset_y = this_tile.offset_y
                new_tile.type = 0
                new_line.append(new_tile)
            else:
                if this_tile.type == 1:
                    if vires == 1 or vires == 2:
                        new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                        new_tile.offset_x = this_tile.offset_x
                        new_tile.offset_y = this_tile.offset_y
                        new_tile.type = 2
                        new_line.append(new_tile)
                    else:
                        new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                        new_tile.offset_x = this_tile.offset_x
                        new_tile.offset_y = this_tile.offset_y
                        new_tile.type = 1
                        new_line.append(new_tile)
                elif this_tile.type == 2:
                    new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                    new_tile.offset_x = this_tile.offset_x
                    new_tile.offset_y = this_tile.offset_y
                    new_tile.type = 3
                    new_line.append(new_tile)
                elif this_tile.type == 3:
                    new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                    new_tile.offset_x = this_tile.offset_x
                    new_tile.offset_y = this_tile.offset_y
                    new_tile.type = 1
                    new_line.append(new_tile)
                '''
                if k == 2 or k == 3:
                    new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                    new_tile.offset_x = this_tile.offset_x
                    new_tile.offset_y = this_tile.offset_y
                    new_tile.type = 1
                    new_line.append(new_tile)
                else:
                    new_tile = tile(this_tile.x, this_tile.y, this_tile.window, this_tile.size)
                    new_tile.offset_x = this_tile.offset_x
                    new_tile.offset_y = this_tile.offset_y
                    new_tile.type = 0
                    new_line.append(new_tile)
                '''
        new_tiles.append(new_line)
    tiles = new_tiles
    sleep(0.1)

def save():
    all_text = ""
    with open("structure.txt", "w") as file:
        for lines in tiles:
            this_line = ""
            for this_tile in lines:
                this_line += str(this_tile.type) + " "
            all_text += this_line + "\n"
        file.write(all_text)

def load():
    with open("structure.txt", "r") as file:
        y = 0
        x = 0
        for line in file:
            x = 0
            this_line = line.split()
            for number in this_line:
                tiles[y][x].type = int(number)
                x += 1
            y += 1

def main():
    global tiles
    window = pygame.display.set_mode()
    pygame.display.set_caption("Game of life")

    tile_size = 50
    offset_x = 0
    offset_y = 0
    speed = 4
    target_type = 1
    running = True

    generate_tiles(tile_grid_size, tile_grid_size, window, tile_size)
    colors = tiles[0][0].colors
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for lines in tiles:
                        for this_tile in lines:
                            if pygame.Rect((this_tile.x * this_tile.size + offset_x,
                                            this_tile.y * this_tile.size + this_tile.offset_y),
                                           (this_tile.size, this_tile.size)).collidepoint(pygame.mouse.get_pos()):
                                this_tile.type = target_type
                if pygame.mouse.get_pressed()[2]:
                    for lines in tiles:
                        for this_tile in lines:
                            if pygame.Rect((this_tile.x * this_tile.size + offset_x,
                                            this_tile.y * this_tile.size + this_tile.offset_y),
                                           (this_tile.size, this_tile.size)).collidepoint(pygame.mouse.get_pos()):
                                this_tile.type = 0

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    for lines in tiles:
                        for this_tile in lines:
                            if pygame.Rect((this_tile.x * this_tile.size + offset_x,
                                            this_tile.y * this_tile.size + this_tile.offset_y),
                                           (this_tile.size, this_tile.size)).collidepoint(pygame.mouse.get_pos()):
                                this_tile.type = target_type
                if pygame.mouse.get_pressed()[2]:
                    for lines in tiles:
                        for this_tile in lines:
                            if pygame.Rect((this_tile.x * this_tile.size + offset_x,
                                            this_tile.y * this_tile.size + this_tile.offset_y),
                                           (this_tile.size, this_tile.size)).collidepoint(pygame.mouse.get_pos()):
                                this_tile.type = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: next_move()
        if keys[pygame.K_1]: target_type = 1
        if keys[pygame.K_2]: target_type = 2
        if keys[pygame.K_3]: target_type = 3
        if keys[pygame.K_n]: save()
        if keys[pygame.K_m]: load()
        if keys[pygame.K_w]: offset_y += speed
        if keys[pygame.K_a]: offset_x += speed
        if keys[pygame.K_s]: offset_y -= speed
        if keys[pygame.K_d]: offset_x -= speed
        if keys[pygame.K_t]:
            for lines in tiles:
                for this_tile in lines:
                    this_tile.type = 0
        if keys[pygame.K_r]:
            for lines in tiles:
                for this_tile in lines:
                    this_tile.type = 1

        if keys[pygame.K_e]:
            for lines in tiles:
                for this_tile in lines:
                    if this_tile.size > 10:
                        this_tile.size -= speed / 10
                    else: break
        if keys[pygame.K_q]:
            for lines in tiles:
                for this_tile in lines:
                    if this_tile.size < 100:
                        this_tile.size += speed / 10
                    else: break

        window.fill((64, 64, 64))
        for lines in tiles:
            for this_tile in lines:
                this_tile.draw(offset_x, offset_y)
        pygame.draw.rect(window, colors[target_type], pygame.Rect((10, 10), (50, 50)))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
