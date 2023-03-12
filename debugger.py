import pygame

class Debugger:
    def __init__(self, app) -> None:
        self.app = app
        self.enabled = True
        if not pygame.font.get_init():
            pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    
    def draw(self):
        if not self.enabled:
            return
        r = self.app.robot
        screen = self.app.screen
        mouse_position = self.font.render(str(pygame.mouse.get_pos()), True, self.app.settings.text_color)
        screen.blit(mouse_position, (10, 560))

