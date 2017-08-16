import pygame
from pygame.locals import *
from game.locals import terminate
from game.locals import constants as const
from game.tasks import base_scene as bs


class Game(bs.BaseScene):
    def __init__(self, display_surf, ft, changer):
        bs.BaseScene.__init__(self, display_surf, ft, changer)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate.terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.m_scene_changer.change_scene(const.e_scene_menu)
            elif event.type == MOUSEMOTION:
                (const.mouse_x, const.mouse_y) = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                (const.mouse_x, const.mouse_y) = pygame.mouse.get_pos()

    def draw(self):
        self.display_surf.fill(const.black)
        ft_surf1 = self.ft.render('it is the game scene.', True, const.white)
        ft_rect1 = ft_surf1.get_rect()
        ft_rect1.topleft = (0, 0)
        self.display_surf.blit(ft_surf1, ft_rect1)
        ft_surf2 = self.ft.render('press ESC to go to the game scene', True, const.white)
        ft_rect2 = ft_surf2.get_rect()
        ft_rect2.topleft = (0, 30)
        self.display_surf.blit(ft_surf2, ft_rect2)
