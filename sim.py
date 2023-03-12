import sys, pygame
from settings import Settings
from robot import Robot
from debugger import Debugger

class App:
    def __init__(self) -> None:
        self.settings = Settings()
        pygame.init()
        self.screen = pygame.display.set_mode(self.settings.window_size)
        pygame.display.set_caption("Robot arm simulator")
        self.robot = Robot(self)
        self.debugger = Debugger(self)
    
    def run_simulation(self):
        while True:
            self._check_events()            
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.robot.draw()
        self.debugger.draw()
        pygame.display.flip()

if __name__ == '__main__':
    app = App()
    app.run_simulation()