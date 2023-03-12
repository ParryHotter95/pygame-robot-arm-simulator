import pygame
from math import radians, sin, cos
from settings import Settings

class Robot:
    shoulder_angle = 120
    elbow_angle = 45
    origin = (400, 500)
    arm_length = 100
    forearm_length = 100

    def __init__(self, app) -> None:
        self.settings = Settings()
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
    
    def _calculate_position(self):
        self.elbow_position = (self.arm_length*cos(radians(self.shoulder_angle)),
                               self.arm_length*sin(radians(self.shoulder_angle)))
        self.wrist_position = (self.elbow_position[0]
                                + self.forearm_length*cos(radians(self.elbow_angle)),
                                self.elbow_position[1]
                                + self.forearm_length*sin(radians(self.elbow_angle)))
    
    def _transpose_to_WH(self, point):
        return (self.origin[0]+point[0], self.origin[1]-point[1])
    
    def draw(self):
        #draw a base
        base_width = 40
        base_height = 20
        left = self.origin[0] - base_width/2
        top = self.origin[1]
        base_rect = pygame.Rect(left, top, base_width, base_height)
        pygame.draw.rect(self.screen, self.settings.base_color, base_rect)
        #draw an arm
        self._calculate_position()
        elbow = self._transpose_to_WH(self.elbow_position)
        pygame.draw.line(self.screen, self.settings.arms_color,
                         self.origin, elbow, self.settings.arms_width)
        #draw a forearm
        wrist = self._transpose_to_WH(self.wrist_position)
        pygame.draw.line(self.screen, self.settings.arms_color,
                         elbow, wrist, self.settings.arms_width)
        #draw joints
        pygame.draw.circle(self.screen, self.settings.joints_color,
                           elbow, self.settings.joints_rad)
        pygame.draw.circle(self.screen, self.settings.joints_color,
                           wrist, self.settings.joints_rad)