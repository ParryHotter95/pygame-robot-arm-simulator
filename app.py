import pyglet
from robot import Robot
from settings import Settings

class App(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = Settings()
        self.robot = Robot(self)
        self.label = pyglet.text.Label("Hello, World!",
                      font_name='Times New Roman',
                      font_size=36,
                      x=self.width//2, y=self.height//2,
                      anchor_x='center', anchor_y='center')
        pyglet.app.run()
   
    def on_mouse_motion(self, x, y, dx, dy):
        text = f'{x=}, {y=}, {dx=}, {dy=}'
        #print(text)
        self.mouse_position_label = pyglet.text.Label(text,
                              font_name='Times New Roman',
                              font_size=16,
                              x=5, y=5)

    def on_draw(self):
        self.clear()
        self.robot.draw()
        self.mouse_position_label.draw()

if __name__ == "__main__":
    window = App()
    pyglet.app.run() 
