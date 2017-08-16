from game.tasks import task


class BaseScene(task.Task):
    def __init__(self, display_surf, ft, changer):
        task.Task.__init__(self)
        self.display_surf = display_surf
        self.ft = ft
        self.m_scene_changer = changer
