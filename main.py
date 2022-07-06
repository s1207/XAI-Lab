from manimlib.scene.scene import Scene
from matplotlib.collections import PatchCollection

import family_parser
import geometry
import os
import pandas as pd
from manim import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

if __name__ == '__main__':
    os.chdir('data')
    df = pd.DataFrame(pd.read_csv('test_family_tree.csv'))
    circle_array = family_parser.parse_csv('test family tree.csv', df)
    family_parser.find_relations(circle_array, df)
    family_parser.initialize_circles(circle_array)
    for person in circle_array:
        family_parser.adjust_circles_for_spouses(person)
        family_parser.adjust_circles_for_children(person)

    # print(circle_array[1].children[1].name)
    circles_list = []
    for person in circle_array:
        circle = plt.Circle((person.xCoordinate, person.yCoordinate), person.radius, color='b', fill=False)
        circles_list.append(circle)
        person.xCoordinate += 2 * person.radius
        # c_y += 1

    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot

    # change default range so that new circles will work
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))

    for circle in circles_list:
        ax.add_patch(circle)

    fig.savefig('plotcircles2.png')
