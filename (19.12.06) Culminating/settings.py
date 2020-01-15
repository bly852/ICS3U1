#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school
#                 collecting food for the food drive.

# game variables and settings

# colours
blue = (66, 144, 245)
red = (247, 59, 49)
green = (62, 247, 49)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
lightgrey = (100, 100, 100)


# game options
width, height = 800, 600 # (640x480 or 800x600 or 1024x768 or 1280x1024)
fps = 120 # fps limit
title = 'Food Wars'
time_limit = 60 # game time limit in seconds


# tiles
tileSize = 32
gridWidth = width / tileSize
gridHeight = height / tileSize


# player settings
player_speed = 400


# images
player1_image = 'hitman1_hold.png'
player2_image = 'manBlue_hold.png'
floor_image = 'brick_floor32x32.png'
wall_image = 'mask_32x_0.png'


# food settings
food_spawn_rate = 30 # lower number = more food
food_spawn_timer = 0.1 # seconds between food spawn


# text settings
default_font = 'Segoe UI.ttf'
default_font_bold = 'Segoe UI Bold.ttf'
