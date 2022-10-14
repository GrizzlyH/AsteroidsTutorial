import sys, os
import pygame
from pygame import Vector2
import random


pygame.init()


#  Utility Functions
def gameImageLoad(imagefilepath, size):
    """A utility function, for loading all of the game assets, and converting sizes where necessary"""
    image = pygame.image.load(imagefilepath)
    image = pygame.transform.scale(image, (size[0], size[1]))
    return image


def asteroidImageLoading():
    """Utility function for mass loading the various asteroid images"""
    for imgSize in ['large', 'medium', 'small']:
        for item in os.listdir(f'assets/asteroids/{imgSize}'):
            if str(item)[:2] == 'a1':
                AsteroidImgA[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))
            elif str(item)[:2] == 'a3':
                AsteroidImgB[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))
            elif str(item)[:2] == 'b1':
                AsteroidImgC[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))
            elif str(item)[:2] == 'b3':
                AsteroidImgD[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))
            elif str(item)[:2] == 'c1':
                AsteroidImgE[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))
            elif str(item)[:2] == 'c3':
                AsteroidImgF[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))
            elif str(item)[:2] == 'c4':
                AsteroidImgG[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (200, 200)))


def gameWindowUpdating():
    """Function to handle the updating of the game screen"""
    #  Background Image
    GAMESCREEN.blit(BGIMG, (0, 0))

    player.draw(GAMESCREEN)

    pygame.display.update()


#  Game Objects
class Player:
    def __init__(self, image, coOrds):
        self.img = image
        self.imgRect = self.img.get_rect()
        self.x, self.y = coOrds
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.imgRect.x = self.x - self.width//2
        self.imgRect.y = self.y - self.height//2
        self.pos = Vector2(self.imgRect.x, self.imgRect.y)
        self.direction = Vector2(0, -1)
        self.velocity = Vector2()
        self.rotation_speed = object_rotation_speed
        self.speed = object_speed


    def accelerate(self):
        """Increases the speed of the player object"""
        self.velocity += self.direction * self.speed


    def rotation(self, rotation=1):
        """Accepts input for rotating the objcet"""
        angle = self.rotation_speed * rotation
        self.direction.rotate_ip(angle)


    def _wrap_to_screen(self, position):
        """Wraps the player to the screen"""
        self.x, self.y = position
        return Vector2(self.x % SCREENWIDTH, self.y % SCREENHEIGHT)


    def move(self):
        """Updates the position of the Object"""
        self.pos = self._wrap_to_screen(self.pos + self.velocity)


    def draw(self, window):
        """Accepts the rotation angle of the image, and the latest object coords, puts the image to the gamescreen"""
        angle = self.direction.angle_to(Vector2(0, -1))
        rotated_img = pygame.transform.rotozoom(self.img, angle, 1.0)
        rotated_img_size = Vector2(rotated_img.get_size())
        blit_pos = self.pos - rotated_img_size * 0.5
        window.blit(rotated_img, blit_pos)


#  Game Settings Variables
SCREENWIDTH = 1280
SCREENHEIGHT = 960
object_rotation_speed = 3
object_speed = 0.25
CLOCK = pygame.time.Clock()


#  Pygame display window initialisation
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Asteroids')
icnImg = gameImageLoad('assets/Rocket Ship.png', (20, 20))
icnImg = pygame.transform.rotate(icnImg, -90)
pygame.display.set_icon(icnImg)


#  Pygame loading game assets
BGIMG = gameImageLoad('assets/space.png', (SCREENWIDTH, SCREENHEIGHT))
AsteroidImgA = {'large': [], 'medium': [], 'small': []}
AsteroidImgB = {'large': [], 'medium': [], 'small': []}
AsteroidImgC = {'large': [], 'medium': [], 'small': []}
AsteroidImgD = {'large': [], 'medium': [], 'small': []}
AsteroidImgE = {'large': [], 'medium': [], 'small': []}
AsteroidImgF = {'large': [], 'medium': [], 'small': []}
AsteroidImgG = {'large': [], 'medium': [], 'small': []}
PlayerImg = gameImageLoad('assets/Rocket Ship.png', (50, 50))


#  Run once off functions, load GameObjects
asteroidImageLoading()
player = Player(PlayerImg, (SCREENWIDTH//2, SCREENHEIGHT//2))


#  Main Game Loop
RUNGAME = True
while RUNGAME:

    #  Update game object movements
    player.move()


    #  Event handling for loop, check for quit, and Escape key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNGAME = False

    #  Handling input
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.rotation(-1)
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.rotation(1)
    elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.accelerate()

    gameWindowUpdating()
    CLOCK.tick(60)

pygame.quit()
sys.exit()