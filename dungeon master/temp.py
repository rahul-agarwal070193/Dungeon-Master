import pygame
import random
import time
import pyglet
import os

env_x = 10
env_y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (env_x, env_y)

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# initialising constant variable
display_width = 675 * 2
display_height = 350 * 2

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (150, 0, 0)
green = (0, 150, 0)
brown = (139, 69, 19)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

spider_life = 100
x_spider: int = 0
y_spider: int = 0
alive = True

bullet_left = []
bullet_right = []
bullet_up = []
bullet_down = []
velocity = 5
bag = [" ", " ", " "]
tree_dic = {}

bo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, "g1", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "key2", 0, 0, 0, 0],
      [0, 0, 0, 10, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0],
      [0, 1, 0, 10, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, "g2", 1, 1, 1, 1, 1, 10, 0, "exit", 0],
      [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 10, 0, 0, 10, 1, 1, 10, 1, 0, 0, 1, 0],
      [0, 1, 0, 1, 1, 0, 1, 10, 1, 10, 0, "g1", 0, 0, 1, 1, 1, 1, 0, 1, 10, 1, 1, 0, 0, 1, 0],
      [0, 1, 1, 1, 10, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 10, 1, 1, 1, 0, 1, 0],
      [0, 0, 0, 0, 10, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 10, 1, 0, 1, 1, 0],
      [0, 1, 1, 1, 1, 1, 1, 10, 1, 0, 1, 0, 0, 1, 10, 0, 10, 1, 0, 1, 10, 1, 1, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 10, 0, 1, 1, 10, 0, 0, 1, 0, 1, 1, 10, 1, 0, 10, 1, 0],
      [0, 1, 0, 1, 1, 1, 0, 1, 10, 0, "g2", 0, 1, 0, 10, 0, 1, 1, 0, 1, 1, 1, 1, 1, 10, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 10, 10, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
      [0, 1, 1, 1, 0, "key1", 0, 1, 1, 1, 1, 0, 10, 0, 10, 0, 10, 0, 10, 1, 0, 0, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]

# loading images needed
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.flip()

pygame.display.set_caption('DUNGEON HUNTER')
key = pygame.image.load('key1.png')
gate = pygame.image.load('gate1.jpg')
tree = pygame.image.load('tree1.jpg')
bolder = pygame.image.load('bolder1.jpg')
hero = pygame.image.load('standing.png')
spider = pygame.image.load('spider1.jpg')
background = pygame.image.load('bag1.jpg')
axe = pygame.image.load('axe1.jpg')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]


# gameIcon = pygame.image.load('car_type_1.png')
# pygame.display.set_icon(gameIcon)


def tree_cutting():
    global tree_dic
    global bo
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 10:
                tree_dic[i * 100 + j] = 2


def spider_die():
    global x_spider
    global y_spider
    global bo
    global spider_life
    global alive
    # print(spider_life)


def bullet_movement():
    global bullet_down
    global bullet_left
    global bullet_right
    global bullet_up
    global velocity

    for i in bullet_up:
        pygame.draw.circle(gameDisplay, green, (i[0] + 25, i[1]), 5)
        if not is_valid(int((i[0]) / 50), int((i[1]) / 50), True):
            bullet_up.pop(bullet_up.index(i))
        else:
            i[1] = i[1] - velocity

    for i in bullet_down:
        pygame.draw.circle(gameDisplay, green, (i[0] + 25, i[1] + 50), 10)
        if not is_valid(int((i[0]) / 50), int((i[1]) / 50), True):
            bullet_down.pop(bullet_down.index(i))
        else:
            i[1] = i[1] + velocity

    for i in bullet_left:
        pygame.draw.circle(gameDisplay, green, (i[0], i[1] + 25), 10)
        if not is_valid(int((i[0]) / 50), int((i[1]) / 50), True):
            bullet_left.pop(bullet_left.index(i))
        else:
            i[0] = i[0] - velocity

    for i in bullet_right:
        pygame.draw.circle(gameDisplay, green, (i[0] + 50, i[1] + 25), 10)
        if not is_valid(int((i[0]) / 50), int((i[1]) / 50), True):
            bullet_right.pop(bullet_right.index(i))
        else:
            i[0] = i[0] + velocity


def move_spider():
    global x_spider
    global y_spider
    global bo
    global spider_life
    global bullet_left
    global bullet_right
    global bullet_up
    global bullet_down
    global alive
    a = random.randint(1, 4)

    if alive:
        pygame.draw.rect(gameDisplay, (255, 0, 0), (x_spider * 50 + 5, y_spider * 50 + 5, 50, 10))
        pygame.draw.rect(gameDisplay, (0, 128, 0),
                         (x_spider * 50 + 5, y_spider * 50 + 5, 50 - (0.5 * (100 - spider_life)), 10))

        if a == 1:
            if bo[y_spider][x_spider + 1] == 1:
                # print(y_spider, " ", x_spider)
                # print(bo[3][1])
                bo[y_spider][x_spider + 1] = "spider"
                bo[y_spider][x_spider] = 1
                x_spider = x_spider + 1

        if a == 2:
            if bo[y_spider + 1][x_spider] == 1:
                bo[y_spider + 1][x_spider] = "spider"
                bo[y_spider][x_spider] = 1
                # print(bo[y_spider + 2][x_spider])
                y_spider = y_spider + 1

        if a == 3:
            if bo[y_spider][x_spider - 1] == 1:
                bo[y_spider][x_spider - 1] = "spider"
                bo[y_spider][x_spider] = 1
                x_spider = x_spider - 1

        if a == 4:
            if bo[y_spider - 1][x_spider] == 1:
                bo[y_spider - 1][x_spider] = "spider"
                bo[y_spider][x_spider] = 1
                y_spider = y_spider - 1
        if spider_life <= 0:
            alive = False


def things_reward(text, count=None):
    gameDisplay.fill(black)
    font = pygame.font.SysFont("comicsansms", 55)
    text = font.render(text + str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def is_valid(x, y, bullet=None):
    # print(x," ",y)
    global spider_life
    if bo[y][x] == 0:
        return False
    if bo[y][x] == 10:
        return False
    if bo[y][x] == "spider" and bullet == True:
        spider_life = spider_life - 10
        return False
    else:
        return True


def grid(i, j, a, key1, key2):
    y = 5 + i * 50
    x = 5 + j * 50
    wi = 50
    hg = 50

    if (a == 1):
        pygame.draw.rect(gameDisplay, white, [x, y, wi, hg])

    if (a == "key1"):
        pygame.draw.rect(gameDisplay, white, [x, y, wi, hg])
        if (key1 == 0):
            gameDisplay.blit(key, (x - 9, y))

    if (a == "key2"):
        pygame.draw.rect(gameDisplay, white, [x, y, wi, hg])
        if key2 == 0:
            gameDisplay.blit(key, (x - 9, y))

    if (a == 0):
        gameDisplay.blit(bolder, (x, y))

    if (a == 10):
        gameDisplay.blit(tree, (x, y))

    if (a == "g1"):
        gameDisplay.blit(gate, (x, y))
        font = pygame.font.SysFont("ariel", 25)
        text = font.render("1", True, yellow)
        gameDisplay.blit(text, (x + 20, y + 20))

    if (a == "spider"):
        gameDisplay.blit(spider, (x, y))

    if (a == "g2"):
        gameDisplay.blit(gate, (x, y))
        font = pygame.font.SysFont("ariel", 25)
        text = font.render("2", True, yellow)
        gameDisplay.blit(text, (x + 20, y + 20))

    if (a == "exit"):
        pygame.draw.rect(gameDisplay, white, [x, y, wi, hg])
        font = pygame.font.SysFont("ariel", 25)
        text = font.render("EXIT", True, black)
        gameDisplay.blit(text, (x + 5, y + 10))

    if (a == "axe"):
        gameDisplay.blit(axe, (x, y))


def dis_grid(x, y, key1, key2):
    """" for i in range(-2,3):
        cc=x+i
        if(cc>=0 and cc<=27):
            for j in range(-3,4):
                rr=y+j
                if(rr>=0 and rr<=15):
                    grid(y+j,x+i,bo[y+j][x+i],key1,key2)

     """
    for i in range(0, 14):
        for j in range(0, 27):
            grid(i, j, bo[i][j], key1, key2)


def text_objects(text, color, font):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None, car_type=None, life=None, dodged=None, level=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, black, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


# exits game
def quitgame():
    pygame.quit()
    quit()


def instruction():
    intro = True
    gameDisplay.fill(black)

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)

        button("Lets begin", (display_width / 2) - 125, 600, 250, 75, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(20)


def login():
    login_window = pygame.display.set_mode((100, 100))
    # login_window = pygame.display.
    gameDisplay.blit(login_window, (0, 0))
    login_window.fill(white)
    while True:
        print("inside")
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(10)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        title_color = brown
        TextSurf, TextRect = text_objects("Dungeon Hunter", title_color, largeText)
        TextRect.center = ((display_width / 2) - 20, (display_height / 2) - 200)
        gameDisplay.blit(TextSurf, TextRect)
        # car(x,y)

        button("Lets GO!!!!", 50, 350, 250, 75, green, bright_green, login)
        button("Lets GO!!!!", 1100, 350, 250, 75, green, bright_green, game_loop)
        button("Instructions", 1150, 450, 200, 75, green, bright_green, instruction)
        button("Quit", 1200, 550, 150, 75, green, red, quitgame)

        pygame.display.update()
        clock.tick(20)


def game_loop():
    # adding background sound
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.5)

    x = 1  # char x position
    y = 1  # char y position
    x_change = 0
    y_change = 0
    key1 = 0
    key2 = 0
    count = 0
    count1 = 1
    flag = 0
    flag_axe = 0
    bullet = 1
    axe_flag = 0
    global x_spider
    global y_spider
    global bo
    global bag
    gameExit = False
    life = 100

    gameDisplay.fill(black)
    dis_grid(x, y, key1, key2)
    tree_cutting()

    gameDisplay.blit(hero, (x * 50 + 5, y * 50 + 5))

    while not gameExit:
        if life == 0:
            # game over --------------------
            pygame.quit()
            quit()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                if event.key == pygame.K_RIGHT:
                    x_change = 1
                if event.key == pygame.K_UP:
                    y_change = -1
                if event.key == pygame.K_DOWN:
                    y_change = 1

                if event.key == pygame.K_w:
                    if bullet == 1:
                        bullet_up.append([50 * x + 5, 50 * y + 5])
                        bullet_movement()
                    if axe_flag == 1:
                        if bo[y - 1][x] == 10:
                            if tree_dic[(y - 1) * 100 + x] != 0:
                                tree_dic[(y - 1) * 100 + x] -= 1
                            else:
                                bo[y - 1][x] = 1

                if event.key == pygame.K_s:
                    if bullet == 1:
                        bullet_down.append([50 * x + 5, 50 * y + 5])
                        bullet_movement()
                    if axe_flag == 1:
                        if bo[y + 1][x] == 10:
                            if tree_dic[(y + 1) * 100 + x] != 0:
                                tree_dic[(y + 1) * 100 + x] -= 1
                            else:
                                bo[y + 1][x] = 1

                if event.key == pygame.K_a:
                    if bullet == 1:
                        bullet_left.append([50 * x + 5, 50 * y + 5])
                        bullet_movement()
                    if axe_flag == 1:
                        if bo[y][x - 1] == 10:
                            if tree_dic[y * 100 + x - 1] != 0:
                                tree_dic[y * 100 + x - 1] -= 1
                            else:
                                bo[y][x - 1] = 1

                if event.key == pygame.K_d:
                    if bullet == 1:
                        bullet_right.append([50 * x + 5, 50 * y + 5])
                        bullet_movement()
                    if axe_flag == 1:
                        if bo[y][x + 1] == 10:
                            if tree_dic[y * 100 + x + 1] != 0:
                                tree_dic[y * 100 + x + 1] -= 1
                            else:
                                bo[y][x + 1] = 1

                if event.key == pygame.K_c:
                    if axe_flag == 0 and bag[2] == "axe":
                        axe_flag = 1
                        bullet = 0
                    else:
                        axe_flag = 0
                        bullet = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        if is_valid(x, y):
            # map  display
            gameDisplay.fill(black)
            dis_grid(x, y, key1, key2)

            # heath bar
            pygame.draw.rect(gameDisplay, (255, 0, 0), (x * 50 + 5, y * 50 + 5, 50, 10))
            pygame.draw.rect(gameDisplay, (0, 128, 0), (x * 50 + 5, y * 50 + 5, 50 - (0.5 * (100 - life)), 10))

            if x_change > 0:
                gameDisplay.blit(walkRight[count // 3], (x * 50 + 5, y * 50 + 5))
                count = count + 1
                count = count // 3

            if x_change < 0:
                gameDisplay.blit(walkLeft[count1 // 3], (x * 50 + 5, y * 50 + 5))
                count1 = count1 + 1
                count1 = count1 // 3

            else:
                if x_change == 0:
                    gameDisplay.blit(hero, (x * 50 + 5, y * 50 + 5))

        else:
            x = x - x_change
            y = y - y_change

        if x == 5 and y == 12:
            key1 = 1
            things_reward("key1 found ")
            bag[0] = "key1"

        if x == 22 and y == 1:
            key2 = 1
            things_reward("key2 found ")
            bag[1] = "key2"

        if bag[0] == "key1" and x == 11 and y == 5:
            x = 11
            y = 1

        if bag[0] != "key1" and x == 11 and y == 5:
            things_reward("key1 not found")

        if bag[0] == "key1" and x == 10 and y == 1:
            x = 11
            y = 4

        if bag[1] == "key2" and x == 10 and y == 10:
            x = 18
            y = 3
        if bag[1] != "key2" and x == 10 and y == 10:
            things_reward("key2 not found")

        if bag[1] == "key2" and x == 17 and y == 3:
            x = 10
            y = 9

        if x == x_spider and y == y_spider and not alive:
            print(x, " ", y)
            bo[y][x] = 1
            bag[2] = "axe"
            flag_axe = 1

        if x == 25 and y == 3:
            things_reward("end")

        if x == 4 and y == 3 and bo[2][4] == 1:
            bo[3][1] = "spider"
            x_spider = 1
            y_spider = 3
            flag = 1
            bo[2][4] = 0

        if flag == 1 and alive:
            move_spider()
            if x == x_spider and y == y_spider:
                life = life - 5

        if not alive and flag_axe == 0:
            bo[y_spider][x_spider] = "axe"

        bullet_movement()
        pygame.display.update()

        clock.tick(10)


game_intro()
