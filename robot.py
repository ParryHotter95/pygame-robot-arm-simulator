import pyglet
from math import radians, sin, cos

class Robot:
    shoulder_angle = 120
    elbow_angle = 45
    origin = (400, 100)
    arm_length = 200
    forearm_length = 200

    def __init__(self, app) -> None:
        # self.screen = app.screen
        # self.screen_rect = app.screen.get_rect()
        self.app = app
        self.settings = self.app.settings
    
    def _calculate_position(self):
        self.elbow_position = (self.origin[0]+self.arm_length*cos(radians(self.shoulder_angle)),
                               self.origin[1]+self.arm_length*sin(radians(self.shoulder_angle)))
        self.wrist_position = (self.elbow_position[0]
                                + self.forearm_length*cos(radians(self.elbow_angle)),
                                self.elbow_position[1]
                                + self.forearm_length*sin(radians(self.elbow_angle)))
  
    def draw(self):
        #draw a base
        base = pyglet.shapes.Rectangle(self.origin[0], self.origin[1], 40, 20,
                                        color=(200, 200, 200))
        base.anchor_position = 20, 10
        base.draw()
        #draw an arm
        self._calculate_position()
        arm = pyglet.shapes.Line(self.origin[0], self.origin[1],
                                self.elbow_position[0], self.elbow_position[1],
                                width=20, color=(255, 255, 255, 255))
        arm.draw()
        #draw a forearm
        forearm = pyglet.shapes.Line(self.elbow_position[0], self.elbow_position[1],
                                    self.wrist_position[0], self.wrist_position[1],
                                    width=20, color=(255, 255, 255, 255))
        forearm.draw()
        #draw joints
        elbow = pyglet.shapes.Circle(self.elbow_position[0], self.elbow_position[1], 14,
                                    color=(255, 0, 0))
        elbow.draw()
        wrist = pyglet.shapes.Circle(self.wrist_position[0], self.wrist_position[1], 14,
                                    color=(255, 0, 0))
        wrist.draw()

