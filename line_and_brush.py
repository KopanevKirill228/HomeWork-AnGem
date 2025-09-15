import pygame as pg
import sys


screen = pg.display.set_mode((800, 600))
WHITE = (255, 255, 255)
#наивный алгоритм

def naiv_alg(first_x, second_x, first_y, second_y):
    k = (second_y - first_y) / (second_x - first_x)
    for x in range(min(first_x, second_x), max(first_x, second_x) + 1):
        screen.set_at((x, int(first_y + (x - first_x) * k)), WHITE)

naiv_alg(100, 200, 100, 300)

#алгоритм брезенхема

def brez_alg(first_x, second_x, first_y, second_y):
    screen.set_at((first_x, first_y), WHITE)
    dx = abs(second_x - first_x)
    dy = abs(second_y - first_y)
    if first_x < second_x:
        sx = 1
    else:
        sx = -1
    if first_y < second_y:
        sy = 1
    else:
        sy = -1

    e = dx - dy
    while not(first_x == second_x and first_y == second_y):
        e2 = e * 2
        if e2 > -dy:
            e -= dy
            first_x += sx
        if e2 < dx:
            e += dx
            first_y += sy
        if first_x == 400 and first_y == 400:
            print(1)
        screen.set_at((first_x, first_y), WHITE)

brez_alg(200, 300, 100, 300)



#реализация заливки (попробуйте залить квадрат, который я отрисовал)
#чтобы залить область нажмите ЛКМ на квадрат. Заливает все белым цветом для лаконичности.
#сделать выбор цветов довольно несложно


sys.setrecursionlimit(10000)
def zalivka(position, color):
    x = position[0]
    y = position[1]

    if x < 0 or x >= 800 or y < 0 or y >= 600:
        return

    if screen.get_at((x, y)) == color:
        return

    screen.set_at((x, y), color)

    need_move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(len(need_move)):
        sx, sy = need_move[i]
        zalivka((x + sx, y + sy), color)



#(отрисовка четырех линий снизу, чтобы попробовать залить какую-либо область)

brez_alg(400, 400, 400, 500)
brez_alg(500, 500, 400, 500)
brez_alg(400, 500, 400, 400)
brez_alg(500, 400, 500, 500)

pg.display.update()
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                color = screen.get_at((x, y))
                zalivka((x, y), WHITE)

    pg.display.flip()



