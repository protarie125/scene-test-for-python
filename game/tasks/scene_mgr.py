from game.locals import constants as const
from game.tasks import scene_changer as sc
from game.tasks import task
from game.tasks import menu
from game.tasks import game


class SceneMgr(sc.SceneChanger, task.Task):
    def __init__(self, display_surf, ft):
        sc.SceneChanger.__init__(self)
        task.Task.__init__(self)
        self.display_surf = display_surf
        self.ft = ft
        self.m_scene = menu.Menu(self.display_surf, self.ft, self)
        self.m_next_scene = const.e_scene_none

    def initialize(self):
        self.m_scene.initialize()

    def finalize(self):
        self.m_scene.finalize()

    def update(self):
        if not self.m_next_scene == const.e_scene_none:
            self.m_scene.finalize()
            del self.m_scene

            # e_scene if-elif
            if self.m_next_scene == const.e_scene_menu:
                self.m_scene = menu.Menu(self.display_surf, self.ft, self)
            elif self.m_next_scene == const.e_scene_game:
                self.m_scene = game.Game(self.display_surf, self.ft, self)

            self.m_next_scene = const.e_scene_none
            self.m_scene.initialize()

        self.m_scene.update()

    def draw(self):
        self.m_scene.draw()

    def change_scene(self, next_scene):
        self.m_next_scene = next_scene
