import pyglet
from robot import Robot
from settings import Settings

class App(pyglet.window.Window):
    debug = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = Settings()
        self.robot = Robot(self)
   
    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_UP and\
            self.robot.shoulder_angle < self.settings.shoulder_max_angle-1:
            self.robot.shoulder_angle += 1
        if motion == pyglet.window.key.MOTION_DOWN and\
            self.robot.shoulder_angle >= self.settings.shoulder_min_angle+1:
            self.robot.shoulder_angle -= 1
        if motion == pyglet.window.key.MOTION_RIGHT and\
            self.robot.elbow_angle >= self.settings.elbow_min_angle+1:
            self.robot.elbow_angle -= 1
        if motion == pyglet.window.key.MOTION_LEFT and\
            self.robot.elbow_angle < self.settings.elbow_max_angle-1:
            self.robot.elbow_angle += 1

    def show_position(self):
        lines = (f'alpha = {self.robot.shoulder_angle}',
                 f'beta = {self.robot.elbow_angle}')
        for i, line in enumerate(lines):
            text = pyglet.text.Label(line, font_size=25, x=self.width-200,
                                     y=self.height-40-40*i)
            text.draw()

    def on_draw(self):
        self.clear()
        self.robot.draw()
        self.show_position()


if __name__ == "__main__":
    window = App()
    #window.debug = True
    pyglet.app.run()
