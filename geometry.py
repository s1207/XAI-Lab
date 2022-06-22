
from manimlib import *
#from manimlib.mobject.geometry import Circle

import parser


class Geometry(Scene):
    def construct(self, family_list):
        for person in family_list:
            circle = Circle(radius=1.5)
            circle.set_fill(BLUE, opacity=0.1)
            circle.set_stroke(BLUE_E, width=4)
            circle.center = (1, 2)
            self.add(circle)