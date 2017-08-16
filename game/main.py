# Scene Manager Test v0.0
# By Arie, Prot (2017)
# protarie@gmail.com
# CC BY-NC-SA 3.0

# ref// dixq.net/g/sp_06.html

##########
# import #
##########
import pygame
from game.locals import constants as const
from game.tasks import scene_mgr

###########
# globals #
###########


###########
# classes #
###########


###############
# definitions #
###############


#################
# main function #
#################
def main():
    # set up #
    pygame.init()
    display_surf = pygame.display.set_mode((const.window_x, const.window_y))
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Game Template')

    # locals #
    basic_font = pygame.font.Font(None, 30)
    the_scene_mgr = scene_mgr.SceneMgr(display_surf, basic_font)
    the_scene_mgr.initialize()

    # main game loop #
    while True:
        # game logic #
        the_scene_mgr.update()

        # draw game #
        the_scene_mgr.draw()

        # update #
        pygame.display.update()
        fps_clock.tick(const.fps)

#######
# run #
#######
if __name__ == '__main__':
    main()
